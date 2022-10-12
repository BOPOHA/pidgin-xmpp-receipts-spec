# required packages:
# dnf install rpmdevtools rpkg

PROJECTNAME=pidgin-xmpp-receipts
PROJECTTMPDIR=/tmp/$(PROJECTNAME)

clean:
	rm -rf $(PROJECTTMPDIR)

rpmbuild:
	spectool --get-files --directory $(PROJECTTMPDIR) $(PROJECTNAME).spec
	rpkg srpm --spec $(PROJECTNAME).spec --outdir $(PROJECTTMPDIR)
	rpmbuild --nocheck --rebuild $(PROJECTTMPDIR)/$(PROJECTNAME)-*.src.rpm
