%{?scl:%scl_package nodejs-config-chain}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-config-chain
Version:        1.1.9
Release:        3%{?dist}
Summary:        Handle configuration once and for all
BuildArch:      noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
License:        MIT
URL:            https://github.com/dominictarr/config-chain
Source0:        http://registry.npmjs.org/config-chain/-/config-chain-%{version}.tgz
BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Use this module to load all your configurations.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/config-chain
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/config-chain

#fix permissions on non-executable main javascript code file
chmod 0644 %{buildroot}%{nodejs_sitelib}/config-chain/index.js

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/config-chain
%doc LICENCE readme.markdown

%changelog
* Mon Jan 16 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.9-3
- Clean up

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.9-2
- rebuilt

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 1.1.9-1
- New upsteram release

* Tue Mar 04 2014 Tomas Hrcka <thrcka@redhat.com> - 1.1.8-2
- Add missing nodejs_symlink_deps macro

* Thu Jan 16 2014 Tomas Hrcka <thrcka@redhat.com> - 1.1.8-1
- New upstream release 1.1.8

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 1.1.7-2
- replace provides and requires with macro

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.7-1
- new upstream release 1.1.7

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.5-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.5-2
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1.5-2
- Add support for software collections

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.5-1
- new upstream release 1.1.5

* Thu Jan 17 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-3
- fix permissions

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.3-1
- initial package generated by npm2rpm
