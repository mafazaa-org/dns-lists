from dns_db.src.block import Block
from dns_db.src._block import *
from re import match
from .utils import with_ending
from pytest import raises


def test_initializing():
    low_list = low["list"].copy() + ["exampleblock.com"]
    high_list = low_list + high["list"]

    block = __init__()

    low_list.sort()
    high_list.sort()

    assert block.to_records("www.google.com") == [
        {
            "host": "www.google.com",
            "type": "A",
            "answer": "0.0.0.0",
        }
    ]

    assert block.to_string("www.google.com") == "google.com"


def test_set():
    block = __init__()
    block.low_regex_contains = block.low_regex_contains.copy()
    block.low_regex_contains.append("porn")

    with raises(
        Exception,
    ) as excep_info:
        block.set()
    assert (
        excep_info.value.args[0]
        == f"dublicate of 'porn' in low regex (contains) \n[{block.group_name}]"
    )

    block.low_regex_contains = low["regex"]["contains"]
    block.low_list = block.low_list.copy()
    block.low_list.append("www.pornhub.com")

    with raises(
        Exception,
    ) as excep_info:
        block.set()
    assert (
        excep_info.value.args[0]
        == f"www.pornhub.com exists in low list while it's already blocked by low.regex \n[{block.group_name}]"
    )


def test_valid_zones():

    for invalid_domain in [[], 3232, ["hello", "world"], ["hello.com"]]:
        block = __init__()
        block.high_list = block.high_list.copy()

        block.high_list.append(invalid_domain)

        with raises(Exception) as excep_info:
            block.valid_zones()

        assert excep_info.type == Exception
        assert (
            excep_info.value.args[0]
            == f"Can't make a zone for the domain {invalid_domain} in high list with data: A    0.0.0.0   \n[{block.group_name}]"
        )


@with_ending
def test_matches(ending: str):
    block = __init__()
    for domain in low_match:
        domain = domain + ending

        assert match(block.low_regex, domain)
        assert match(block.high_regex, domain)

    for domain in high_match:
        domain = domain + ending
        assert match(block.high_regex, domain)


@with_ending
def test_non_matches(ending: str):
    block = __init__()
    for domain in low_no_match:
        domain = domain + ending

        assert match(block.low_regex, domain) == None

    for domain in high_no_match:
        domain = domain + ending

        assert match(block.high_regex, domain) == None

        assert match(block.low_regex, domain) == None


low_match = [
    "www.pornhub.com",
    "ns500242.ns500249.ns500248.ns500270.ns500250.ns500262.ns500250.ns500213.ns500261.ns500245.ns500225.ns500219.sweetchicksclub.com",
    "ns500242.ns500249.ns500248.ns500270.ns500250.ns500262.ns500250.ns500213.ns500261.ns500245.ns500225.ns500219.sweetkisses.com",
    "ns500242.ns500249.ns500248.ns500270.ns500250.ns500262.ns500250.ns500213.ns500261.ns500245.ns500225.ns500219.sweetxladies.com",
    "www.xnxx.com",
    "xnxx.com",
    "pornhub.com",
    "www.sex.com",
    "sex.com",
    "sex.hello.example.com",
    "ass.sex.com",
    "asses.pornhub.com",
    "breast.pornhub.com",
    "www.striphacker.com",
    "ads.google.com",
    "ads.example.com",
    "ad.sex.com",
    "ad.hello.world.com",
    "www.nordvpn.com",
    "secure-vpn.com",
    "wmail-endpoint.com",
    "wmail-blog.com",
    "wmail-chat.com",
    "wmail-cdn.com",
    "wmail-schnellvpn.com",
    "fairu-endpoint.com",
    "fairu-blog.com",
    "fairu-chat.com",
    "fairu-cdn.com",
    "fairu-schnellvpn.com",
    "bideo-endpoint.com",
    "bideo-blog.com",
    "bideo-chat.com",
    "bideo-cdn.com",
    "bideo-schnellvpn.com",
    "privatproxy-endpoint.com",
    "privatproxy-blog.com",
    "privatproxy-chat.com",
    "privatproxy-cdn.com",
    "privatproxy-schnellvpn.com",
    "ahoravideo-endpoint.com",
    "ahoravideo-blog.com",
    "ahoravideo-chat.com",
    "ahoravideo-cdn.com",
    "ahoravideo-schnellvpn.com",
    "wmail-endpoint.xyz",
    "wmail-blog.xyz",
    "wmail-chat.xyz",
    "wmail-cdn.xyz",
    "wmail-schnellvpn.xyz",
    "fairu-endpoint.xyz",
    "fairu-blog.xyz",
    "fairu-chat.xyz",
    "fairu-cdn.xyz",
    "fairu-schnellvpn.xyz",
    "bideo-endpoint.xyz",
    "bideo-blog.xyz",
    "bideo-chat.xyz",
    "bideo-cdn.xyz",
    "bideo-schnellvpn.xyz",
    "privatproxy-endpoint.xyz",
    "privatproxy-blog.xyz",
    "privatproxy-chat.xyz",
    "privatproxy-cdn.xyz",
    "privatproxy-schnellvpn.xyz",
    "ahoravideo-endpoint.xyz",
    "ahoravideo-blog.xyz",
    "ahoravideo-chat.xyz",
    "ahoravideo-cdn.xyz",
    "ahoravideo-schnellvpn.xyz",
]

high_match = [
    "tiktok.com",
    "www.tiktok.com",
    "tiktok-cdn",
    "movies.example.com",
    "movie.example.com",
    "ad.example.com",
    "ads.example.com",
    "egybest.com",
    "cimaclub.hello",
    "spotify.com",
    "login5.spotify.com",
    "hello.cimaclub.watch",
]

low_no_match = [
    "www.google.ad",
    "www.google.movie",
]

high_no_match = []


def __init__() -> Block:
    return Block()
