# This specfile is licensed under:
# SPDX-License-Identifier: GPL-3.0-or-later

# https://github.com/ollama/ollama
%global	goipath	github.com/ollama/ollama

Name:           ollama
Version:        0.3.4
Release:        1%{?dist}
Summary:        

License:        
URL:            
Source0:        

BuildRequires:	systemd-rpm-macros
BuildRequires:	go-rpm-macros
BuildRequires:	golang 
Requires:       

%description


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Wed Aug 07 2024 Mohammadreza Hendiani <man2dev@fedoraproject.org>
- 
