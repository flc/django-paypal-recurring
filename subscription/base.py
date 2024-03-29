import urlparse
from django.utils.translation import ugettext as _
from django.db import models


class ResponseModel(models.Model):
    # Debug information
    raw_request = models.TextField(max_length=512, verbose_name=_(u"raw_request"))
    raw_response = models.TextField(max_length=512, verbose_name=_(u"raw_response"))

    response_time = models.FloatField(help_text=_(u"Response time in milliseconds"), verbose_name=_(u"response_time"))

    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_(u"date created"))

    class Meta:
        abstract = True
        ordering = ('-date_created',)
        app_label = 'subscription'

    def request(self):
        request_params = urlparse.parse_qs(self.raw_request)
        return self._as_table(request_params)

    request.allow_tags = True

    def response(self):
        return self._as_table(self.context)

    response.allow_tags = True

    def _as_table(self, params):
        rows = []
        for k, v in sorted(params.items()):
            rows.append('<tr><th>%s</th><td>%s</td></tr>' % (k, v[0]))
        return '<table>%s</table>' % ''.join(rows)

    @property
    def context(self):
        return urlparse.parse_qs(self.raw_response)

    def value(self, key):
        ctx = self.context
        return ctx[key][0].decode('utf8') if key in ctx else None
