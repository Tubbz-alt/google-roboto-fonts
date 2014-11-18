
%define _fontsdir               %{_datadir}/fonts
%define _ttffontsdir            %{_fontsdir}/truetype
%define _miscfontsdir           %{_fontsdir}/misc
%define _fontsconfdir           %{_sysconfdir}/fonts
%define _fontsconfddir          %{_fontsconfdir}/conf.d
%define _fontsconfavaildir      %{_datadir}/%{name}/conf.avail

Name:           google-roboto-fonts
Version:        1.2
Release:        1
License:        ASL 2.0
Summary:        Google Roboto fonts
Url:            https://www.google.com/fonts/specimen/Roboto
Group:          System/Fonts
Source:         %{name}-%{version}.tar.xz
Source1001: 	google-roboto-fonts.manifest
BuildArch:      noarch
Requires(post): %{_bindir}/fc-cache

%description
Roboto is a sans-serif typeface family introduced with Android Ice Cream
Sandwich operating system. Google describes the font as "modern, yet
approachable" and "emotional".

%prep
%setup -q
cp %{SOURCE1001} .

%build

%install
mkdir -p %{buildroot}%{_ttffontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttffontsdir}/

%post
if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache %{_ttffontsdir} || :
fi

%postun
if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache %{_ttffontsdir} || :
fi

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license LICENSE.txt
%{_ttffontsdir}

