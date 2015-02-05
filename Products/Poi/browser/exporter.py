import csv
from cStringIO import StringIO

from Acquisition import aq_inner
from Products.Five.browser import BrowserView

from plone.app.layout.viewlets.content import ContentHistoryViewlet


class CSVExport(BrowserView):
    """ view to produce the CSV exports
    """

    def __call__(self):
        context = aq_inner(self.context)
        encoding = self.request.get('encoding')
        issuefolder = context.restrictedTraverse('@@issuefolder')
        pas_member = context.restrictedTraverse('@@pas_member')

        issues = issuefolder.getFilteredIssues(self.request)
        buffer = StringIO()

        writer = csv.writer(buffer)
        header = [
            '#',
            'Title',
            'Target',
            'Area',
            'Type',
            'Severity',
            'Responsible',
            'Required due date',
            'Tags',
            'State',
            'Last modified by',
            'Last modified by date/time',
            'Version',
            'Submitted by',
            'Submitted date/time',
        ]
        writer.writerow(header)
        for issue in issues:
            obj = issue.getObject()
            chv = ContentHistoryViewlet(obj, self.request, None, None)
            # These attributes are needed, the fullHistory()
            # call fails otherwise
            chv.navigation_root_url = chv.site_url = 'http://www.re-trans.com'
            history = chv.fullHistory()
            last_actor = history[0]['actor'].get('fullname', 'username')

            row = []
            row.append(issue.getId)
            row.append(issue.Title)
            row.append(issue.getTargetRelease.encode('utf-8'))
            row.append(issue.getArea.encode('utf-8'))
            row.append(issue.getIssueType.encode('utf-8'))
            row.append(issue.getSeverity.encode('utf-8'))
            row.append(issue.getResponsibleManager.encode('utf-8'))
            row.append(issue.getDueDate)
            row.append("|".join(issue.Subject))
            row.append(issue.review_state.encode('utf-8'))
            row.append(last_actor.encode('utf-8'))
            row.append(issue.modified)
            row.append(issue.getRelease.encode('utf-8'))
            row.append(
                pas_member.info(issue.Creator)['name_or_id'].encode('utf-8'))
            row.append(issue.CreationDate)
            writer.writerow(row)
        value = buffer.getvalue()
        value = unicode(value, "utf-8").encode("iso-8859-1", "replace")

        if not encoding:
            encoding = 'UTF-8'
        self.request.response.setHeader('Content-type',
                                        'text/csv;charset='+encoding)
        self.request.response.setHeader('Content-Disposition',
                                        'attachment; filename=export.csv')

        return value
