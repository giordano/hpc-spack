# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Aria2(AutotoolsPackage):
    """An ultra fast download utility"""

    homepage = "https://aria2.github.io"
    url = "https://github.com/aria2/aria2/releases/download/release-1.36.0/aria2-1.36.0.tar.gz"

    license("GPL-2.0-or-later")

    version("1.37.0", sha256="8e7021c6d5e8f8240c9cc19482e0c8589540836747744724d86bf8af5a21f0e8")
    version("1.36.0", sha256="b593b2fd382489909c96c62c6e180054c3332b950be3d73e0cb0d21ea8afb3c5")
    version("1.35.0", sha256="fd85589416f8246cefc4e6ba2fa52da54fdf11fd5602a2db4b6749f7c33b5b2d")
    version("1.34.0", sha256="ec4866985760b506aa36dc9021dbdc69551c1a647823cae328c30a4f3affaa6c")

    variant("bittorrent", default=True, description="Enable bittorrent support")
    variant("metalink", default=True, description="Enable Metalink support")
    variant(
        "tls",
        values=disjoint_sets(
            ("auto",), ("gnutls", "openssl", "appletls", "wintls")
        ).with_non_feature_values("auto"),
        description="List of TLS suppliers for which support is enabled; "
        "'auto' lets aria determine. Chooses OS support on OSX and Win, chooses GnuTLS over OpenSSL",
    )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("libxml2")
    depends_on("libssh2")
    depends_on("libgcrypt")
    depends_on("zlib-api")
    depends_on("c-ares")
    depends_on("sqlite")
    depends_on("gnutls", when="tls=gnutls")
    depends_on("openssl", when="tls=openssl")

    def configure_args(self):
        spec = self.spec
        config_args = []

        if spec.satisfies("tls=gnutls"):
            config_args.append(["--with-tls", "--without-openssl", "--without-appletls", "--without-wintls"])
        elif spec.satisfies("tls=openssl"):
            config_args.append(["--with-openssl", "--without-gnutls", "--without-appletls", "--without-wintls"])
        elif spec.satisfies("tls=appletls"):
            config_args.append(["--with-appletls", "--without-gnutls", "--without-openssl", "--without-wintls"])
        elif spec.satisfies("tls=wintls"):
            config_args.append(["--with-wintls", "--without-gnutls", "--without-openssl", "--without-appletls"])

        if spec.satisfies("~bittorrent"):
            config_args.append("--disable-bittorrent")
        if spec.satisfies("~metalink"):
            config_args.append("--disable-metalink")

        return config_args

