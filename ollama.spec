# This specfile is licensed under:
# SPDX-License-Identifier: GPL-3.0-or-later

%bcond_without check

%global	goipath		github.com/ollama/ollama
%global forgeurl 	https://github.com/ollama/ollama
Version:	0.3.4
%global tag	v%{version}
%global commit	69eb06c40ec22fe002cfbe1d52b560fce0dcddba
%global godocs	README.md docs/*.md docs/tutorials/*.md
%gometa

%global common_description %{expand:
Get up and running with Llama, Mistral, Gemma, and other large language models}

Name:           ollama
Release:        1%{?dist}
Summary:        Running many types of LLMs locally

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:	golang
BuildRequires:	compiler(go-compiler)
BuildRequires:	go-rpm-macros
BuildRequires:	systemd-rpm-macros
# Requires:       

%description %{common_description}

%global golicenses	LICENSE

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/ollama %{goipath}

%install
%gopkginstall

%if %{with check}	
%check
%gocheck	
%endif

	
%files
%license %{golicenses}
%doc %{godocs}

%gopkgfiles

%changelog
%autochangelog
