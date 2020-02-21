#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-protobuf-soname21
Version  : 3.10.1
Release  : 61
URL      : https://github.com/protocolbuffers/protobuf/releases/download/v3.10.1/protobuf-all-3.10.1.tar.gz
Source0  : https://github.com/protocolbuffers/protobuf/releases/download/v3.10.1/protobuf-all-3.10.1.tar.gz
Summary  : Google's Data Interchange Format
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: compat-protobuf-soname21-lib = %{version}-%{release}
Requires: compat-protobuf-soname21-license = %{version}-%{release}
Requires: setuptools
Requires: six
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : emacs
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : zlib-dev
Patch1: 0001-Add-gmock-gtest-at-1.7.0.patch
Patch2: 0002-Ensure-everything-can-build-in-tree.patch
Patch3: 0003-Add-gtest-symlink-to-account-for-the-rest-of-the-bro.patch

%description
This is the 'v2' C++ implementation for python proto2.
It is active when:
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSION=2

%package lib
Summary: lib components for the compat-protobuf-soname21 package.
Group: Libraries
Requires: compat-protobuf-soname21-license = %{version}-%{release}

%description lib
lib components for the compat-protobuf-soname21 package.


%package license
Summary: license components for the compat-protobuf-soname21 package.
Group: Default

%description license
license components for the compat-protobuf-soname21 package.


