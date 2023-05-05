from __future__ import annotations

import os
import sys

from setuptools import setup

dependencies = [
    "aiofiles==23.1.0",  # Async IO for files
    "anyio==3.6.2",
    "boto3==1.26.111",  # AWS S3 for DL s3 plugin
    "blspy==1.0.16",  # Signature library
    "chiavdf==1.0.8",  # timelord and vdf verification
    "chiabip158==1.2",  # bip158-style wallet filters
    "chiapos==1.0.11",  # proof of space
    "clvm==0.9.7",
    "clvm_tools==0.4.6",  # Currying, Program.to, other conveniences
    "chia_rs==0.2.7",
    "clvm-tools-rs==0.1.30",  # Rust implementation of clvm_tools' compiler
    "aiohttp==3.8.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==4.0.1",  # Binary data management library
    "colorama==0.4.6",  # Colorizes terminal output
    "colorlog==6.7.0",  # Adds color to logs
    "concurrent-log-handler==0.9.20",  # Concurrently log and rotate logs
    "cryptography==39.0.1",  # Python cryptography library for TLS - keyring conflict
    "filelock==3.9.0",  # For reading and writing config multiprocess and multithread safely  (non-reentrant locks)
    "keyring==23.13.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "PyYAML==6.0",  # Used for config file format
    "setproctitle==1.3.2",  # Gives the spare processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "click==8.1.3",  # For the CLI
    "dnspython==2.3.0",  # Query DNS seeds
    "watchdog==2.2.0",  # Filesystem event watching - watches keyring.yaml
    "dnslib==0.9.23",  # dns lib
    "typing-extensions==4.5.0",  # typing backports like Protocol and TypedDict
    "zstd==1.5.4.0",
    "packaging==23.0",
    "psutil==5.9.4",
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "build",
    "coverage",
    "diff-cover",
    "pre-commit",
    "py3createtorrent",
    "pylint",
    "pytest",
    "pytest-asyncio>=0.18.1",  # require attribute 'fixture'
    "pytest-cov",
    "pytest-monitor; sys_platform == 'linux'",
    "pytest-xdist",
    "twine",
    "isort",
    "flake8",
    "mypy",
    "black==23.3.0",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "pyinstaller==5.8.0",
    "types-aiofiles",
    "types-cryptography",
    "types-pkg_resources",
    "types-pyyaml",
    "types-setuptools",
]

legacy_keyring_dependencies = [
    "keyrings.cryptfile==1.3.9",
]

kwargs = dict(
    name="spare-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@spare.net",
    description="Spare blockchain full node, farmer, timelord, and wallet.",
    url="https://spare.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="spare blockchain node",
    install_requires=dependencies,
    extras_require=dict(
        dev=dev_dependencies,
        upnp=upnp_dependencies,
        legacy_keyring=legacy_keyring_dependencies,
    ),
    packages=[
        "spare",
        "spare.cmds",
        "spare.clvm",
        "spare.consensus",
        "spare.daemon",
        "spare.data_layer",
        "spare.full_node",
        "spare.timelord",
        "spare.farmer",
        "spare.harvester",
        "spare.introducer",
        "spare.plot_sync",
        "spare.plotters",
        "spare.plotting",
        "spare.pools",
        "spare.protocols",
        "spare.rpc",
        "spare.seeder",
        "spare.server",
        "spare.simulator",
        "spare.types.blockchain_format",
        "spare.types",
        "spare.util",
        "spare.wallet",
        "spare.wallet.db_wallet",
        "spare.wallet.puzzles",
        "spare.wallet.cat_wallet",
        "spare.wallet.did_wallet",
        "spare.wallet.nft_wallet",
        "spare.wallet.trading",
        "spare.wallet.util",
        "spare.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "spare = spare.cmds.spare:main",
            "spare_daemon = spare.daemon.server:main",
            "spare_wallet = spare.server.start_wallet:main",
            "spare_full_node = spare.server.start_full_node:main",
            "spare_harvester = spare.server.start_harvester:main",
            "spare_farmer = spare.server.start_farmer:main",
            "spare_introducer = spare.server.start_introducer:main",
            "spare_crawler = spare.seeder.start_crawler:main",
            "spare_seeder = spare.seeder.dns_server:main",
            "spare_timelord = spare.server.start_timelord:main",
            "spare_timelord_launcher = spare.timelord.timelord_launcher:main",
            "spare_full_node_simulator = spare.simulator.start_simulator:main",
            "spare_data_layer = spare.server.start_data_layer:main",
            "spare_data_layer_http = spare.data_layer.data_layer_server:main",
            "spare_data_layer_s3_plugin = spare.data_layer.s3_plugin_service:run_server",
        ]
    },
    package_data={
        "spare": ["pyinstaller.spec"],
        "": ["*.clsp", "*.clsp.hex", "*.clvm", "*.clib", "py.typed"],
        "spare.util": ["initial-*.yaml", "english.txt"],
        "spare.ssl": ["spare_ca.crt", "spare_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    project_urls={
        "Source": "https://github.com/Spare-Network/spare-blockchain/",
        "Changelog": "https://github.com/Spare-Network/spare-blockchain/blob/main/CHANGELOG.md",
    },
)

if "setup_file" in sys.modules:
    # include dev deps in regular deps when run in snyk
    dependencies.extend(dev_dependencies)

if len(os.environ.get("SPARE_SKIP_SETUP", "")) < 1:
    setup(**kwargs)  # type: ignore
