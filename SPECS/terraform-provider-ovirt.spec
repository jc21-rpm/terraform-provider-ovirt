%define debug_package %{nil}

%global gh_user imjoey

Name:           terraform-provider-ovirt
Version:        0.2.0
Release:        1
Summary:        This plugin allows Terraform to work with the oVirt Virtual Machine management platform. It requires oVirt 4.x.
Group:          Applications/System
License:        MPLv2.0
URL:            https://github.com/imjoey/terraform-provider-ovirt
Source0:        terraform-provider-ovirt-install
BuildRequires:  golang >= 1.11
BuildRequires:  make which zip


%description
This plugin allows Terraform to work with the oVirt Virtual Machine management platform. It requires oVirt 4.x.

%prep
wget https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz


%build
cd %{name}-%{version}
export GOPATH=$PWD
export PATH=${PATH}:${GOPATH}/bin
export XC_ARCH=amd64
export XC_OS=linux
mkdir -p src/github.com/%{gh_user}/%{name}
shopt -s extglob dotglob
mv !(src) src/github.com/%{gh_user}/%{name}
shopt -u extglob dotglob
pushd src/github.com/%{gh_user}/%{name}
make build
popd


%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 0755 %{name}-%{version}//bin/%{name} $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf %{buildroot}


%files
%{_bindir}/%{name}
%{_bindir}/%{name}-install

%changelog
* Mon Apr 1 2019 Jamie Curnow <jc@jc21.com> 0.2.0-1
- Initial spec

