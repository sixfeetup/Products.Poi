# Permissions used by Poi

from Products.CMFCore import CMFCorePermissions

View                      = CMFCorePermissions.View
ModifyPortalContent       = CMFCorePermissions.ModifyPortalContent
AccessContentsInformatino = CMFCorePermissions.AccessContentsInformation

ModifyIssueSeverity   = "Poi: Modify issue severity"
ModifyIssueAssignment = "Poi: Modify issue assignment"
ModifyIssueState      = "Poi: Modify issue state"
ModifyIssueTags       = "Poi: Modify issue tags"
ModifyIssueWatchers   = "Poi: Modify issue watchers"

CMFCorePermissions.setDefaultRoles(ModifyIssueSeverity, ['Manager'])
CMFCorePermissions.setDefaultRoles(ModifyIssueAssignment, ['Manager'])
CMFCorePermissions.setDefaultRoles(ModifyIssueState, ['Manager'])
CMFCorePermissions.setDefaultRoles(ModifyIssueTags, ['Manager'])
CMFCorePermissions.setDefaultRoles(ModifyIssueWatchers, ['Manager'])