# This specfile is licensed under:
# SPDX-License-Identifier: GPL-3.0-or-later

%bcond_without check

# https://github.com/ollama/ollama
%global	goipath	github.com/ollama/ollama

%gometa

%global common_description %{expand:
Get up and running with Llama, Mistral, Gemma, and other large language models}

Name:           ollama
Version:        0.3.4
Release:        1%{?dist}
Summary:        Running many types of LLMs locally

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:	golang 
BuildRequires:	go-rpm-macros
BuildRequires:	systemd-rpm-macros
Requires:       

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

	
%if %{with check}	
%check
%gocheck	
%endif

%gopkgfiles

%changelog
%autochangelog