%prep
%setup -q -n protobuf-3.10.1
cd %{_builddir}/protobuf-3.10.1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582310044
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1582310044
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-protobuf-soname21
cp %{_builddir}/protobuf-3.10.1/LICENSE %{buildroot}/usr/share/package-licenses/compat-protobuf-soname21/1b5a14d06dd784e88dadc5c68344be2dc13875b6
cp %{_builddir}/protobuf-3.10.1/third_party/googletest/googlemock/LICENSE %{buildroot}/usr/share/package-licenses/compat-protobuf-soname21/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/protobuf-3.10.1/third_party/googletest/googlemock/scripts/generator/LICENSE %{buildroot}/usr/share/package-licenses/compat-protobuf-soname21/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
cp %{_builddir}/protobuf-3.10.1/third_party/googletest/googletest/LICENSE %{buildroot}/usr/share/package-licenses/compat-protobuf-soname21/5a2314153eadadc69258a9429104cd11804ea304
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/bin/protoc
rm -f %{buildroot}/usr/include/google/protobuf/any.h
rm -f %{buildroot}/usr/include/google/protobuf/any.pb.h
rm -f %{buildroot}/usr/include/google/protobuf/any.proto
rm -f %{buildroot}/usr/include/google/protobuf/api.pb.h
rm -f %{buildroot}/usr/include/google/protobuf/api.proto
rm -f %{buildroot}/usr/include/google/protobuf/arena.h
rm -f %{buildroot}/usr/include/google/protobuf/arena_impl.h
rm -f %{buildroot}/usr/include/google/protobuf/arenastring.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/code_generator.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/command_line_interface.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/cpp/cpp_generator.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/csharp/csharp_generator.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/csharp/csharp_names.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/importer.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/java/java_generator.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/java/java_names.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/js/js_generator.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/js/well_known_types_embed.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/objectivec/objectivec_generator.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/objectivec/objectivec_helpers.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/parser.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/php/php_generator.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/plugin.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/plugin.pb.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/plugin.proto
rm -f %{buildroot}/usr/include/google/protobuf/compiler/python/python_generator.h
rm -f %{buildroot}/usr/include/google/protobuf/compiler/ruby/ruby_generator.h
rm -f %{buildroot}/usr/include/google/protobuf/descriptor.h
rm -f %{buildroot}/usr/include/google/protobuf/descriptor.pb.h
rm -f %{buildroot}/usr/include/google/protobuf/descriptor.proto
rm -f %{buildroot}/usr/include/google/protobuf/descriptor_database.h
rm -f %{buildroot}/usr/include/google/protobuf/duration.pb.h
rm -f %{buildroot}/usr/include/google/protobuf/duration.proto
rm -f %{buildroot}/usr/include/google/protobuf/dynamic_message.h
rm -f %{buildroot}/usr/include/google/protobuf/empty.pb.h
rm -f %{buildroot}/usr/include/google/protobuf/empty.proto
rm -f %{buildroot}/usr/include/google/protobuf/extension_set.h
rm -f %{buildroot}/usr/include/google/protobuf/extension_set_inl.h
rm -f %{buildroot}/usr/include/google/protobuf/field_mask.pb.h
rm -f %{buildroot}/usr/include/google/protobuf/field_mask.proto
rm -f %{buildroot}/usr/include/google/protobuf/generated_enum_reflection.h
rm -f %{buildroot}/usr/include/google/protobuf/generated_enum_util.h
rm -f %{buildroot}/usr/include/google/protobuf/generated_message_reflection.h
rm -f %{buildroot}/usr/include/google/protobuf/generated_message_table_driven.h
rm -f %{buildroot}/usr/include/google/protobuf/generated_message_util.h
rm -f %{buildroot}/usr/include/google/protobuf/has_bits.h
rm -f %{buildroot}/usr/include/google/protobuf/implicit_weak_message.h
rm -f %{buildroot}/usr/include/google/protobuf/inlined_string_field.h
rm -f %{buildroot}/usr/include/google/protobuf/io/coded_stream.h
rm -f %{buildroot}/usr/include/google/protobuf/io/gzip_stream.h
rm -f %{buildroot}/usr/include/google/protobuf/io/io_win32.h
rm -f %{buildroot}/usr/include/google/protobuf/io/printer.h
rm -f %{buildroot}/usr/include/google/protobuf/io/strtod.h
rm -f %{buildroot}/usr/include/google/protobuf/io/tokenizer.h
rm -f %{buildroot}/usr/include/google/protobuf/io/zero_copy_stream.h
rm -f %{buildroot}/usr/include/google/protobuf/io/zero_copy_stream_impl.h
rm -f %{buildroot}/usr/include/google/protobuf/io/zero_copy_stream_impl_lite.h
rm -f %{buildroot}/usr/include/google/protobuf/map.h
rm -f %{buildroot}/usr/include/google/protobuf/map_entry.h
rm -f %{buildroot}/usr/include/google/protobuf/map_entry_lite.h
rm -f %{buildroot}/usr/include/google/protobuf/map_field.h
rm -f %{buildroot}/usr/include/google/protobuf/map_field_inl.h
rm -f %{buildroot}/usr/include/google/protobuf/map_field_lite.h
rm -f %{buildroot}/usr/include/google/protobuf/map_type_handler.h
rm -f %{buildroot}/usr/include/google/protobuf/message.h
rm -f %{buildroot}/usr/include/google/protobuf/message_lite.h
rm -f %{buildroot}/usr/include/google/protobuf/metadata.h
rm -f %{buildroot}/usr/include/google/protobuf/metadata_lite.h
rm -f %{buildroot}/usr/include/google/protobuf/parse_context.h
rm -f %{buildroot}/usr/include/google/protobuf/port.h
rm -f %{buildroot}/usr/include/google/protobuf/port_def.inc
rm -f %{buildroot}/usr/include/google/protobuf/port_undef.inc
rm -f %{buildroot}/usr/include/google/protobuf/reflection.h
rm -f %{buildroot}/usr/include/google/protobuf/reflection_ops.h
rm -f %{buildroot}/usr/include/google/protobuf/repeated_field.h
rm -f %{buildroot}/usr/include/google/protobuf/service.h
rm -f %{buildroot}/usr/include/google/protobuf/source_context.pb.h
rm -f %{buildroot}/usr/include/google/protobuf/source_context.proto
rm -f %{buildroot}/usr/include/google/protobuf/struct.pb.h
rm -f %{buildroot}/usr/include/google/protobuf/struct.proto
rm -f %{buildroot}/usr/include/google/protobuf/stubs/bytestream.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/callback.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/casts.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/common.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/fastmem.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/hash.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/logging.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/macros.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/map_util.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/mutex.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/once.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/platform_macros.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/port.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/status.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/stl_util.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/stringpiece.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/strutil.h
rm -f %{buildroot}/usr/include/google/protobuf/stubs/template_util.h
rm -f %{buildroot}/usr/include/google/protobuf/text_format.h
rm -f %{buildroot}/usr/include/google/protobuf/timestamp.pb.h
rm -f %{buildroot}/usr/include/google/protobuf/timestamp.proto
rm -f %{buildroot}/usr/include/google/protobuf/type.pb.h
rm -f %{buildroot}/usr/include/google/protobuf/type.proto
rm -f %{buildroot}/usr/include/google/protobuf/unknown_field_set.h
rm -f %{buildroot}/usr/include/google/protobuf/util/delimited_message_util.h
rm -f %{buildroot}/usr/include/google/protobuf/util/field_comparator.h
rm -f %{buildroot}/usr/include/google/protobuf/util/field_mask_util.h
rm -f %{buildroot}/usr/include/google/protobuf/util/json_util.h
rm -f %{buildroot}/usr/include/google/protobuf/util/message_differencer.h
rm -f %{buildroot}/usr/include/google/protobuf/util/time_util.h
rm -f %{buildroot}/usr/include/google/protobuf/util/type_resolver.h
rm -f %{buildroot}/usr/include/google/protobuf/util/type_resolver_util.h
rm -f %{buildroot}/usr/include/google/protobuf/wire_format.h
rm -f %{buildroot}/usr/include/google/protobuf/wire_format_lite.h
rm -f %{buildroot}/usr/include/google/protobuf/wrappers.pb.h
rm -f %{buildroot}/usr/include/google/protobuf/wrappers.proto
rm -f %{buildroot}/usr/lib64/libprotobuf-lite.so
rm -f %{buildroot}/usr/lib64/libprotobuf.so
rm -f %{buildroot}/usr/lib64/libprotoc.so
rm -f %{buildroot}/usr/lib64/pkgconfig/protobuf-lite.pc
rm -f %{buildroot}/usr/lib64/pkgconfig/protobuf.pc
## install_append content
pushd python
python ./setup.py install --root=%{buildroot} --cpp_implementation
python3 ./setup.py install --root=%{buildroot} --cpp_implementation
popd
rm -fr %{buildroot}/usr/lib/python3.8/site-packages/google
rm -fr %{buildroot}/usr/lib/python3.8/site-packages/protobuf*
## install_append end

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libprotobuf-lite.so.21
/usr/lib64/libprotobuf-lite.so.21.0.1
/usr/lib64/libprotobuf.so.21
/usr/lib64/libprotobuf.so.21.0.1
/usr/lib64/libprotoc.so.21
/usr/lib64/libprotoc.so.21.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-protobuf-soname21/1b5a14d06dd784e88dadc5c68344be2dc13875b6
/usr/share/package-licenses/compat-protobuf-soname21/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
/usr/share/package-licenses/compat-protobuf-soname21/5a2314153eadadc69258a9429104cd11804ea304
