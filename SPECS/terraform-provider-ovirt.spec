%define debug_package %{nil}

%global gh_user imjoey

Name:           terraform-provider-ovirt
Version:        0.4.2
Release:        1
Summary:        This plugin allows Terraform to work with the oVirt Virtual Machine management platform. It requires oVirt 4.x.
Group:          Applications/System
License:        MPLv2.0
URL:            https://github.com/imjoey/terraform-provider-ovirt
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  golang >= 1.11
BuildRequires:  make which zip

%description
This plugin allows Terraform to work with the oVirt Virtual Machine management platform. It requires oVirt 4.x.

%prep
%setup -q -n %{name}-%{version}

%build
make fmt
GOPROXY= GOARCH=amd64 GOOS=linux go build -o bin/%{name}

%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 0755 bin/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/%{name}

%changelog
* Thu Sep 8 2022 Jamie Curnow <jc@jc21.com> 0.4.2-1
- v0.4.2

* Mon Apr 1 2019 Jamie Curnow <jc@jc21.com> 0.2.0-1
- Initial spec
