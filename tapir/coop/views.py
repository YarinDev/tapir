from datetime import date

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.views.generic import UpdateView, CreateView

from django_weasyprint import WeasyTemplateResponseMixin

from tapir.accounts.models import TapirUser
from tapir.coop.forms import CoopShareOwnershipForm, DraftUserForm
from tapir.coop.models import ShareOwnership, DraftUser, ShareOwner


class ShareOwnershipViewMixin(PermissionRequiredMixin):
    permission_required = "coop.manage"
    model = ShareOwnership
    form_class = CoopShareOwnershipForm

    def get_success_url(self):
        # After successful creation or update of a ShareOwnership, return to the user overview page.
        return self.object.owner.get_absolute_url()


class ShareOwnershipUpdateView(ShareOwnershipViewMixin, UpdateView):
    pass


class ShareOwnershipCreateForUserView(ShareOwnershipViewMixin, CreateView):
    def get_initial(self):
        return {"start_date": date.today(), "user": self._get_user()}

    def _get_user(self):
        return get_object_or_404(TapirUser, pk=self.kwargs["user_pk"])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["user"] = self._get_user()
        return ctx

    def form_valid(self, form):
        user = self._get_user()
        if hasattr(user, "coop_share_owner"):
            share_owner = user.coop_share_owner
        else:
            share_owner = ShareOwner.objects.create(user=user, is_company=False)
        form.instance.owner = share_owner
        return super().form_valid(form)


class DraftUserViewMixin(PermissionRequiredMixin):
    permission_required = "coop.manage"
    model = DraftUser
    form_class = DraftUserForm


class DraftUserListView(DraftUserViewMixin, generic.ListView):
    pass


class DraftUserCreateView(DraftUserViewMixin, generic.CreateView):
    pass


class DraftUserUpdateView(DraftUserViewMixin, generic.UpdateView):
    pass


class DraftUserDetailView(DraftUserViewMixin, generic.DetailView):
    pass


class DraftUserDeleteView(DraftUserViewMixin, generic.DeleteView):
    pass


class DraftUserMembershipAgreementView(WeasyTemplateResponseMixin, DraftUserDetailView):
    template_name = "coop/membership_agreement_pdf.html"
    # Show inline, not download view
    pdf_attachment = False

    def get_pdf_filename(self):
        return "Beteiligungserklärung %s %s.pdf" % (
            self.object.first_name,
            self.object.last_name,
        )


@require_POST
@csrf_protect
@permission_required("coop.manage")
def mark_signed_membership_agreement(request, pk):
    u = DraftUser.objects.get(pk=pk)
    u.signed_membership_agreement = True
    u.save()

    return redirect(u)


@require_POST
@csrf_protect
@permission_required("coop.manage")
def mark_attended_welcome_session(request, pk):
    u = DraftUser.objects.get(pk=pk)
    u.attended_welcome_session = True
    u.save()

    return redirect(u)


@require_POST
@csrf_protect
@permission_required("coop.manage")
def create_user_from_draftuser(request, pk):
    draft = DraftUser.objects.get(pk=pk)
    if not draft.signed_membership_agreement:
        # TODO(Leon Handreke): Error message
        return redirect(draft)

    with transaction.atomic():
        u = TapirUser.objects.create(
            username=draft.username,
            first_name=draft.first_name,
            last_name=draft.last_name,
            email=draft.email,
        )
        for _ in range(0, draft.num_shares):
            ShareOwnership.objects.create(
                user=u, start_date=date.today(),
            )
        draft.delete()

    # TODO(Leon Handreke): Why does just passing u here not work?
    return redirect(u.get_absolute_url())


class ActiveShareOwnerListView(generic.ListView):
    model = ShareOwner
    template_name = "coop/shareowner_list.html"

    def get_queryset(self):
        # TODO(Leon Handreke): Allow passing a date
        return ShareOwner.objects.filter(
            share_ownerships__in=ShareOwnership.objects.active_temporal()
        ).distinct()