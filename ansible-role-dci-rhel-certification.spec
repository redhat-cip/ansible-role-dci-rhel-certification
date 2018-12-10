Name:       ansible-role-dci-rhel-certification
Version:    0.0.VERS
Release:    1%{?dist}
Summary:    ansible-role-dci-rhel-certification
License:    ASL 2.0
URL:        https://github.com/redhat-cip/ansible-role-dci-rhel-certification
Source0:    ansible-role-dci-rhel-certification-%{version}.tar.gz

BuildArch:  noarch

%description
An Ansible role that use automated certification test

%prep
%setup -qc


%build

%install
mkdir -p %{buildroot}%{_datadir}/dci/roles/dci-rhel-certification
chmod 755 %{buildroot}%{_datadir}/dci/roles/dci-rhel-certification

cp -r files %{buildroot}%{_datadir}/dci/roles/dci-rhel-certification
cp -r tasks %{buildroot}%{_datadir}/dci/roles/dci-rhel-certification


%files
%doc README.md
%license LICENSE
%{_datadir}/dci/roles/dci-rhel-certification


%changelog
* Wed Nov 12 2018 Cedric Lecomte <clecomte@redhat.com> - 0.0.1-1
- Initial release
