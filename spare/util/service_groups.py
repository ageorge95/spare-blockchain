from __future__ import annotations

from typing import Generator, KeysView

SERVICES_FOR_GROUP = {
    "all": [
        "spare_harvester",
        "spare_timelord_launcher",
        "spare_timelord",
        "spare_farmer",
        "spare_full_node",
        "spare_wallet",
        "spare_data_layer",
        "spare_data_layer_http",
    ],
    # TODO: should this be `data_layer`?
    "data": ["spare_wallet", "spare_data_layer"],
    "data_layer_http": ["spare_data_layer_http"],
    "node": ["spare_full_node"],
    "harvester": ["spare_harvester"],
    "farmer": ["spare_harvester", "spare_farmer", "spare_full_node", "spare_wallet"],
    "farmer-no-wallet": ["spare_harvester", "spare_farmer", "spare_full_node"],
    "farmer-only": ["spare_farmer"],
    "timelord": ["spare_timelord_launcher", "spare_timelord", "spare_full_node"],
    "timelord-only": ["spare_timelord"],
    "timelord-launcher-only": ["spare_timelord_launcher"],
    "wallet": ["spare_wallet"],
    "introducer": ["spare_introducer"],
    "simulator": ["spare_full_node_simulator"],
    "crawler": ["spare_crawler"],
    "seeder": ["spare_crawler", "spare_seeder"],
    "seeder-only": ["spare_seeder"],
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
