%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-servlet-3.0-api
Version:          1.0.1
Release:          6%{dist}
Summary:          Java Servlet 3.0 API
Group:            Development/Libraries
License:          CDDL
Url:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-servlet-api_spec.git
# cd jboss-servlet-api_spec/ && git archive --format=tar --prefix=jboss-servlet-3.0-api/ jboss-servlet-api_3.0_spec-1.0.1.Final | xz > jboss-servlet-3.0-api-1.0.1.Final.tar.xz
Source0:          jboss-servlet-3.0-api-%{namedversion}.tar.xz

BuildRequires:    java-devel
BuildRequires:    jboss-specs-parent
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin

Requires:         jpackage-utils
Requires:         java
BuildArch:        noarch

%description
The Java Servlet 3.0 API classes.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Libraries
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-servlet-3.0-api

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/jboss-servlet-api_3.0_spec-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "javax.servlet:servlet-api"

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE README

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE README

%changelog
* Thu May 9 2013 Ade Lee <alee@redhat.com> 1.0.1-6
- Resolves #961462 - Remove unneeded maven-checkstyle-plugin and 
  maven-eclipse-plugin BR

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> - 1.0.1-3
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Upstream release 1.0.1.Final
- Added mapping to javax.servlet:servlet-api

* Thu Aug 11 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-0.1.20120312gitd4b6f2
- Packaging after license cleanup
- Spec cleanup

* Thu Aug 11 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging
