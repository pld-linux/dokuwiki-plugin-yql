%define		plugin	yql
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	A plugin for embedding results of the Yahoo! YQL query API in a page
Name:		dokuwiki-plugin-%{plugin}
Version:	20110703
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://github.com/Michitux/dokuwiki-plugin-yql/tarball/master#/%{plugin}.tgz
# Source0-md5:	b409b0a93659d7b0c36efd6e8cd0a312
URL:		http://www.dokuwiki.org/plugin:yql
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20090214
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin allows to embed results from the YQL (Yahoo! Query
Language) API of Yahoo! in a wiki page. The plugin only works for
certain queries and certain query fields and has mainly been created
because I needed to embed a certain query result. The plugin does not
support queries that need authorization or return one single result
(and not a list of results). It is recommended that you try out your
query in the YQL Console in order to find the necessary parameters for
the plugin.

%prep
%setup -qc
mv *-%{plugin}-*/* .

version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/example_usage.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.txt
