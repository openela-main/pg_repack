Name:           pg_repack
Version:        1.4.8
Release:        2%{?dist}
Summary:        Reorganize tables in PostgreSQL databases without any locks

License:        BSD
URL:            http://reorg.github.io/%{name}/
Source0:        https://github.com/reorg/%{name}/archive/ver_%{version}.tar.gz

BuildRequires: 	make
BuildRequires:  lz4-devel, libzstd-devel
BuildRequires:  postgresql, gcc, openssl-devel, postgresql-server
BuildRequires:  postgresql-server-devel >= 15
BuildRequires:  readline-devel, zlib-devel, postgresql-static
BuildRequires:  python3-docutils
%{?postgresql_module_requires}

%description
pg_repack is a PostgreSQL extension which lets you remove
bloat from tables and indexes, and optionally
restore the physical order of clustered indexes.
Unlike CLUSTER and VACUUM FULL it works online,
without holding an exclusive lock on the processed tables during processing.
pg_repack is efficient to boot,
with performance comparable to using CLUSTER directly.

Please check the documentation (in the doc directory or online)
for installation and usage instructions.
%prep
%setup -n %{name}-ver_%{version} -q


%build

make %{?_smp_mflags}
cd doc
make


%install
%make_install

%files
%{_bindir}/%{name}
%{_libdir}/pgsql/%{name}.so
%if 0%{?postgresql_server_llvmjit}
%{_libdir}/pgsql/bitcode/%{name}.index.bc
%{_libdir}/pgsql/bitcode/%{name}/pgut/pgut-spi.bc
%{_libdir}/pgsql/bitcode/%{name}/repack.bc
%endif
%{_datadir}/pgsql/extension/%{name}.control
%{_datadir}/pgsql/extension/%{name}--%{version}.sql

%license COPYRIGHT

%doc README.rst
%doc doc/%{name}.html
%doc doc/%{name}.rst
%doc doc/%{name}_jp.html
%doc doc/%{name}_jp.rst
%doc doc/release.html
%doc doc/release.rst


%changelog
* Mon Aug 19 2024 Ales Nezbeda <anezbeda@redhat.com> 1.4.8-2
- Add new build dependencies to fix build with lz4 enabled
- Related: RHEL-47350

* Tue Oct 25 2022 Filip Janus <fjanus@redhat.com> - 1.4.8-1
- Update to version 1.4.8
- Postgresql 15 is supported
- Related: #2128410

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.4.6-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Jun 22 2021 Mohan Boddu <mboddu@redhat.com> - 1.4.6-3
- Rebuilt for RHEL 9 BETA for openssl 3.0
  Related: rhbz#1971065

* Thu Apr 22 2021 Honza Horak <hhorak@redhat.com> - 1.4.6-2
- Build jit based on what postgresql server does
  Related: #1933048

* Thu Jan 28 2021 Patrik Novotný <panovotn@redhat.com> - 1.4.6-1
- Rebase to upstream release 1.4.6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Aug 21 2019 Filip Januš <fjanus@redhat.com> 1.4.5-1
- Initial packaging
