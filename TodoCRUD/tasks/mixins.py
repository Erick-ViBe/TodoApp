from django.http import Http404


class IsMyTask:
    """ Check if user task is request user """
    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        if not task.user == self.request.user:
            raise Http404
        return task