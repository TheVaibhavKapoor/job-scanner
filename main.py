from __future__ import annotations

# === job_reference_urls.py (inlined) ===

import json
import re
from pathlib import Path
from typing import Dict, List
from urllib.parse import urlparse


APP_ROOT = Path(__file__).resolve().parent
AWESOME_CAREER_PAGES_PATH = APP_ROOT / ".tmp" / "vendor" / "awesome-career-pages" / "Portal.json"

REFERENCE_URL_GROUPS = [
    {
        "id": "indian_it_services",
        "label": "Indian IT & Services",
        "urls": [
            "https://www.tcs.com/careers",
            "https://careers.infosys.com/",
            "https://careers.wipro.com/",
            "https://careers.hcltech.com/",
            "https://careers.techmahindra.com/",
            "https://www.cognizant.com/careers",
            "https://www.capgemini.com/in-en/careers/",
            "https://www.oracle.com/corporate/careers/india/",
            "https://www.ibm.com/employment/in-en/",
        ],
    },
    {
        "id": "banking_finance",
        "label": "Banking & Finance",
        "urls": [
            "https://www.hdfc.bank.in/careers",
            "https://www.icicibank.com/careers",
            "https://www.kotak.com/en/careers.html",
            "https://www.axisbank.com/careers",
            "https://www.sbi.co.in/web/careers",
            "https://www.yesbank.in/career",
            "https://www.bajajfinserv.in/careers",
            "https://www.phonepe.com/careers/",
            "https://jobs.phonepe.com/",
            "https://careers.paytm.com/",
            "https://careers.zerodha.com/",
            "https://groww.in/careers",
            "https://jobs.payu.com/",
            "https://jobs.bharatpe.com/",
            "https://jobs.sliceit.com/",
            "https://jobs.khatabook.com/",
            "https://jobs.rblbank.com/",
            "https://jobs.idfcfirstbank.com/",
            "https://jobs.indusind.com/",
            "https://jobs.bandhanbank.com/",
        ],
    },
    {
        "id": "consumer_retail_telecom",
        "label": "Consumer, Retail & Telecom",
        "urls": [
            "https://www.amazon.jobs/",
            "https://www.flipkartcareers.com/",
            "https://careers.ril.com/",
            "https://careers.myntra.com/",
            "https://www.hul.co.in/careers/",
            "https://www.nestle.in/jobs",
            "https://www.itcportal.com/careers/",
            "https://www.britannia.co.in/careers",
            "https://www.dabur.com/careers",
            "https://www.marico.com/careers",
            "https://jobs.airtel.com/",
            "https://jobs.jio.com/",
            "https://jobs.vodafoneidea.com/",
            "https://jobs.tatadigital.com/",
            "https://jobs.tatacliq.com/",
            "https://jobs.relianceretail.com/",
            "https://jobs.lenskart.com/",
            "https://jobs.boat-lifestyle.com/",
            "https://jobs.delhivery.com/",
            "https://jobs.nykaa.com/",
            "https://jobs.bigbasket.com/",
        ],
    },
    {
        "id": "industrial_pharma_core",
        "label": "Industrial, Pharma & Core",
        "urls": [
            "https://careers.tatamotors.com/",
            "https://www.tatasteel.com/careers/",
            "https://www.larsentoubro.com/careers/",
            "https://www.mahindra.com/careers",
            "https://careers.adanigroup.com/",
            "https://www.sunpharma.com/careers",
            "https://www.cipla.com/careers",
            "https://www.drreddys.com/careers/",
            "https://www.ongcindia.com/wps/wcm/connect/en/careers/",
            "https://iocl.com/careers",
            "https://www.ntpc.co.in/careers",
            "https://jobs.moglix.com/",
            "https://jobs.indiamart.com/",
            "https://jobs.apollotyres.com/",
            "https://jobs.heromotocorp.com/",
            "https://jobs.bosch.in/",
        ],
    },
    {
        "id": "startup_saas_internet",
        "label": "Startups, SaaS & Internet",
        "urls": [
            "https://razorpay.com/careers/",
            "https://www.zomato.com/careers",
            "https://jobs.zomato.com/",
            "https://careers.swiggy.com/",
            "https://jobs.swiggy.com/",
            "https://www.freshworks.com/careers/",
            "https://www.byjus.com/careers/",
            "https://unacademy.com/careers",
            "https://jobs.zoho.com/",
            "https://jobs.cred.club/",
            "https://jobs.browserstack.com/",
            "https://careers.postman.com/",
            "https://jobs.dream11.com/",
            "https://careers.meesho.com/",
            "https://jobs.sharechat.com/",
            "https://jobs.ola.com/",
            "https://jobs.cars24.com/",
            "https://jobs.spinny.com/",
            "https://jobs.uplers.com/",
            "https://jobs.upgrad.com/",
            "https://jobs.physicswallah.com/",
            "https://jobs.inmobi.com/",
            "https://jobs.media.net/",
        ],
    },
    {
        "id": "global_tech_consulting",
        "label": "Global Tech & Consulting",
        "urls": [
            "https://www.adobe.com/careers.html",
            "https://careers.google.com/locations/india/",
            "https://careers.microsoft.com/us/en/locations/india",
            "https://www.salesforce.com/company/careers/",
            "https://www2.deloitte.com/in/en/careers.html",
            "https://www.pwc.in/careers.html",
            "https://www.ey.com/en_in/careers",
            "https://home.kpmg/in/en/home/careers.html",
            "https://www.mckinsey.com/careers",
        ],
    },
    {
        "id": "job_boards_aggregators",
        "label": "Job Boards & Aggregators",
        "urls": [
            "https://www.naukri.com/",
            "https://www.linkedin.com/jobs/",
            "https://www.indeed.co.in/",
            "https://in.indeed.com/",
            "https://wellfound.com/",
            "https://wellfound.com/jobs",
            "https://www.foundit.in/",
            "https://www.timesjobs.com/",
            "https://www.shine.com/",
            "https://www.glassdoor.co.in/Jobs/",
            "https://instahyre.com/",
            "https://cutshort.io/jobs",
            "https://hirist.com/",
            "https://www.updazz.com/",
            "https://www.iimjobs.com/",
            "https://www.freshersworld.com/",
            "https://apna.co/jobs",
            "https://www.workindia.in/jobs",
            "https://www.quikr.com/jobs",
            "https://www.clickindia.com/jobs",
            "https://placementindia.com/jobs",
            "https://www.jobgrin.co.in/",
            "https://www.simplyhired.com/",
            "https://www.whatjobs.com/",
            "https://www.jobrapido.com/",
            "https://www.trovit.com/jobs",
            "https://www.jora.com/",
            "https://www.careerjet.co.in/",
            "https://www.adzuna.in/",
            "https://www.jobisjob.co.in/",
        ],
    },
    {
        "id": "ats_platforms",
        "label": "ATS Platforms",
        "urls": [
            "https://jobs.lever.co/",
            "https://hire.lever.co/",
            "https://boards.greenhouse.io/",
            "https://jobs.smartrecruiters.com/",
            "https://myworkdayjobs.com/",
            "https://careers.pageuppeople.com/",
            "https://jobs.jobvite.com/",
            "https://apply.workable.com/",
            "https://jobs.ashbyhq.com/",
            "https://jobs.gohire.io/",
        ],
    },
]


REFERENCE_URL_PACKS = {
    "companies": [
        "indian_it_services",
        "banking_finance",
        "consumer_retail_telecom",
        "industrial_pharma_core",
        "startup_saas_internet",
        "global_tech_consulting",
    ],
    "job_boards": [
        "job_boards_aggregators",
        "ats_platforms",
    ],
    "all": [group["id"] for group in REFERENCE_URL_GROUPS],
}


def _unique_urls(urls: List[str]) -> List[str]:
    items: List[str] = []
    seen = set()
    for url in urls:
        value = _normalize_reference_url(url)
        if not value:
            continue
        if value in seen:
            continue
        seen.add(value)
        items.append(value)
    return items


def _normalize_reference_url(url: str) -> str:
    value = str(url or "").strip()
    if not value:
        return ""
    if value.startswith("//"):
        value = "https:" + value
    elif not re.match(r"^[a-z][a-z0-9+.-]*://", value, flags=re.I):
        value = "https://" + value.lstrip("/")
    return value


def _normalize_company_name(value: str) -> str:
    text = str(value or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _load_awesome_career_pages() -> List[Dict[str, str]]:
    if not AWESOME_CAREER_PAGES_PATH.exists():
        return []
    try:
        payload = json.loads(AWESOME_CAREER_PAGES_PATH.read_text(encoding="utf-8"))
    except Exception:
        return []
    entries: List[Dict[str, str]] = []
    for item in payload if isinstance(payload, list) else []:
        if not isinstance(item, dict):
            continue
        title = str(item.get("Title") or "").strip()
        url = _normalize_reference_url(item.get("Link"))
        if not title or not url:
            continue
        entries.append({"title": title, "url": url})
    return entries


def _summarize_hosts(urls: List[str], max_hosts: int = 3) -> str:
    hosts: List[str] = []
    seen = set()
    for url in urls:
        host = urlparse(url).netloc.lower().removeprefix("www.")
        if not host or host in seen:
            continue
        seen.add(host)
        hosts.append(host)
    if not hosts:
        return ""
    if len(hosts) <= max_hosts:
        return ", ".join(hosts)
    return f"{', '.join(hosts[:max_hosts])} +{len(hosts) - max_hosts} more"


def get_reference_url_groups() -> List[Dict[str, object]]:
    groups: List[Dict[str, object]] = []
    for group in REFERENCE_URL_GROUPS:
        urls = _unique_urls(group["urls"])
        groups.append(
            {
                "id": group["id"],
                "label": group["label"],
                "count": len(urls),
                "urls": urls,
                "text": "\n".join(urls),
                "preview": _summarize_hosts(urls),
            }
        )
    return groups


def get_all_reference_urls() -> List[str]:
    groups = {group["id"]: group for group in get_reference_url_groups()}
    urls: List[str] = []
    for group_id in REFERENCE_URL_PACKS["all"]:
        urls.extend(groups.get(group_id, {}).get("urls", []))
    return _unique_urls(urls)


def get_reference_scan_catalog() -> Dict[str, object]:
    groups = get_reference_url_groups()
    all_urls = get_all_reference_urls()
    awesome_entries = _load_awesome_career_pages()
    return {
        "total_urls": len(all_urls),
        "group_count": len(groups),
        "groups": groups,
        "host_preview": _summarize_hosts(all_urls, max_hosts=6),
        "awesome_company_count": len(awesome_entries),
    }


def discover_reference_urls_for_companies(companies) -> List[str]:
    targets = [_normalize_company_name(company) for company in companies or [] if _normalize_company_name(company)]
    if not targets:
        return []

    matched_urls: List[str] = []
    for entry in _load_awesome_career_pages():
        title_key = _normalize_company_name(entry["title"])
        if not title_key:
            continue
        for target in targets:
            if target == title_key or target in title_key or title_key in target:
                matched_urls.append(entry["url"])
                break
    return _unique_urls(matched_urls)


def get_reference_url_packs() -> Dict[str, Dict[str, object]]:
    groups = {group["id"]: group for group in get_reference_url_groups()}
    packs: Dict[str, Dict[str, object]] = {}
    for group_id, group in groups.items():
        packs[group_id] = {
            "count": group["count"],
            "text": group["text"],
        }
    for pack_id, group_ids in REFERENCE_URL_PACKS.items():
        urls: List[str] = []
        for group_id in group_ids:
            urls.extend(groups.get(group_id, {}).get("urls", []))
        unique_urls = _unique_urls(urls)
        packs[pack_id] = {
            "count": len(unique_urls),
            "text": "\n".join(unique_urls),
        }
    return packs

# === universal_job_scanner.py (inlined) ===

import html
import json
import os
import re
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from selenium.common.exceptions import TimeoutException

try:
    from jobspy import scrape_jobs as _jobspy_scrape_jobs
except Exception:
    _jobspy_scrape_jobs = None

STANDARD_COLUMNS = [
    "Company",
    "Platform",
    "Role",
    "Location",
    "Date",
    "Primary Apply Link",
    "Apply Links",
    "Job Description",
    "Post Text",
    "Post Link",
    "Author Name",
    "Emails",
    "Phone Numbers",
    "All Links",
]

DEFAULT_TIMEOUT = 20
DEFAULT_MAX_PAGES = 1
DEFAULT_LIMIT_PER_SOURCE = 5
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
)
DEFAULT_SELENIUM_PAGE_WAIT = 5
DEFAULT_SELENIUM_FALLBACK_LIMIT = 3

DEFAULT_SOURCE_NAMES = [
    "indeed",
    "naukri",
    "greenhouse",
    "lever",
    "smartrecruiters",
    "ashby",
    "workday",
    "workable",
    "icims",
    "generic",
]

CAREER_SOURCE_NAMES = {"greenhouse", "lever", "smartrecruiters", "ashby", "workday", "workable", "icims", "generic"}
JOBSPY_SOURCE_NAMES = set()
NAUKRI_DEFAULT_CLIENT_ID = "d3skt0p"
NAUKRI_DEFAULT_GID = "LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE"
DEFAULT_INPUT_SELENIUM_BUDGET = 10


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _emit(status_cb: Optional[Callable[[str], None]], message: str) -> None:
    if callable(status_cb):
        try:
            status_cb(message)
        except Exception:
            pass


def _emit_url_progress(status_cb: Optional[Callable[[str], None]], source: str, index: int, total: int, url: str, progress_state: Optional[Dict[str, int]] = None) -> None:
    if isinstance(progress_state, dict) and int(progress_state.get("total") or 0) > 0:
        progress_state["count"] = int(progress_state.get("count") or 0) + 1
        index = progress_state["count"]
        total = int(progress_state.get("total") or total or 0)
    cleaned_url = _clean_text(url)
    parsed = urllib.parse.urlparse(cleaned_url)
    label = parsed.netloc or cleaned_url
    if parsed.path and parsed.path != "/":
        label = f"{label}{parsed.path}"
    label = label[:120]
    payload = {
        "source": _clean_text(source),
        "index": int(index or 0),
        "total": int(total or 0),
        "url": cleaned_url,
        "label": label,
    }
    _emit(status_cb, "URL_PROGRESS::" + json.dumps(payload, ensure_ascii=True))


def _limit_rows(rows: List[Dict[str, str]], limit_per_source: int, enforce_result_limit: bool = True) -> List[Dict[str, str]]:
    if not enforce_result_limit or limit_per_source <= 0:
        return rows
    return rows[:limit_per_source]


def _clean_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, float) and pd.isna(value):
        return ""
    text = html.unescape(str(value))
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _unique(seq: Iterable[str]) -> List[str]:
    out: List[str] = []
    seen = set()
    for item in seq:
        text = _clean_text(item)
        if not text:
            continue
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(text)
    return out


def _slugify(value: str) -> str:
    text = _clean_text(value).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def _normalize_url(url: str, base_url: str = "") -> str:
    url = _clean_text(url)
    if not url:
        return ""
    if url.startswith("//"):
        return "https:" + url
    if base_url:
        return urllib.parse.urljoin(base_url, url)
    return url


def _url_with_query(url: str, params: Dict[str, str], path: str = "", fragment: Optional[str] = None) -> str:
    parsed = urllib.parse.urlparse(_clean_text(url))
    current = dict(urllib.parse.parse_qsl(parsed.query, keep_blank_values=True))
    for key, value in params.items():
        if value is None:
            continue
        current[str(key)] = str(value)
    new_query = urllib.parse.urlencode(current, doseq=True)
    new_path = path or parsed.path
    new_fragment = parsed.fragment if fragment is None else fragment
    return urllib.parse.urlunparse(parsed._replace(path=new_path, query=new_query, fragment=new_fragment))


def _search_terms(query: str = "", keywords=None, max_terms: int = 2) -> List[str]:
    values = []
    for value in [query] + _split_text_list(keywords):
        text = _clean_text(value)
        if text and text.lower() not in {item.lower() for item in values}:
            values.append(text)
        if len(values) >= max_terms:
            break
    return values


def _search_locations(locations, max_locations: int = 3) -> List[str]:
    values = []
    for value in _split_text_list(locations):
        text = _clean_text(value)
        if text and text.lower() not in {item.lower() for item in values}:
            values.append(text)
        if len(values) >= max_locations:
            break
    return values


def _country_code_for_location(location: str) -> str:
    normalized = _clean_text(location).lower()
    if normalized == "india":
        return "IN"
    return ""


def _search_url_variants(url: str, query: str = "", keywords=None, locations=None, platform_hint: str = "", max_pages: int = DEFAULT_MAX_PAGES) -> List[str]:
    base_url = _normalize_url(url)
    if not base_url:
        return []
    parsed = urllib.parse.urlparse(base_url)
    host = parsed.netloc.lower()
    path = parsed.path or "/"
    roles = _search_terms(query=query, keywords=keywords, max_terms=2)
    places = _search_locations(locations, max_locations=3)
    variants = [base_url]

    if "indeed." in host or platform_hint == "indeed":
        terms = roles or [""]
        locs = places or [""]
        for term in terms[:1]:
            for location in locs[:3]:
                for page in range(max_pages):
                    variants.append(
                        _url_with_query(
                            f"{parsed.scheme or 'https'}://{host}/jobs",
                            {"q": term, "l": location, "start": str(page * 10)},
                        )
                    )
        return _unique(variants)

    if "naukri.com" in host or platform_hint == "naukri":
        terms = roles or [""]
        locs = places or [""]
        for term in terms[:1]:
            for location in locs[:3]:
                for page in range(max_pages):
                    variants.append(
                        _url_with_query(
                            f"{parsed.scheme or 'https'}://{host}/job-listings",
                            {"keyword": term, "location": location, "pageNo": str(page + 1)},
                        )
                    )
        return _unique(variants)

    if "linkedin.com" in host and "/jobs" in path:
        for term in roles[:1] or [""]:
            for location in places[:3] or [""]:
                variants.append(
                    _url_with_query(
                        f"{parsed.scheme or 'https'}://{host}/jobs/search/",
                        {"keywords": term, "location": location},
                    )
                )

    if "careers.cognizant.com" in host:
        for term in roles[:1] or [""]:
            for location in places[:3] or ["India"]:
                params = {
                    "keyword": term,
                    "location": location,
                    "radius": "100",
                    "lat": "",
                    "lng": "",
                    "cname": location,
                    "ccode": _country_code_for_location(location),
                    "pagesize": "10",
                }
                variants.append(_url_with_query(base_url, params, fragment="results"))

    generic_param_sets = [
        ("keyword", "location"),
        ("q", "location"),
        ("query", "location"),
    ]
    for term in roles[:1]:
        for location in places[:2] or [""]:
            for role_key, location_key in generic_param_sets:
                params = {role_key: term}
                if location:
                    params[location_key] = location
                variants.append(_url_with_query(base_url, params))

    if roles:
        encoded_role = urllib.parse.quote_plus(roles[0])
        encoded_location = urllib.parse.quote_plus((places[0] if places else "India"))
        variants.append(base_url.replace("Job+Role", encoded_role).replace("Job%20Role", encoded_role).replace("India", encoded_location, 1))

    return _unique(variants)


def _document_base_url(page_url: str, html_text: str) -> str:
    try:
        soup = bs(html_text, "html.parser")
        base_tag = soup.find("base", href=True)
        if base_tag and base_tag.get("href"):
            return _normalize_url(base_tag.get("href"), page_url)
    except Exception:
        pass
    return page_url


def _candidate_search_urls(url: str, query: str = "", keywords=None, locations=None) -> List[str]:
    parsed = urllib.parse.urlparse(_normalize_url(url))
    host = parsed.netloc.lower()
    path = parsed.path.rstrip("/")
    roles = _search_terms(query=query, keywords=keywords, max_terms=1)
    places = _search_locations(locations, max_locations=1)
    variants = []
    if "google.com" in host and "/about/careers" in path:
        variants.append("https://www.google.com/about/careers/applications/jobs/results/")
    if "careers.google.com" in host:
        variants.append("https://www.google.com/about/careers/applications/jobs/results/")
    if "microsoft.com" in host:
        variants.append(_url_with_query("https://jobs.careers.microsoft.com/global/en/job-search-results", {"lc": places[0] if places else "India"}))
    if "cognizant.com" in host:
        variants.extend(_search_url_variants("https://careers.cognizant.com/global-en/jobs/", query=query, keywords=keywords, locations=locations, platform_hint="generic"))
    if path in {"", "/careers", "/career", "/jobs"}:
        for extra_path in ["/careers/job-openings/", "/job-openings/", "/jobs/", "/careers/jobs/"]:
            variants.append(urllib.parse.urlunparse(parsed._replace(path=extra_path, query="", fragment="")))
    return _unique([item for item in variants if item and item != url])


def _extract_candidate_job_links(page_url: str, html_text: str, limit: int = 20) -> List[str]:
    soup = bs(html_text, "html.parser")
    base_url = _document_base_url(page_url, html_text)
    page_host = urllib.parse.urlparse(page_url).netloc.lower()
    scored_links = []
    seen = set()
    for anchor in soup.find_all("a", href=True):
        href = _normalize_url(anchor.get("href"), base_url)
        if not href:
            continue
        lowered_href = href.lower()
        target_host = urllib.parse.urlparse(href).netloc.lower()
        if lowered_href.startswith(("mailto:", "javascript:", "tel:")):
            continue
        if any(lowered_href.endswith(ext) for ext in (".pdf", ".doc", ".docx", ".png", ".jpg", ".jpeg", ".gif")):
            continue
        label = _clean_text(anchor.get_text(" "))
        lowered_label = label.lower()
        target_platform = detect_ats_platform_from_url(href)
        is_ats_platform = target_platform in CAREER_SOURCE_NAMES and target_platform != "generic"
        if target_host and page_host and target_host != page_host and not is_ats_platform and target_platform not in {"indeed", "naukri"}:
            continue
        if not any(term in lowered_href or term in lowered_label for term in STRONG_JOB_LINK_TERMS) and not is_ats_platform:
            continue
        score = 0
        if is_ats_platform:
            score += 12
        if _is_probable_job_url(href, label):
            score += 8
        if "current openings" in lowered_label or "job openings" in lowered_label:
            score += 8
        if "job-search-results" in lowered_href or "/jobs/results/" in lowered_href:
            score += 10
        if any(term in lowered_href for term in NON_JOB_LINK_TERMS):
            score -= 12
        key = href.lower()
        if key in seen:
            continue
        seen.add(key)
        if score >= 8:
            scored_links.append((score, href))
    scored_links.sort(key=lambda item: (-item[0], item[1]))
    return [href for _, href in scored_links[:limit]]


def _strip_url_artifacts(raw_url: str) -> str:
    cleaned = _clean_text(raw_url)
    if not cleaned:
        return ""
    for token in ['"', "'", ">", "<", "%22", "%23", "&sa=", "&ved=", "&utm", "#", ":~:"]:
        if token in cleaned:
            cleaned = cleaned.split(token, 1)[0]
    return cleaned.strip()


def _extract_urls_from_text(text: str) -> List[str]:
    if not text:
        return []
    return re.findall(r"https?://[^\s\"'<>]+", text, flags=re.I)


def _decode_slug(slug: str) -> str:
    try:
        return urllib.parse.unquote(slug)
    except Exception:
        return slug


def _sanitize_slug(slug: str) -> str:
    slug = _clean_text(_decode_slug(slug))
    slug = slug.replace('"', "").replace("'", "").replace("<", "").replace(">", "").replace("%", "")
    return slug.strip()


def _extract_greenhouse_slugs(text: str) -> List[str]:
    slugs = set()
    blocked = {
        "about",
        "apply",
        "careers",
        "company",
        "embed",
        "home",
        "job",
        "jobs",
        "positions",
        "requests",
    }
    for raw_url in _extract_urls_from_text(text):
        cleaned = _strip_url_artifacts(raw_url)
        try:
            parsed = urllib.parse.urlparse(cleaned)
        except Exception:
            continue
        if parsed.netloc not in {"boards.greenhouse.io", "job-boards.greenhouse.io"}:
            continue
        if parsed.netloc == "job-boards.greenhouse.io":
            for_param = urllib.parse.parse_qs(parsed.query).get("for")
            if for_param:
                slugs.add(for_param[0].lower())
            continue
        parts = [part for part in parsed.path.split("/") if part]
        if not parts:
            continue
        if parts[0] == "embed":
            for_param = urllib.parse.parse_qs(parsed.query).get("for")
            if for_param:
                slugs.add(for_param[0].lower())
            continue
        slugs.add(parts[0].lower())

    for match in re.findall(r"boards\.greenhouse\.io\s*[^a-z0-9]+([a-z0-9_-]+)", text or "", flags=re.I):
        slugs.add(match.lower())
    for match in re.findall(r"job_app\?[^\\s]*for=([a-z0-9_-]+)", text or "", flags=re.I):
        slugs.add(match.lower())

    cleaned_slugs = []
    for slug in slugs:
        slug = _sanitize_slug(slug)
        if not slug or slug in blocked:
            continue
        if not re.match(r"^[a-z0-9_-]+$", slug):
            continue
        cleaned_slugs.append(slug)
    return _unique(cleaned_slugs)


def _extract_lever_slugs(text: str) -> List[str]:
    slugs = set()
    normalized = text.replace("&amp;", "&") if text else ""
    for raw_url in _extract_urls_from_text(normalized):
        cleaned = _strip_url_artifacts(raw_url)
        try:
            parsed = urllib.parse.urlparse(cleaned)
        except Exception:
            continue
        if parsed.netloc != "jobs.lever.co":
            continue
        parts = [part for part in parsed.path.split("/") if part]
        if parts:
            slugs.add(parts[0].lower())
    for match in re.findall(r"jobs\.lever\.co\s*[^a-z0-9]+([a-z0-9_-]+)", normalized, flags=re.I):
        slugs.add(match.lower())
    cleaned_slugs = []
    for slug in slugs:
        slug = _sanitize_slug(slug)
        if slug and re.match(r"^[a-z0-9_-]+$", slug):
            cleaned_slugs.append(slug)
    return _unique(cleaned_slugs)


def _extract_ashby_slugs(text: str) -> List[str]:
    slugs = set()
    for raw_url in _extract_urls_from_text(text):
        cleaned = _strip_url_artifacts(raw_url)
        try:
            parsed = urllib.parse.urlparse(cleaned)
        except Exception:
            continue
        if "ashbyhq.com" not in parsed.netloc:
            continue
        parts = [part for part in parsed.path.split("/") if part]
        if not parts:
            continue
        if parsed.netloc == "api.ashbyhq.com":
            if len(parts) >= 3 and parts[0] == "posting-api" and parts[1] == "job-board":
                slugs.add(parts[2].lower())
            continue
        slugs.add(parts[0].lower())

    for match in re.findall(r"jobs\.ashbyhq\.com\s*[^a-z0-9]+([a-z0-9_.-]+)", text or "", flags=re.I):
        slugs.add(match.lower())

    cleaned_slugs = []
    for slug in slugs:
        slug = _sanitize_slug(slug)
        if slug and re.match(r"^[a-z0-9_.-]+$", slug):
            cleaned_slugs.append(slug)
    return _unique(cleaned_slugs)


def _extract_smartrecruiters_slugs(text: str) -> List[str]:
    slugs = set()
    normalized = text.replace("&amp;", "&") if text else ""
    for raw_url in _extract_urls_from_text(normalized):
        cleaned = _strip_url_artifacts(raw_url)
        try:
            parsed = urllib.parse.urlparse(cleaned)
        except Exception:
            continue
        if not parsed.netloc.endswith("smartrecruiters.com"):
            continue
        parts = [part for part in parsed.path.split("/") if part]
        if parts:
            slugs.add(parts[0].lower())
    cleaned_slugs = []
    for slug in slugs:
        slug = _sanitize_slug(slug)
        if slug and re.match(r"^[a-z0-9_-]+$", slug):
            cleaned_slugs.append(slug)
    return _unique(cleaned_slugs)


def _extract_workable_slugs(text: str) -> List[str]:
    slugs = set()
    normalized = text.replace("&amp;", "&") if text else ""
    for raw_url in _extract_urls_from_text(normalized):
        cleaned = _strip_url_artifacts(raw_url)
        try:
            parsed = urllib.parse.urlparse(cleaned)
        except Exception:
            continue
        if parsed.netloc == "apply.workable.com":
            parts = [part for part in parsed.path.split("/") if part]
            if parts and parts[0] not in {"j", "jobs", "careers", "api"}:
                slugs.add(parts[0].lower())
        if parsed.netloc.endswith("jobs.workable.com"):
            parts = [part for part in parsed.path.split("/") if part]
            if len(parts) >= 3 and parts[0] == "company":
                slugs.add(parts[-1].lower())
    cleaned_slugs = []
    for slug in slugs:
        slug = _sanitize_slug(slug)
        if slug and re.match(r"^[a-z0-9_-]+$", slug):
            cleaned_slugs.append(slug)
    return _unique(cleaned_slugs)


def _extract_workday_boards(text: str) -> List[str]:
    normalized = text.replace("&amp;", "&") if text else ""
    url_matches = _extract_urls_from_text(normalized)
    blocked_segments = {"job", "jobs", "details"}
    boards = []
    seen = set()

    for raw_url in url_matches:
        cleaned = _strip_url_artifacts(raw_url)
        try:
            url = urllib.parse.urlparse(cleaned)
        except Exception:
            continue
        if not url.netloc.endswith("myworkdayjobs.com"):
            continue
        host_parts = [part for part in url.netloc.split(".") if part]
        tenant_slug = host_parts[0] if host_parts else ""
        parts = [part for part in url.path.split("/") if part]
        if not parts:
            continue
        site_segment = parts[0]
        locale_segment = ""
        if re.match(r"^[a-z]{2}-[A-Z]{2}$", site_segment) and len(parts) > 1:
            locale_segment = site_segment
            site_segment = parts[1]
        if not site_segment or site_segment.lower() in blocked_segments:
            continue
        board_url = f"{url.scheme}://{url.netloc}/{locale_segment}/{site_segment}" if locale_segment else f"{url.scheme}://{url.netloc}/{site_segment}"
        if board_url not in seen:
            seen.add(board_url)
            boards.append(board_url)
        if tenant_slug and tenant_slug not in seen:
            seen.add(tenant_slug)
    return boards


def _extract_icims_boards(text: str) -> List[str]:
    normalized = text.replace("&amp;", "&") if text else ""
    url_matches = _extract_urls_from_text(normalized)
    boards = []
    seen = set()
    for raw_url in url_matches:
        cleaned = _strip_url_artifacts(raw_url)
        try:
            url = urllib.parse.urlparse(cleaned)
        except Exception:
            continue
        if not url.netloc.endswith("icims.com"):
            continue
        board_url = f"{url.scheme}://{url.netloc}/jobs/search?ss=1"
        if board_url not in seen:
            seen.add(board_url)
            boards.append(board_url)
    return boards


def _extract_taleo_boards(text: str) -> List[str]:
    normalized = text.replace("&amp;", "&") if text else ""
    url_matches = _extract_urls_from_text(normalized)
    boards = []
    seen = set()
    for raw_url in url_matches:
        cleaned = _strip_url_artifacts(raw_url)
        try:
            url = urllib.parse.urlparse(cleaned)
        except Exception:
            continue
        if not url.netloc.endswith("taleo.net"):
            continue
        parts = [part for part in url.path.split("/") if part]
        if len(parts) >= 2 and parts[0] == "careersection":
            section = parts[1]
            if not re.match(r"^[a-zA-Z0-9_-]{1,20}$", section):
                continue
            board_url = f"{url.scheme}://{url.netloc}/careersection/{section}/jobsearch.ftl"
            if board_url not in seen:
                seen.add(board_url)
                boards.append(board_url)
    return boards


def _extract_ats_board_urls_from_text(text: str) -> List[str]:
    urls = []
    for slug in _extract_greenhouse_slugs(text):
        urls.append(f"https://boards.greenhouse.io/{slug}")
    for slug in _extract_lever_slugs(text):
        urls.append(f"https://jobs.lever.co/{slug}")
    for slug in _extract_ashby_slugs(text):
        urls.append(f"https://jobs.ashbyhq.com/{slug}")
    for slug in _extract_smartrecruiters_slugs(text):
        urls.append(f"https://careers.smartrecruiters.com/{slug}")
    for slug in _extract_workable_slugs(text):
        urls.append(f"https://apply.workable.com/{slug}/")
    urls.extend(_extract_workday_boards(text))
    urls.extend(_extract_icims_boards(text))
    urls.extend(_extract_taleo_boards(text))
    return _unique(urls)


def _canonicalize_ats_url(url: str) -> str:
    cleaned = _clean_text(url)
    if not cleaned:
        return ""
    platform = detect_ats_platform_from_url(cleaned)
    try:
        parsed = urllib.parse.urlparse(cleaned)
    except Exception:
        return cleaned
    parts = [part for part in parsed.path.split("/") if part]
    if platform == "greenhouse":
        if parsed.netloc in {"job-boards.greenhouse.io", "boards.greenhouse.io"}:
            if parsed.netloc == "job-boards.greenhouse.io":
                for_param = urllib.parse.parse_qs(parsed.query).get("for")
                if for_param:
                    return f"https://boards.greenhouse.io/{for_param[0]}"
            if parts:
                return f"https://boards.greenhouse.io/{parts[0]}"
        return cleaned
    if platform == "lever":
        if parsed.netloc == "jobs.lever.co" and parts:
            return f"https://jobs.lever.co/{parts[0]}"
        return cleaned
    if platform == "ashby":
        if "ashbyhq.com" in parsed.netloc and parts:
            if parsed.netloc == "api.ashbyhq.com" and len(parts) >= 3 and parts[0] == "posting-api" and parts[1] == "job-board":
                return f"https://jobs.ashbyhq.com/{parts[2]}"
            return f"https://jobs.ashbyhq.com/{parts[0]}"
        return cleaned
    if platform == "smartrecruiters":
        if parsed.netloc.endswith("smartrecruiters.com") and parts:
            return f"https://careers.smartrecruiters.com/{parts[0]}"
        return cleaned
    if platform == "workable":
        if parsed.netloc == "apply.workable.com" and parts:
            return f"https://apply.workable.com/{parts[0]}/"
        return cleaned
    if platform == "workday":
        boards = _extract_workday_boards(cleaned)
        return boards[0] if boards else cleaned
    if platform == "icims":
        boards = _extract_icims_boards(cleaned)
        return boards[0] if boards else cleaned
    if platform == "taleo":
        boards = _extract_taleo_boards(cleaned)
        return boards[0] if boards else cleaned
    return cleaned


def _discover_ats_board_urls_from_html(base_url: str, html_text: str) -> List[str]:
    if not html_text:
        return []
    combined = [base_url]
    combined.extend(_extract_urls_from_text(html_text))
    try:
        soup = bs(html_text, "html.parser")
        for tag in soup.find_all(["a", "link", "script", "iframe"]):
            for attr in ("href", "src", "data-href", "data-src"):
                value = tag.get(attr)
                if value:
                    combined.append(_normalize_url(value, base_url))
    except Exception:
        pass
    text = " ".join([item for item in combined if item]) + " " + html_text
    return _extract_ats_board_urls_from_text(text)


def _ollama_job_scanner_enabled() -> bool:
    flag = _clean_text(os.getenv("OLLAMA_JOB_SCANNER_ENABLED", ""))
    if flag.lower() not in {"1", "true", "yes"}:
        return False
    return bool(_clean_text(os.getenv("OLLAMA_JOB_SCANNER_MODEL", "")) or _clean_text(os.getenv("OLLAMA_MODEL", "")))


def _ollama_job_scanner_model() -> str:
    return _clean_text(os.getenv("OLLAMA_JOB_SCANNER_MODEL")) or _clean_text(os.getenv("OLLAMA_MODEL")) or "qwen2.5:7b-instruct"


def _ollama_generate(prompt: str, temperature: float = 0.1, max_output_tokens: int = 600) -> str:
    if not _ollama_job_scanner_enabled():
        return ""
    model = _ollama_job_scanner_model()
    if not model:
        return ""
    base_url = _clean_text(os.getenv("OLLAMA_BASE_URL", "")).rstrip("/")
    if not base_url:
        return ""
    url = f"{base_url}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature,
            "num_predict": max_output_tokens,
        },
    }
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=90) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        if isinstance(data, dict):
            return str(data.get("response") or "")
    except Exception:
        return ""
    return ""


def _extract_json_block(text: str) -> Optional[Dict[str, object]]:
    if not text:
        return None
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        return None
    try:
        return json.loads(match.group(0))
    except Exception:
        return None


def _ollama_extract_ats_urls(base_url: str, html_text: str) -> List[str]:
    if not _ollama_job_scanner_enabled():
        return []
    max_chars = int(os.getenv("OLLAMA_JOB_SCANNER_MAX_CHARS", "12000") or "12000")
    snippet = html_text[:max_chars]
    prompt = (
        "You are an ATS discovery agent. Extract ATS board URLs from the HTML snippet.\n"
        "Return ONLY JSON in this schema:\n"
        '{"urls":[string]}\n'
        "Rules:\n"
        "- Only include ATS board or job listing URLs for Greenhouse, Lever, Ashby, Workday, SmartRecruiters, Workable, iCIMS, or Taleo.\n"
        "- Normalize to board URLs (not individual job pages).\n"
        "- If none, return {\"urls\": []}.\n\n"
        f"BASE_URL: {base_url}\n"
        f"HTML_SNIPPET:\n{snippet}"
    )
    output = _ollama_generate(prompt)
    payload = _extract_json_block(output)
    if not isinstance(payload, dict):
        return []
    urls = payload.get("urls")
    if not isinstance(urls, list):
        return []
    cleaned = []
    for url in urls:
        text_url = _canonicalize_ats_url(_clean_text(url))
        if not text_url:
            continue
        platform = detect_ats_platform_from_url(text_url)
        if platform in CAREER_SOURCE_NAMES or platform in {"taleo"}:
            cleaned.append(text_url)
    return _unique(cleaned)


def _fetch_landing_page(url: str, timeout: int = DEFAULT_TIMEOUT) -> Tuple[int, str, str]:
    headers = {
        "User-Agent": DEFAULT_USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }
    response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
    return int(response.status_code), response.url, response.text


def _resolve_input_targets(url: str, query: str = "", keywords=None, locations=None, max_pages: int = DEFAULT_MAX_PAGES) -> Dict[str, object]:
    normalized = _normalize_url(url)
    input_platform = detect_ats_platform_from_url(normalized)
    resolved_targets: List[str] = []
    blocked: List[Dict[str, str]] = []
    unsupported: List[Dict[str, str]] = []
    discovery_notes: Dict[str, object] = {}

    if not normalized:
        unsupported.append({"input_url": url, "url": url, "reason": "Invalid URL", "platform": "generic"})
        return {"targets": [], "resolved_targets": [], "blocked": blocked, "unsupported": unsupported}

    if _is_root_only_ats_url(normalized, input_platform):
        unsupported.append({"input_url": normalized, "url": normalized, "reason": "ATS root URL is missing a company slug", "platform": input_platform or "generic"})
        return {"targets": [], "resolved_targets": [], "blocked": blocked, "unsupported": unsupported}

    if input_platform in {"indeed", "naukri", "greenhouse", "lever", "smartrecruiters", "ashby", "workday", "workable", "icims"}:
        return {
            "targets": [normalized],
            "resolved_targets": [{"input_url": normalized, "targets": [normalized], "platform": input_platform}],
            "blocked": blocked,
            "unsupported": unsupported,
        }

    search_targets = _candidate_search_urls(normalized, query=query, keywords=keywords, locations=locations)

    try:
        status_code, final_url, html_text = _fetch_landing_page(normalized)
        final_platform = detect_ats_platform_from_url(final_url)
        if status_code >= 400 or _looks_like_block_page(html_text):
            blocked.append(
                {
                    "input_url": normalized,
                    "url": final_url or normalized,
                    "reason": f"Blocked or unavailable page ({status_code})",
                    "platform": final_platform or input_platform or "generic",
                }
            )
        else:
            ats_urls: List[str] = []
            canonical_final = _canonicalize_ats_url(final_url)
            if canonical_final:
                ats_urls.append(canonical_final)
            ats_urls.extend(_discover_ats_board_urls_from_html(final_url, html_text))
            ats_urls = _unique([_canonicalize_ats_url(item) for item in ats_urls if item])
            ats_urls = [item for item in ats_urls if item]

            if not ats_urls:
                ats_urls.extend(_ollama_extract_ats_urls(final_url, html_text))
            ats_urls = _unique([item for item in ats_urls if item])

            if ats_urls:
                resolved_targets.extend(ats_urls)
                discovery_notes["ats_urls"] = ats_urls
            else:
                resolved_targets.extend(search_targets)
                if _is_probable_job_url(final_url, final_url):
                    resolved_targets.append(final_url)
                resolved_targets.extend(_extract_candidate_job_links(final_url, html_text))
    except Exception as exc:
        blocked.append({"input_url": normalized, "url": normalized, "reason": str(exc), "platform": input_platform or "generic"})

    resolved_targets = _unique(resolved_targets)
    filtered_targets: List[str] = []
    for target in resolved_targets:
        platform = detect_ats_platform_from_url(target)
        if _is_root_only_ats_url(target, platform):
            unsupported.append({"input_url": normalized, "url": target, "reason": "Resolved to an ATS root URL without company slug", "platform": platform or "generic"})
            continue
        filtered_targets.append(target)

    if not filtered_targets and not blocked:
        unsupported.append({"input_url": normalized, "url": normalized, "reason": "No job board or openings page could be resolved", "platform": input_platform or "generic"})

    return {
        "targets": filtered_targets,
        "resolved_targets": [{"input_url": normalized, "targets": filtered_targets, "platform": input_platform or "generic", "discovery": discovery_notes}],
        "blocked": blocked,
        "unsupported": unsupported,
    }


def _fetch_text(url: str, timeout: int = DEFAULT_TIMEOUT, headers: Optional[Dict[str, str]] = None) -> Tuple[str, str, Dict[str, str]]:
    request_headers = {
        "User-Agent": DEFAULT_USER_AGENT,
        "Accept": "text/html,application/json;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }
    if headers:
        request_headers.update(headers)
    req = urllib.request.Request(url, headers=request_headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        final_url = resp.geturl()
        content_type = resp.headers.get_content_type() or ""
        charset = resp.headers.get_content_charset() or "utf-8"
        body = resp.read().decode(charset, errors="replace")
        return body, final_url, {"content_type": content_type, "charset": charset}


def _fetch_json(url: str, timeout: int = DEFAULT_TIMEOUT, headers: Optional[Dict[str, str]] = None):
    text, final_url, meta = _fetch_text(url, timeout=timeout, headers=headers)
    payload = _safe_json_loads(text)
    return payload, final_url, meta


def _safe_json_loads(text: str):
    try:
        return json.loads(text)
    except Exception:
        return None


def _split_text_list(value) -> List[str]:
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        items = []
        for item in value:
            items.extend(_split_text_list(item))
        return _unique(items)
    parts = re.split(r"[\n,;]+", _clean_text(value))
    return _unique(parts)


def _extract_emails(text: str) -> str:
    emails = re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,24}", text or "", flags=re.I)
    return "; ".join(_unique(emails))


def _extract_phone_numbers(text: str) -> str:
    matches = re.findall(r"(?:\+?\d[\d\s().-]{7,}\d)", text or "")
    cleaned = []
    for value in matches:
        value = re.sub(r"\s+", " ", value).strip()
        if len(re.sub(r"\D", "", value)) >= 8:
            cleaned.append(value)
    return "; ".join(_unique(cleaned))


def _extract_links_from_text(text: str) -> List[str]:
    links = re.findall(r"https?://[^\s\]\)>'\"]+", text or "", flags=re.I)
    return _unique(links)


def _extract_links_from_soup(soup: bs, base_url: str = "") -> List[str]:
    links = []
    for anchor in soup.find_all("a", href=True):
        href = _normalize_url(anchor.get("href"), base_url)
        if href:
            links.append(href)
    return _unique(links)


def _strip_html(value: str) -> str:
    if not value:
        return ""
    soup = bs(value, "html.parser")
    return _clean_text(soup.get_text(" "))


def _join_non_empty(parts: Sequence[str], sep: str = " | ") -> str:
    return sep.join([part for part in (_clean_text(x) for x in parts) if part])


def _build_post_text(company: str, role: str, location: str, description: str, platform: str) -> str:
    parts = []
    if role:
        parts.append(role)
    if company:
        parts.append(company)
    if location:
        parts.append(location)
    if platform:
        parts.append(platform)
    if description:
        parts.append(description)
    return _join_non_empty(parts, sep=" | ")


def _ensure_standard_row(row: Dict[str, object], platform: str = "") -> Dict[str, str]:
    all_links = _unique(
        _split_text_list(row.get("All Links"))
        + _split_text_list(row.get("Apply Links"))
        + _split_text_list(row.get("Primary Apply Link"))
        + _split_text_list(row.get("Post Link"))
    )
    apply_links = _unique(_split_text_list(row.get("Apply Links")) + _split_text_list(row.get("Primary Apply Link")))
    primary = _clean_text(row.get("Primary Apply Link")) or (apply_links[0] if apply_links else "")
    company = _clean_text(row.get("Company"))
    role = _clean_text(row.get("Role"))
    location = _clean_text(row.get("Location"))
    description = _clean_text(row.get("Job Description"))
    platform_value = _clean_text(row.get("Platform") or platform)
    post_text = _clean_text(row.get("Post Text")) or _build_post_text(company, role, location, description, platform_value)
    post_link = _clean_text(row.get("Post Link")) or primary
    author = _clean_text(row.get("Author Name")) or company or platform_value
    date_value = _clean_text(row.get("Date"))

    return {
        "Company": company,
        "Platform": platform_value,
        "Role": role,
        "Location": location,
        "Date": date_value,
        "Primary Apply Link": primary,
        "Apply Links": "; ".join(apply_links),
        "Job Description": description,
        "Post Text": post_text,
        "Post Link": post_link,
        "Author Name": author,
        "Emails": _clean_text(row.get("Emails")) or _extract_emails(f"{post_text} {description}"),
        "Phone Numbers": _clean_text(row.get("Phone Numbers")) or _extract_phone_numbers(f"{post_text} {description}"),
        "All Links": "; ".join(all_links),
    }


def _rows_to_dataframe(rows: List[Dict[str, object]]) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame(columns=STANDARD_COLUMNS)
    normalized = [_ensure_standard_row(row, platform=_clean_text(row.get("Platform"))) for row in rows]
    df = pd.DataFrame(normalized)
    for col in STANDARD_COLUMNS:
        if col not in df.columns:
            df[col] = ""
    ordered = [col for col in STANDARD_COLUMNS if col in df.columns]
    rest = [col for col in df.columns if col not in ordered]
    df = df[ordered + rest]
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].fillna("").map(_clean_text)
    df = df.drop_duplicates(subset=["Company", "Role", "Location", "Primary Apply Link", "Post Link"], keep="first")
    return df.reset_index(drop=True)


def detect_ats_platform_from_url(url: str) -> str:
    parsed = urllib.parse.urlparse(_clean_text(url))
    host = parsed.netloc.lower()
    path = parsed.path.lower()
    if "greenhouse.io" in host:
        return "greenhouse"
    if "lever.co" in host:
        return "lever"
    if "smartrecruiters.com" in host:
        return "smartrecruiters"
    if "ashbyhq.com" in host:
        return "ashby"
    if "workable.com" in host:
        return "workable"
    if "taleo.net" in host:
        return "taleo"
    if "myworkdayjobs.com" in host or "workday.com" in host:
        return "workday"
    if "icims.com" in host:
        return "icims"
    if "indeed." in host:
        return "indeed"
    if "naukri.com" in host:
        return "naukri"
    if "jobvite" in host:
        return "jobvite"
    if "careers" in path or "jobs" in path:
        return "generic"
    return "generic"


JOB_LINK_TERMS = (
    "job",
    "jobs",
    "career",
    "careers",
    "opening",
    "openings",
    "position",
    "positions",
    "apply",
    "search",
    "result",
    "results",
)
STRONG_JOB_LINK_TERMS = (
    "job",
    "jobs",
    "opening",
    "openings",
    "apply",
    "search",
    "result",
    "results",
)
NON_JOB_LINK_TERMS = (
    "privacy",
    "policy",
    "cookies",
    "terms",
    "insurance",
    "credit-card",
    "credit-cards",
    "notice",
    "ethics",
    "about",
    "news",
    "blog",
    "login",
    "signup",
    "investor",
)
JOB_TITLE_TERMS = (
    "engineer",
    "developer",
    "manager",
    "analyst",
    "designer",
    "consultant",
    "specialist",
    "lead",
    "architect",
    "scientist",
    "director",
    "associate",
    "intern",
    "officer",
    "executive",
    "coordinator",
    "product",
    "program",
)
BLOCK_PAGE_TERMS = (
    "attention required",
    "access denied",
    "forbidden",
    "verify you are human",
    "security check",
    "cloudflare",
    "akamai",
    "request unsuccessful",
    "bot detection",
)


def _host_labels(host: str) -> List[str]:
    labels = []
    for part in str(host or "").lower().split("."):
        if not part or part in {"www", "careers", "career", "jobs", "job", "com", "co", "in", "net", "org"}:
            continue
        if part not in labels:
            labels.append(part)
    return labels


def _is_root_only_ats_url(url: str, platform: str = "") -> bool:
    platform = platform or detect_ats_platform_from_url(url)
    parsed = urllib.parse.urlparse(_clean_text(url))
    path_parts = [part for part in parsed.path.split("/") if part]
    if platform in {"greenhouse", "lever", "smartrecruiters", "ashby", "workable"}:
        return len(path_parts) < 1
    if platform == "workday":
        return len(path_parts) < 1
    if platform == "icims":
        return len(path_parts) < 1
    return False


def _looks_like_block_page(html_text: str) -> bool:
    lowered = _clean_text(html_text).lower()
    if not lowered:
        return False
    return any(term in lowered for term in BLOCK_PAGE_TERMS)


def _is_probable_job_text(text: str) -> bool:
    lowered = _clean_text(text).lower()
    if not lowered or len(lowered) < 6:
        return False
    if any(term in lowered for term in NON_JOB_LINK_TERMS):
        return False
    return any(term in lowered for term in JOB_TITLE_TERMS)


def _is_probable_job_url(url: str, label: str = "") -> bool:
    lowered_url = _clean_text(url).lower()
    lowered_label = _clean_text(label).lower()
    if not lowered_url:
        return False
    if any(term in lowered_url or term in lowered_label for term in NON_JOB_LINK_TERMS):
        return False
    if any(term in lowered_url or term in lowered_label for term in JOB_LINK_TERMS):
        return True
    return _is_probable_job_text(label)


def _company_slug_candidates(company: str) -> List[str]:
    company = _clean_text(company)
    if not company:
        return []
    variants = {_slugify(company)}
    variants.add(re.sub(r"[^a-z0-9]+", "", company.lower()))
    variants.add(_slugify(company).replace("-", ""))
    variants.add(_slugify(company).replace("-", "."))
    return [variant for variant in variants if variant]


def discover_career_urls(company: str) -> List[str]:
    urls: List[str] = []
    urls.extend(discover_reference_urls_for_companies([company]))
    for slug in _company_slug_candidates(company):
        urls.extend(
            [
                f"https://boards.greenhouse.io/{slug}",
                f"https://jobs.lever.co/{slug}",
                f"https://careers.smartrecruiters.com/{slug}",
                f"https://jobs.ashbyhq.com/{slug}",
                f"https://{slug}.myworkdayjobs.com/en-US/{slug}",
                f"https://{slug}.wd3.myworkdayjobs.com/en-US/{slug}",
                f"https://{slug}.wd5.myworkdayjobs.com/en-US/{slug}",
                f"https://apply.workable.com/{slug}/",
            ]
        )
    return _unique(urls)


def _record_text(record: Dict[str, object]) -> str:
    parts = [
        record.get("Company", ""),
        record.get("Role", ""),
        record.get("Location", ""),
        record.get("Job Description", ""),
        record.get("Post Text", ""),
        record.get("Platform", ""),
        record.get("All Links", ""),
    ]
    return _clean_text(" ".join([_clean_text(part) for part in parts if _clean_text(part)]))


def _query_terms(query: str) -> List[str]:
    query = _clean_text(query).lower()
    if not query:
        return []
    parts = [query]
    stop_words = {"hiring", "jobs", "job", "opening", "openings", "role", "roles", "career", "careers"}
    words = [word for word in re.split(r"[^a-z0-9+#&/.-]+", query) if len(word) >= 3 and word not in stop_words]
    parts.extend(words)
    if len(words) >= 2:
        parts.append(" ".join(words[:2]))
    return _unique(parts)


def _match_any(haystack: str, values) -> bool:
    tokens = []
    for value in values or []:
        for token in _split_text_list(value):
            text = _clean_text(token).lower()
            if text:
                tokens.append(text)
    if not tokens:
        return True
    return any(token in haystack for token in _unique(tokens))


def _record_matches(record: Dict[str, object], query: str = "", keywords=None, companies=None, locations=None) -> bool:
    haystack = _record_text(record).lower()
    if not haystack:
        return False
    role_terms = _query_terms(query) + _split_text_list(keywords)
    company_terms = _split_text_list(companies)
    location_terms = _split_text_list(locations)
    if not role_terms and not company_terms and not location_terms:
        return True
    return (
        _match_any(haystack, role_terms)
        and _match_any(haystack, company_terms)
        and _match_any(haystack, location_terms)
    )


def _filter_board_rows(rows: List[Dict[str, str]], query: str = "", keywords=None, companies=None, locations=None) -> List[Dict[str, str]]:
    role_terms = _query_terms(query) + _split_text_list(keywords)
    company_terms = _split_text_list(companies)
    location_terms = _split_text_list(locations)
    if not role_terms and not company_terms and not location_terms:
        return rows[:]
    filtered = []
    for row in rows:
        haystack = _record_text(row).lower()
        if not haystack:
            continue
        if role_terms and not _match_any(haystack, role_terms):
            continue
        if company_terms and not _match_any(haystack, company_terms):
            continue
        if location_terms and not _match_any(haystack, location_terms):
            continue
        filtered.append(row)
    return filtered


def _jobspy_series_value(record, key: str) -> str:
    if key not in record.index:
        return ""
    value = record.get(key)
    if value is None:
        return ""
    if isinstance(value, float) and pd.isna(value):
        return ""
    if isinstance(value, (list, tuple, set)):
        return "; ".join(_unique(value))
    return _clean_text(value)


def _jobspy_rows_to_standard_rows(df: pd.DataFrame, platform: str) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    if df is None or df.empty:
        return rows
    for _, record in df.iterrows():
        company = _jobspy_series_value(record, "company")
        role = _jobspy_series_value(record, "title")
        location = _jobspy_series_value(record, "location")
        date_posted = _jobspy_series_value(record, "date_posted")
        description = _jobspy_series_value(record, "description")
        job_url = _jobspy_series_value(record, "job_url")
        direct_url = _jobspy_series_value(record, "company_url_direct")
        company_url = _jobspy_series_value(record, "company_url")
        primary_link = job_url or direct_url
        all_links = _unique([primary_link, direct_url, company_url])
        rows.append(
            _ensure_standard_row(
                {
                    "Company": company,
                    "Platform": platform,
                    "Role": role,
                    "Location": location,
                    "Date": date_posted,
                    "Primary Apply Link": primary_link,
                    "Apply Links": "; ".join(_unique([primary_link, direct_url])),
                    "Job Description": description,
                    "Post Text": _build_post_text(company, role, location, description, platform),
                    "Post Link": primary_link,
                    "Author Name": company or platform.title(),
                    "Emails": _jobspy_series_value(record, "emails"),
                    "All Links": "; ".join(all_links),
                },
                platform=platform,
            )
        )
    return rows


def _naukri_url_type(location: str) -> str:
    return "search_by_key_loc" if _clean_text(location) else "search_by_keyword"


def _naukri_seo_key(term: str, location: str) -> str:
    term_slug = _slugify(term) or "jobs"
    location_slug = _slugify(location)
    if location_slug:
        return f"{term_slug}-jobs-in-{location_slug}"
    return f"{term_slug}-jobs"


def _naukri_search_page_url(term: str, location: str) -> str:
    return f"https://www.naukri.com/{_naukri_seo_key(term, location)}"


def _naukri_api_url(term: str, location: str, page_no: int = 1) -> str:
    params = {
        "noOfResults": "20",
        "urlType": _naukri_url_type(location),
        "searchType": "adv",
        "keyword": _clean_text(term),
        "pageNo": str(max(1, int(page_no))),
        "seoKey": _naukri_seo_key(term, location),
        "src": "directSearch",
        "latLong": "",
    }
    cleaned_location = _clean_text(location)
    if cleaned_location:
        params["location"] = cleaned_location.lower()
    return "https://www.naukri.com/jobapi/v3/search?" + urllib.parse.urlencode(params)


def _extract_naukri_location(job: Dict[str, object]) -> str:
    for item in job.get("placeholders", []) or []:
        if _clean_text(item.get("type")) == "location":
            return _clean_text(item.get("label"))
    return ""


def _extract_naukri_salary(job: Dict[str, object]) -> str:
    for item in job.get("placeholders", []) or []:
        if _clean_text(item.get("type")) == "salary":
            return _clean_text(item.get("label"))
    return ""


def _extract_naukri_experience(job: Dict[str, object]) -> str:
    for item in job.get("placeholders", []) or []:
        if _clean_text(item.get("type")) == "experience":
            return _clean_text(item.get("label"))
    return _clean_text(job.get("experienceText"))


def _naukri_job_to_standard_row(job: Dict[str, object]) -> Dict[str, str]:
    company = _clean_text(job.get("companyName"))
    role = _clean_text(job.get("title"))
    location = _extract_naukri_location(job)
    date_value = _clean_text(job.get("footerPlaceholderLabel"))
    job_description = _strip_html(job.get("jobDescription") or "")
    skills = _clean_text(job.get("tagsAndSkills"))
    salary = _extract_naukri_salary(job)
    experience = _extract_naukri_experience(job)
    extra_bits = [part for part in [salary, experience, skills] if part]
    if extra_bits:
        detail_suffix = " | ".join(extra_bits)
        job_description = f"{job_description} | {detail_suffix}" if job_description else detail_suffix

    jd_url = _normalize_url(job.get("jdURL"), "https://www.naukri.com")
    company_url = ""
    static_url = _clean_text(job.get("staticUrl"))
    if static_url:
        company_url = _normalize_url(static_url, "https://www.naukri.com/")
    apply_links = _unique([jd_url, company_url])

    return _ensure_standard_row(
        {
            "Company": company,
            "Platform": "naukri",
            "Role": role,
            "Location": location,
            "Date": date_value,
            "Primary Apply Link": jd_url,
            "Apply Links": "; ".join(apply_links),
            "Job Description": job_description,
            "Post Text": _build_post_text(company, role, location, job_description, "naukri"),
            "Post Link": jd_url,
            "Author Name": company or "Naukri",
            "All Links": "; ".join(apply_links),
        },
        platform="naukri",
    )


def get_driver(headless: bool = True, performance_log: bool = False):
    """Single Chrome entry point: ChromeDriverManager only (no local cache / CHROMEDRIVER_PATH)."""
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080" if headless else "--window-size=1440,1200")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--remote-debugging-port=0")
    options.page_load_strategy = os.getenv("SCANNER_PAGE_LOAD_STRATEGY", "eager").strip() or "eager"
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    if performance_log:
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def _fetch_dynamic_html(url: str, status_cb=None) -> str:
    wait_seconds = max(2, int(os.getenv("SCANNER_SELENIUM_WAIT_SECONDS", str(DEFAULT_SELENIUM_PAGE_WAIT)) or DEFAULT_SELENIUM_PAGE_WAIT))
    page_timeout = max(wait_seconds + 5, int(os.getenv("SCANNER_SELENIUM_PAGE_TIMEOUT", "20") or "20"))
    _emit(status_cb, f"Selenium fallback loading {urllib.parse.urlparse(url).netloc or url}.")
    use_headless = os.getenv("SCANNER_SELENIUM_HEADLESS", "1").strip().lower() in {"1", "true", "yes", "on"}
    driver = get_driver(headless=use_headless)
    try:
        driver.set_page_load_timeout(page_timeout)
        driver.set_script_timeout(page_timeout)
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"},
        )
        try:
            driver.get(url)
        except TimeoutException:
            _emit(status_cb, f"Selenium timed out on {urllib.parse.urlparse(url).netloc or url}; using partial page content.")
        time.sleep(wait_seconds)
        return driver.page_source or ""
    finally:
        try:
            driver.quit()
        except Exception:
            pass


def _selenium_parse_job_page(url: str, platform: str, company_hint: str = "", status_cb=None) -> List[Dict[str, str]]:
    html_text = _fetch_dynamic_html(url, status_cb=status_cb)
    rows = _jobpostings_from_json_ld(url, html_text, platform, company_hint=company_hint)
    rows.extend(_generic_job_cards_from_html(url, html_text, platform, company_hint=company_hint))
    return rows


def _bootstrap_naukri_session(term: str, location: str, status_cb=None):
    page_url = _naukri_search_page_url(term, location)
    _emit(status_cb, "Opening Naukri in Chrome to bootstrap the search session.")
    naukri_headless = os.getenv("NAUKRI_HEADLESS", "0").strip().lower() in {"1", "true", "yes", "on"}
    try:
        driver = get_driver(headless=naukri_headless, performance_log=True)
    except Exception as exc:
        raise RuntimeError("Chrome startup failed for Naukri bootstrap.") from exc
    _emit(status_cb, "Chrome started.")
    try:
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"},
        )
        driver.execute_cdp_cmd("Network.enable", {})
        driver.get(page_url)

        request_headers = None
        first_body = None
        request_id = None

        for _ in range(30):
            time.sleep(1)
            logs = driver.get_log("performance")
            for entry in logs:
                try:
                    message = json.loads(entry["message"]).get("message", {})
                except Exception:
                    continue
                method = message.get("method")
                params = message.get("params", {})
                if method == "Network.requestWillBeSent":
                    request = params.get("request", {})
                    url = request.get("url", "")
                    if "jobapi/v3/search" in url and request_headers is None:
                        request_headers = request.get("headers", {})
                elif method == "Network.responseReceived":
                    response = params.get("response", {})
                    url = response.get("url", "")
                    if "jobapi/v3/search" in url and response.get("status") == 200:
                        request_id = params.get("requestId")
            if request_id:
                try:
                    body = driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
                    first_body = body.get("body", "")
                except Exception:
                    first_body = ""
                break

        cookies = {cookie["name"]: cookie["value"] for cookie in driver.get_cookies()}
    finally:
        driver.quit()

    if not request_headers:
        raise RuntimeError("Naukri bootstrap did not capture search headers.")

    session = requests.Session()
    for key, value in cookies.items():
        session.cookies.set(key, value, domain=".naukri.com")

    headers = {
        "Content-Type": "application/json",
        "Referer": page_url,
        "User-Agent": request_headers.get("User-Agent", DEFAULT_USER_AGENT),
        "accept": request_headers.get("accept", "application/json"),
        "appid": request_headers.get("appid", "109"),
        "clientid": request_headers.get("clientid", NAUKRI_DEFAULT_CLIENT_ID),
        "gid": request_headers.get("gid", NAUKRI_DEFAULT_GID),
        "nkparam": request_headers.get("nkparam", ""),
        "sec-ch-ua": request_headers.get("sec-ch-ua", ""),
        "sec-ch-ua-mobile": request_headers.get("sec-ch-ua-mobile", "?0"),
        "sec-ch-ua-platform": request_headers.get("sec-ch-ua-platform", '"Windows"'),
        "systemid": request_headers.get("systemid", "Naukri"),
    }
    headers = {key: value for key, value in headers.items() if value != ""}

    initial_payload = _safe_json_loads(first_body) if first_body else None
    if not isinstance(initial_payload, dict):
        initial_payload = None

    return session, headers, initial_payload


def _scan_naukri_with_browser(term: str, keywords=None, companies=None, locations=None, limit_per_source: int = DEFAULT_LIMIT_PER_SOURCE, max_pages: int = DEFAULT_MAX_PAGES, status_cb=None) -> SourceResult:
    role_terms = _unique([term, *(_split_text_list(keywords))])
    company_terms = _split_text_list(companies)
    search_terms = role_terms or company_terms or [""]
    location_values = _unique(_split_text_list(locations)) or [""]

    rows: List[Dict[str, str]] = []
    errors: List[str] = []
    scanned_urls: List[str] = []
    seen_jobs = set()

    bootstrap_term = search_terms[0]
    bootstrap_location = location_values[0]
    session, headers, initial_payload = _bootstrap_naukri_session(bootstrap_term, bootstrap_location, status_cb=status_cb)

    def append_jobs(payload):
        if not isinstance(payload, dict):
            return
        for job in payload.get("jobDetails", []) or []:
            job_id = _clean_text(job.get("jobId"))
            if job_id and job_id in seen_jobs:
                continue
            if job_id:
                seen_jobs.add(job_id)
            rows.append(_naukri_job_to_standard_row(job))

    append_jobs(initial_payload)

    for term_value in search_terms[:5]:
        if len(rows) >= limit_per_source:
            break
        for location in location_values[:5]:
            if len(rows) >= limit_per_source:
                break
            for page_no in range(1, max_pages + 1):
                if len(rows) >= limit_per_source:
                    break
                api_url = _naukri_api_url(term_value, location, page_no)
                referer = _naukri_search_page_url(term_value, location)
                scanned_urls.append(api_url)
                if page_no == 1 and term_value == bootstrap_term and location == bootstrap_location and initial_payload:
                    continue
                request_headers = dict(headers)
                request_headers["Referer"] = referer
                try:
                    response = session.get(api_url, headers=request_headers, timeout=DEFAULT_TIMEOUT)
                    if response.status_code not in {200}:
                        errors.append(f"Naukri browser API: HTTP {response.status_code}")
                        continue
                    payload = response.json()
                    append_jobs(payload)
                except Exception as exc:
                    errors.append(f"Naukri browser API: {exc}")

    filtered_rows = _filter_board_rows(rows, query=term, keywords=keywords, companies=companies, locations=locations)
    return SourceResult("naukri", filtered_rows[:limit_per_source], scanned_urls, errors)


def _scan_with_jobspy(site_name: str, query: str = "", keywords=None, companies=None, locations=None, limit_per_source: int = DEFAULT_LIMIT_PER_SOURCE, status_cb=None) -> Optional[SourceResult]:
    if _jobspy_scrape_jobs is None or site_name not in JOBSPY_SOURCE_NAMES:
        return None

    role_terms = _unique([query, *(_split_text_list(keywords))])
    company_terms = _split_text_list(companies)
    search_terms = role_terms or company_terms or [""]
    location_values = _unique(_split_text_list(locations)) or [""]

    rows: List[Dict[str, str]] = []
    errors: List[str] = []
    scanned_urls: List[str] = []
    label = site_name.title()

    _emit(status_cb, f"{label} JobSpy search started.")

    for term in search_terms[:5]:
        if len(rows) >= limit_per_source:
            break
        for location in location_values[:5]:
            if len(rows) >= limit_per_source:
                break
            remaining = max(5, min(limit_per_source - len(rows), limit_per_source))
            scanned_urls.append(f"jobspy://{site_name}?term={urllib.parse.quote(term or '*')}&location={urllib.parse.quote(location or '*')}")
            try:
                params = {
                    "site_name": [site_name],
                    "search_term": term or None,
                    "location": location or None,
                    "results_wanted": remaining,
                    "verbose": 0,
                }
                if site_name == "indeed":
                    params["country_indeed"] = "India"
                df = _jobspy_scrape_jobs(**params)
                rows.extend(_jobspy_rows_to_standard_rows(df, platform=site_name))
            except Exception as exc:
                errors.append(f"{label} JobSpy: {exc}")

    filtered_rows = _filter_board_rows(rows, query=query, keywords=keywords, companies=companies, locations=locations)
    return SourceResult(site_name, filtered_rows[:limit_per_source], scanned_urls, errors)


def _parse_json_ld_objects(soup: bs) -> List[Dict[str, object]]:
    objects: List[Dict[str, object]] = []
    for script in soup.find_all("script", attrs={"type": re.compile(r"ld\+json", re.I)}):
        raw = script.string or script.get_text() or ""
        raw = _clean_text(raw)
        if not raw:
            continue
        payload = _safe_json_loads(raw)
        if payload is None:
            continue
        stack = [payload]
        while stack:
            item = stack.pop()
            if isinstance(item, dict):
                if str(item.get("@type", "")).lower() == "jobposting":
                    objects.append(item)
                for value in item.values():
                    if isinstance(value, (dict, list)):
                        stack.append(value)
            elif isinstance(item, list):
                stack.extend(item)
    return objects


def _json_ld_location(value) -> str:
    if isinstance(value, dict):
        address = value.get("address")
        if isinstance(address, dict):
            pieces = [
                address.get("addressLocality"),
                address.get("addressRegion"),
                address.get("addressCountry"),
            ]
            text = ", ".join([_clean_text(piece) for piece in pieces if _clean_text(piece)])
            if text:
                return text
        return _clean_text(value.get("name") or value.get("addressLocality") or value.get("addressRegion"))
    if isinstance(value, list):
        parts = [_json_ld_location(item) for item in value]
        return ", ".join([part for part in parts if part])
    return _clean_text(value)


def _json_ld_to_row(payload: Dict[str, object], page_url: str, platform: str, company_hint: str = "") -> Dict[str, str]:
    title = _clean_text(payload.get("title") or payload.get("name"))
    company = company_hint
    hiring = payload.get("hiringOrganization")
    if isinstance(hiring, dict):
        company = _clean_text(hiring.get("name")) or company
    location = _json_ld_location(payload.get("jobLocation") or payload.get("jobLocationType") or payload.get("jobLocationType"))
    description = _strip_html(_clean_text(payload.get("description") or payload.get("summary") or payload.get("abstract")))
    apply_links = _unique(
        [
            _normalize_url(payload.get("url") or payload.get("applicationUrl") or payload.get("directApplyUrl") or "", page_url),
            _normalize_url(payload.get("sameAs") or "", page_url),
            page_url,
        ]
    )
    return _ensure_standard_row(
        {
            "Company": company,
            "Platform": platform,
            "Role": title,
            "Location": location,
            "Date": _clean_text(payload.get("datePosted") or payload.get("publishedAt") or payload.get("updatedAt")),
            "Primary Apply Link": apply_links[0] if apply_links else page_url,
            "Apply Links": "; ".join(apply_links),
            "Job Description": description,
            "Post Text": _build_post_text(company, title, location, description, platform),
            "Post Link": page_url,
            "Author Name": company or platform,
            "All Links": "; ".join(_unique(apply_links + [page_url])),
        },
        platform=platform,
    )


def _jobpostings_from_json_ld(page_url: str, html_text: str, platform: str, company_hint: str = "") -> List[Dict[str, str]]:
    soup = bs(html_text, "html.parser")
    rows = []
    for payload in _parse_json_ld_objects(soup):
        try:
            row = _json_ld_to_row(payload, page_url, platform=platform, company_hint=company_hint)
            rows.append(row)
        except Exception:
            continue
    return rows


def _parse_google_results_rows(page_url: str, html_text: str, platform: str, company_hint: str = "") -> List[Dict[str, str]]:
    soup = bs(html_text, "html.parser")
    base_url = _document_base_url(page_url, html_text)
    rows: List[Dict[str, str]] = []
    seen = set()
    for anchor in soup.find_all("a", href=True):
        href = _normalize_url(anchor.get("href"), base_url)
        if "/about/careers/applications/jobs/results/" not in href:
            continue
        last_segment = urllib.parse.urlparse(href).path.rstrip("/").split("/")[-1]
        if not re.match(r"^\d+-", last_segment):
            continue
        title = _clean_text(anchor.get_text(" "))
        if not _is_probable_job_text(title):
            title = re.sub(r"^\d+-", "", last_segment).replace("-", " ").strip()
        title = title.title()
        container = anchor.find_parent(["li", "div", "section", "article"]) or anchor
        text = _clean_text(container.get_text(" "))
        location_match = re.search(r"\b(remote|hybrid|bengaluru|bangalore|gurugram|gurgaon|noida|mumbai|pune|chennai|hyderabad|delhi|india)\b", text, flags=re.I)
        key = (title.lower(), href)
        if key in seen or not title:
            continue
        seen.add(key)
        rows.append(
            _ensure_standard_row(
                {
                    "Company": company_hint or "Google",
                    "Platform": platform,
                    "Role": title,
                    "Location": location_match.group(1) if location_match else "",
                    "Date": "",
                    "Primary Apply Link": href,
                    "Apply Links": href,
                    "Job Description": text[:500],
                    "Post Text": _build_post_text(company_hint or "Google", title, location_match.group(1) if location_match else "", text[:500], platform),
                    "Post Link": href,
                    "Author Name": company_hint or "Google",
                    "All Links": href,
                },
                platform=platform,
            )
        )
    return rows


def _generic_job_cards_from_html(page_url: str, html_text: str, platform: str, company_hint: str = "") -> List[Dict[str, str]]:
    parsed_page = urllib.parse.urlparse(page_url)
    if "google.com" in parsed_page.netloc.lower() and "/about/careers/applications/jobs/results" in parsed_page.path.lower():
        google_rows = _parse_google_results_rows(page_url, html_text, platform, company_hint=company_hint)
        if google_rows:
            return google_rows

    soup = bs(html_text, "html.parser")
    base_url = _document_base_url(page_url, html_text)
    rows: List[Dict[str, str]] = []
    seen = set()
    selectors = [
        "article",
        "li",
        "div[class*='job']",
        "div[class*='opening']",
        "div[class*='career']",
        "section",
    ]
    for node in soup.select(",".join(selectors)):
        text = _clean_text(node.get_text(" "))
        if len(text) < 25:
            continue
        links = [anchor.get("href") for anchor in node.find_all("a", href=True)]
        links = _unique([_normalize_url(link, base_url) for link in links])
        title = ""
        title_candidates = []
        for selector in ["h1", "h2", "h3", "a", "strong"]:
            found = node.select_one(selector)
            if found:
                candidate = _clean_text(found.get_text(" "))
                if candidate:
                    title_candidates.append(candidate)
        if title_candidates:
            title = sorted(title_candidates, key=lambda value: (-len(value), value))[0]
        company = company_hint or _clean_text(node.get("data-company") or node.get("aria-label"))
        location_match = re.search(r"\b(remote|hybrid|onsite|bengaluru|bangalore|gurugram|gurgaon|noida|mumbai|pune|chennai|hyderabad|delhi|india)\b", text, flags=re.I)
        location = location_match.group(1) if location_match else ""
        primary_link = links[0] if links else page_url
        if not title and not links:
            continue
        if not _is_probable_job_url(primary_link, title) and not _is_probable_job_text(title):
            continue
        key = (title.lower(), primary_link if links else text[:80].lower())
        if key in seen:
            continue
        seen.add(key)
        rows.append(
            _ensure_standard_row(
                {
                    "Company": company,
                    "Platform": platform,
                    "Role": title,
                    "Location": location,
                    "Date": "",
                    "Primary Apply Link": primary_link,
                    "Apply Links": "; ".join(links),
                    "Job Description": text[:500],
                    "Post Text": _build_post_text(company, title, location, text[:500], platform),
                    "Post Link": primary_link,
                    "Author Name": company or platform,
                    "All Links": "; ".join(_unique(links + [page_url])),
                },
                platform=platform,
            )
        )
    return rows


@dataclass
class SourceResult:
    source: str
    rows: List[Dict[str, str]]
    scanned_urls: List[str]
    errors: List[str]


class BaseSourceAdapter:
    name = "base"

    def scan(self, **kwargs) -> SourceResult:
        raise NotImplementedError


class IndeedAdapter(BaseSourceAdapter):
    name = "indeed"

    def _build_urls(self, query: str, keywords, companies, locations, max_pages: int) -> List[str]:
        search_terms = _unique([query, *(keywords or [])])
        if not search_terms:
            search_terms = _split_text_list(companies)
        if not search_terms:
            search_terms = [""]
        location_values = _unique(locations or [""])
        if not location_values:
            location_values = [""]
        urls = []
        for term in search_terms[:5]:
            for location in location_values[:5]:
                for page in range(max_pages):
                    start = page * 10
                    params = {"q": term, "start": str(start)}
                    cleaned_location = _clean_text(location)
                    if cleaned_location:
                        params["l"] = cleaned_location
                    urls.append("https://in.indeed.com/jobs?" + urllib.parse.urlencode(params))
        return _unique(urls)

    def _parse(self, url: str, html_text: str) -> List[Dict[str, str]]:
        soup = bs(html_text, "html.parser")
        rows: List[Dict[str, str]] = []
        seen = set()
        cards = soup.select("a.tapItem, div.job_seen_beacon, td.resultContent")
        for card in cards:
            text = _clean_text(card.get_text(" "))
            if len(text) < 20:
                continue
            title = ""
            for selector in ["h2", "a[data-jk]", "a"]:
                node = card.select_one(selector)
                if node:
                    title = _clean_text(node.get_text(" "))
                    if title:
                        break
            company = ""
            for selector in ["span.companyName", "[data-testid='company-name']", ".companyName"]:
                node = card.select_one(selector)
                if node:
                    company = _clean_text(node.get_text(" "))
                    if company:
                        break
            location = ""
            for selector in ["div.companyLocation", "[data-testid='text-location']", ".companyLocation"]:
                node = card.select_one(selector)
                if node:
                    location = _clean_text(node.get_text(" "))
                    if location:
                        break
            date = ""
            for selector in ["span.date", "[data-testid='myJobsStateDate']", ".date"]:
                node = card.select_one(selector)
                if node:
                    date = _clean_text(node.get_text(" "))
                    if date:
                        break
            snippet = ""
            for selector in ["div.job-snippet", "[data-testid='job-snippet']"]:
                node = card.select_one(selector)
                if node:
                    snippet = _clean_text(node.get_text(" "))
                    if snippet:
                        break
            link = ""
            anchor = card.select_one("a[href]")
            if anchor:
                link = _normalize_url(anchor.get("href"), url)
            if not title and not link:
                continue
            key = (title.lower(), company.lower(), location.lower(), link)
            if key in seen:
                continue
            seen.add(key)
            rows.append(
                _ensure_standard_row(
                    {
                        "Company": company,
                        "Platform": self.name,
                        "Role": title,
                        "Location": location,
                        "Date": date,
                        "Primary Apply Link": link,
                        "Apply Links": link,
                        "Job Description": snippet or text[:500],
                        "Post Text": _build_post_text(company, title, location, snippet or text[:500], self.name),
                        "Post Link": link,
                        "Author Name": company or "Indeed",
                        "All Links": link,
                    },
                    platform=self.name,
                )
            )
        return rows

    def _direct_urls(self, career_urls) -> List[str]:
        return _unique([_clean_text(url) for url in (career_urls or []) if detect_ats_platform_from_url(url) == self.name])

    def _parse_page(self, url: str, html_text: str) -> List[Dict[str, str]]:
        company = _slugify(url)
        rows = _jobpostings_from_json_ld(url, html_text, self.name, company_hint=company)
        rows.extend(self._parse(url, html_text))
        rows.extend(_generic_job_cards_from_html(url, html_text, self.name, company_hint=company))
        return rows

    def scan(self, query: str = "", keywords=None, companies=None, locations=None, career_urls=None, limit_per_source: int = DEFAULT_LIMIT_PER_SOURCE, max_pages: int = DEFAULT_MAX_PAGES, status_cb=None, direct_urls_only: bool = False, enforce_result_limit: bool = True, url_progress_state=None) -> SourceResult:
        direct_urls = self._direct_urls(career_urls)
        rows: List[Dict[str, str]] = []
        errors: List[str] = []
        scanned_urls: List[str] = []
        if direct_urls:
            _emit(status_cb, "Scanning Indeed URLs one by one.")
            for index, url in enumerate(direct_urls, start=1):
                _emit_url_progress(status_cb, self.name, index, len(direct_urls), url, progress_state=url_progress_state)
                target_urls = _search_url_variants(url, query=query, keywords=keywords, locations=locations, platform_hint=self.name, max_pages=max_pages)
                for target_url in target_urls:
                    scanned_urls.append(target_url)
                    try:
                        html_text, _, _ = _fetch_text(target_url)
                        rows.extend(self._parse_page(target_url, html_text))
                    except Exception as exc:
                        errors.append(f"Indeed URL: {exc}")
            rows = _filter_board_rows(rows, query=query, keywords=keywords, companies=companies, locations=locations)
            if direct_urls_only:
                return SourceResult(self.name, _limit_rows(rows, limit_per_source, enforce_result_limit), scanned_urls, errors)
        elif direct_urls_only:
            return SourceResult(self.name, [], [], [])

        jobspy_result = _scan_with_jobspy(
            self.name,
            query=query,
            keywords=keywords,
            companies=companies,
            locations=locations,
            limit_per_source=limit_per_source,
            status_cb=status_cb,
        )
        if jobspy_result and jobspy_result.rows:
            merged_rows = rows + jobspy_result.rows
            merged_urls = scanned_urls + jobspy_result.scanned_urls
            merged_errors = errors + jobspy_result.errors
            return SourceResult(self.name, _limit_rows(_filter_board_rows(merged_rows, query=query, keywords=keywords, companies=companies, locations=locations), limit_per_source, enforce_result_limit), merged_urls, merged_errors)

        urls = self._build_urls(query, keywords, companies, locations, max_pages)
        errors.extend(jobspy_result.errors[:] if jobspy_result else [])
        _emit(status_cb, "Scanning Indeed public search results.")
        for url in urls:
            if len(rows) >= limit_per_source:
                break
            try:
                html_text, _, _ = _fetch_text(url)
                rows.extend(self._parse(url, html_text))
            except Exception as exc:
                errors.append(f"Indeed: {exc}")
        rows = _filter_board_rows(rows, query=query, keywords=keywords, companies=companies, locations=locations)
        return SourceResult(self.name, _limit_rows(rows, limit_per_source, enforce_result_limit), scanned_urls + (jobspy_result.scanned_urls if jobspy_result else []) + urls, errors)


class NaukriAdapter(BaseSourceAdapter):
    name = "naukri"

    def _build_urls(self, query: str, keywords, companies, locations, max_pages: int) -> List[str]:
        search_terms = _unique([query, *(keywords or [])])
        if not search_terms:
            search_terms = _split_text_list(companies)
        if not search_terms:
            search_terms = [""]
        location_values = _unique(locations or [""])
        if not location_values:
            location_values = [""]
        urls = []
        for term in search_terms[:5]:
            for location in location_values[:5]:
                for page in range(max_pages):
                    params = {"keyword": term}
                    cleaned_location = _clean_text(location)
                    if cleaned_location:
                        params["location"] = cleaned_location
                    params["pageNo"] = str(page + 1)
                    urls.append("https://www.naukri.com/job-listings?" + urllib.parse.urlencode(params))
        return _unique(urls)

    def _parse(self, url: str, html_text: str) -> List[Dict[str, str]]:
        soup = bs(html_text, "html.parser")
        rows: List[Dict[str, str]] = []
        seen = set()
        cards = soup.select("article, div.jobTuple, div[data-job-id], div[class*='jobTuple']")
        if not cards:
            cards = soup.select("a[href*='job-listings'], a[href*='jobdetail']")
        for card in cards:
            text = _clean_text(card.get_text(" "))
            if len(text) < 20:
                continue
            title = ""
            company = ""
            location = ""
            date = ""
            snippet = ""
            for selector in ["a.title", "a[title]", "h2", "h3", "span.title"]:
                node = card.select_one(selector)
                if node:
                    title = _clean_text(node.get_text(" "))
                    if title:
                        break
            for selector in ["a.subTitle", "span.comp-name", "[class*='company']", "[class*='CompName']"]:
                node = card.select_one(selector)
                if node:
                    company = _clean_text(node.get_text(" "))
                    if company:
                        break
            for selector in ["span.locWdth", "li.location", "[class*='loc']", "[class*='Location']"]:
                node = card.select_one(selector)
                if node:
                    location = _clean_text(node.get_text(" "))
                    if location:
                        break
            for selector in ["span.date", "[class*='date']", "[class*='Date']"]:
                node = card.select_one(selector)
                if node:
                    date = _clean_text(node.get_text(" "))
                    if date:
                        break
            for selector in ["div.job-description", "[class*='desc']", "[class*='snippet']"]:
                node = card.select_one(selector)
                if node:
                    snippet = _clean_text(node.get_text(" "))
                    if snippet:
                        break
            link = ""
            anchor = card.select_one("a[href]")
            if anchor:
                link = _normalize_url(anchor.get("href"), url)
            if not title and not link:
                continue
            key = (title.lower(), company.lower(), location.lower(), link)
            if key in seen:
                continue
            seen.add(key)
            rows.append(
                _ensure_standard_row(
                    {
                        "Company": company,
                        "Platform": self.name,
                        "Role": title,
                        "Location": location,
                        "Date": date,
                        "Primary Apply Link": link,
                        "Apply Links": link,
                        "Job Description": snippet or text[:500],
                        "Post Text": _build_post_text(company, title, location, snippet or text[:500], self.name),
                        "Post Link": link,
                        "Author Name": company or "Naukri",
                        "All Links": link,
                    },
                    platform=self.name,
                )
            )
        return rows

    def _direct_urls(self, career_urls) -> List[str]:
        return _unique([_clean_text(url) for url in (career_urls or []) if detect_ats_platform_from_url(url) == self.name])

    def _parse_page(self, url: str, html_text: str) -> List[Dict[str, str]]:
        company = _slugify(url)
        rows = _jobpostings_from_json_ld(url, html_text, self.name, company_hint=company)
        rows.extend(self._parse(url, html_text))
        rows.extend(_generic_job_cards_from_html(url, html_text, self.name, company_hint=company))
        return rows

    def scan(self, query: str = "", keywords=None, companies=None, locations=None, career_urls=None, limit_per_source: int = DEFAULT_LIMIT_PER_SOURCE, max_pages: int = DEFAULT_MAX_PAGES, status_cb=None, direct_urls_only: bool = False, enforce_result_limit: bool = True, url_progress_state=None) -> SourceResult:
        direct_urls = self._direct_urls(career_urls)
        rows: List[Dict[str, str]] = []
        errors: List[str] = []
        scanned_urls: List[str] = []
        if direct_urls:
            _emit(status_cb, "Scanning Naukri URLs one by one.")
            for index, url in enumerate(direct_urls, start=1):
                _emit_url_progress(status_cb, self.name, index, len(direct_urls), url, progress_state=url_progress_state)
                target_urls = _search_url_variants(url, query=query, keywords=keywords, locations=locations, platform_hint=self.name, max_pages=max_pages)
                for target_url in target_urls:
                    scanned_urls.append(target_url)
                    try:
                        html_text, _, _ = _fetch_text(target_url)
                        rows.extend(self._parse_page(target_url, html_text))
                    except Exception as exc:
                        errors.append(f"Naukri URL: {exc}")
            rows = _filter_board_rows(rows, query=query, keywords=keywords, companies=companies, locations=locations)
            if direct_urls_only:
                return SourceResult(self.name, _limit_rows(rows, limit_per_source, enforce_result_limit), scanned_urls, errors)
        elif direct_urls_only:
            return SourceResult(self.name, [], [], [])

        browser_result = None
        try:
            browser_result = _scan_naukri_with_browser(
                query,
                keywords=keywords,
                companies=companies,
                locations=locations,
                limit_per_source=limit_per_source,
                max_pages=max_pages,
                status_cb=status_cb,
            )
        except Exception as exc:
            browser_result = SourceResult(self.name, [], [], [f"Naukri browser API: {exc}"])
        if browser_result and browser_result.rows:
            merged_rows = rows + browser_result.rows
            merged_urls = scanned_urls + browser_result.scanned_urls
            merged_errors = errors + browser_result.errors
            return SourceResult(self.name, _limit_rows(_filter_board_rows(merged_rows, query=query, keywords=keywords, companies=companies, locations=locations), limit_per_source, enforce_result_limit), merged_urls, merged_errors)

        jobspy_result = _scan_with_jobspy(
            self.name,
            query=query,
            keywords=keywords,
            companies=companies,
            locations=locations,
            limit_per_source=limit_per_source,
            status_cb=status_cb,
        )
        if jobspy_result and jobspy_result.rows:
            merged_rows = rows + jobspy_result.rows
            merged_urls = scanned_urls + jobspy_result.scanned_urls
            merged_errors = errors + jobspy_result.errors
            return SourceResult(self.name, _limit_rows(_filter_board_rows(merged_rows, query=query, keywords=keywords, companies=companies, locations=locations), limit_per_source, enforce_result_limit), merged_urls, merged_errors)

        urls = self._build_urls(query, keywords, companies, locations, max_pages)
        if browser_result:
            errors.extend(browser_result.errors)
        if jobspy_result:
            errors.extend(jobspy_result.errors)
        _emit(status_cb, "Scanning Naukri public search results.")
        for url in urls:
            if len(rows) >= limit_per_source:
                break
            try:
                html_text, _, _ = _fetch_text(url)
                rows.extend(self._parse(url, html_text))
            except Exception as exc:
                errors.append(f"Naukri: {exc}")
        rows = _filter_board_rows(rows, query=query, keywords=keywords, companies=companies, locations=locations)
        scanned_urls = []
        if browser_result:
            scanned_urls.extend(browser_result.scanned_urls)
        if jobspy_result:
            scanned_urls.extend(jobspy_result.scanned_urls)
        scanned_urls.extend(urls)
        return SourceResult(self.name, _limit_rows(rows, limit_per_source, enforce_result_limit), scanned_urls, errors)


class CareerSourceAdapter(BaseSourceAdapter):
    name = "career"
    platform = "generic"

    def _filter_rows(self, rows: List[Dict[str, str]], query: str, keywords, companies, locations) -> List[Dict[str, str]]:
        filtered = []
        for row in rows:
            if _record_matches(row, query=query, keywords=keywords, companies=companies, locations=locations):
                filtered.append(row)
        return filtered

    def _discover_urls(self, companies, career_urls) -> List[str]:
        urls: List[str] = []
        urls.extend([_clean_text(url) for url in (career_urls or []) if _clean_text(url)])
        for company in companies or []:
            urls.extend(discover_career_urls(company))
        return _unique(urls)


class GreenhouseAdapter(CareerSourceAdapter):
    name = "greenhouse"
    platform = "greenhouse"

    def _company_from_url(self, url: str) -> str:
        parsed = urllib.parse.urlparse(url)
        path = parsed.path.strip("/")
        if parsed.netloc == "job-boards.greenhouse.io":
            for_param = urllib.parse.parse_qs(parsed.query).get("for")
            if for_param:
                return for_param[0]
        if parsed.netloc.endswith("boards.greenhouse.io"):
            if path:
                return path.split("/")[0]
            if path == "embed":
                for_param = urllib.parse.parse_qs(parsed.query).get("for")
                if for_param:
                    return for_param[0]
        match = re.search(r"/boards/([^/?#]+)", path)
        if match:
            return match.group(1)
        return ""

    def _api_urls(self, url: str) -> List[str]:
        company = self._company_from_url(url)
        if not company:
            return []
        return [f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs?content=true"]

    def _parse_api(self, company: str, json_payload) -> List[Dict[str, str]]:
        jobs = []
        if isinstance(json_payload, dict):
            jobs = json_payload.get("jobs") or json_payload.get("results") or []
        if not isinstance(jobs, list):
            return []
        rows = []
        for item in jobs:
            if not isinstance(item, dict):
                continue
            location = ""
            if isinstance(item.get("location"), dict):
                location = _clean_text(item["location"].get("name"))
            description = _strip_html(_clean_text(item.get("content") or item.get("description")))
            link = _clean_text(item.get("absolute_url") or item.get("url"))
            rows.append(
                _ensure_standard_row(
                    {
                        "Company": company,
                        "Platform": self.platform,
                        "Role": _clean_text(item.get("title") or item.get("name")),
                        "Location": location,
                        "Date": _clean_text(item.get("updated_at") or item.get("created_at") or item.get("published_at")),
                        "Primary Apply Link": link,
                        "Apply Links": link,
                        "Job Description": description,
                        "Post Text": _build_post_text(company, _clean_text(item.get("title") or item.get("name")), location, description, self.platform),
                        "Post Link": link,
                        "Author Name": company or self.platform,
                        "All Links": link,
                    },
                    platform=self.platform,
                )
            )
        return rows

    def scan(self, query: str = "", keywords=None, companies=None, locations=None, career_urls=None, limit_per_source: int = DEFAULT_LIMIT_PER_SOURCE, max_pages: int = DEFAULT_MAX_PAGES, status_cb=None, direct_urls_only: bool = False, enforce_result_limit: bool = True, url_progress_state=None) -> SourceResult:
        if direct_urls_only:
            urls = _unique([_clean_text(url) for url in (career_urls or []) if detect_ats_platform_from_url(url) == self.name])
        else:
            urls = self._discover_urls(companies, career_urls)
        rows: List[Dict[str, str]] = []
        errors: List[str] = []
        scanned_urls: List[str] = []
        _emit(status_cb, "Scanning Greenhouse boards.")
        for index, url in enumerate(urls, start=1):
            if detect_ats_platform_from_url(url) != self.name:
                continue
            _emit_url_progress(status_cb, self.name, index, len(urls), url, progress_state=url_progress_state)
            api_urls = self._api_urls(url)
            company = self._company_from_url(url)
            for api_url in api_urls:
                scanned_urls.append(api_url)
                try:
                    payload, _, _ = _fetch_json(api_url)
                    rows.extend(self._parse_api(company, payload))
                except Exception as exc:
                    errors.append(f"Greenhouse: {exc}")
                    try:
                        html_text, _, _ = _fetch_text(url)
                        rows.extend(_jobpostings_from_json_ld(url, html_text, self.platform, company_hint=company))
                        rows.extend(_generic_job_cards_from_html(url, html_text, self.platform, company_hint=company))
                    except Exception as exc2:
                        errors.append(f"Greenhouse fallback: {exc2}")
        rows = self._filter_rows(rows, query, keywords, companies, locations)
        return SourceResult(self.name, _limit_rows(rows, limit_per_source, enforce_result_limit), scanned_urls or urls, errors)


class LeverAdapter(CareerSourceAdapter):
    name = "lever"
    platform = "lever"

    def _company_from_url(self, url: str) -> str:
        parsed = urllib.parse.urlparse(url)
        if parsed.netloc.endswith("jobs.lever.co"):
            parts = [part for part in parsed.path.split("/") if part]
            if parts:
                return parts[0]
        return ""

    def _api_url(self, company: str) -> str:
        return f"https://api.lever.co/v0/postings/{company}?mode=json"

    def _parse_api(self, company: str, payload) -> List[Dict[str, str]]:
        if not isinstance(payload, list):
            return []
        rows = []
        for item in payload:
            if not isinstance(item, dict):
                continue
            categories = item.get("categories") if isinstance(item.get("categories"), dict) else {}
            location = _clean_text(categories.get("location") or categories.get("commitment"))
            description = _strip_html(_clean_text(item.get("description") or item.get("text")))
            link = _clean_text(item.get("hostedUrl") or item.get("applyUrl") or item.get("url"))
            rows.append(
                _ensure_standard_row(
                    {
                        "Company": company,
                        "Platform": self.platform,
                        "Role": _clean_text(item.get("text") or item.get("title")),
                        "Location": location,
                        "Date": _clean_text(item.get("createdAt") or item.get("updatedAt")),
                        "Primary Apply Link": link,
                        "Apply Links": link,
                        "Job Description": description,
                        "Post Text": _build_post_text(company, _clean_text(item.get("text")), location, description, self.platform),
                        "Post Link": link,
                        "Author Name": company or self.platform,
                        "All Links": link,
                    },
                    platform=self.platform,
                )
            )
        return rows

    def scan(self, query: str = "", keywords=None, companies=None, locations=None, career_urls=None, limit_per_source: int = DEFAULT_LIMIT_PER_SOURCE, max_pages: int = DEFAULT_MAX_PAGES, status_cb=None, direct_urls_only: bool = False, enforce_result_limit: bool = True, url_progress_state=None) -> SourceResult:
        urls = []
        if not direct_urls_only:
            for company in companies or []:
                slug = _slugify(company)
                if slug:
                    urls.append(self._api_url(slug))
        for url in career_urls or []:
            if detect_ats_platform_from_url(url) == self.name:
                company = self._company_from_url(url) or _slugify(url)
                if company:
                    urls.append(self._api_url(company))
        urls = _unique(urls)
        rows: List[Dict[str, str]] = []
        errors: List[str] = []
        scanned_urls: List[str] = []
        _emit(status_cb, "Scanning Lever job postings.")
        for index, url in enumerate(urls, start=1):
            _emit_url_progress(status_cb, self.name, index, len(urls), url, progress_state=url_progress_state)
            scanned_urls.append(url)
            try:
                payload, _, _ = _fetch_json(url)
                company = urllib.parse.urlparse(url).path.split("/")[-1]
                rows.extend(self._parse_api(company, payload))
            except Exception as exc:
                errors.append(f"Lever: {exc}")
        rows = self._filter_rows(rows, query, keywords, companies, locations)
        return SourceResult(self.name, _limit_rows(rows, limit_per_source, enforce_result_limit), scanned_urls or urls, errors)


class SmartRecruitersAdapter(CareerSourceAdapter):
    name = "smartrecruiters"
    platform = "smartrecruiters"

    def _company_from_url(self, url: str) -> str:
        parsed = urllib.parse.urlparse(url)
        if parsed.netloc.endswith("smartrecruiters.com"):
            parts = [part for part in parsed.path.split("/") if part]
            if parsed.netloc == "api.smartrecruiters.com":
                if "companies" in parts:
                    try:
                        idx = parts.index("companies")
                        return parts[idx + 1]
                    except Exception:
                        return ""
            if parts:
                return parts[0]
        return ""

    def _api_url(self, company: str, offset: int = 0, limit: int = 100) -> str:
        return f"https://api.smartrecruiters.com/v1/companies/{company}/postings?limit={limit}&offset={offset}"

    def _parse_api(self, company: str, payload) -> List[Dict[str, str]]:
        content = []
        if isinstance(payload, dict):
            content = payload.get("content") or payload.get("jobs") or []
        if not isinstance(content, list):
            return []
        rows = []
        for item in content:
            if not isinstance(item, dict):
                continue
            loc = item.get("location") if isinstance(item.get("location"), dict) else {}
            location = _join_non_empty([loc.get("city"), loc.get("region"), loc.get("country")], sep=", ")
            link = _clean_text(item.get("applyUrl") or item.get("url") or item.get("ref"))
            description = _strip_html(_clean_text(item.get("jobAd") or item.get("description")))
            rows.append(
                _ensure_standard_row(
                    {
                        "Company": company,
                        "Platform": self.platform,
                        "Role": _clean_text(item.get("name") or item.get("title")),
                        "Location": location,
                        "Date": _clean_text(item.get("releasedDate") or item.get("updatedDate") or item.get("publishedDate")),
                        "Primary Apply Link": link,
                        "Apply Links": link,
                        "Job Description": description,
                        "Post Text": _build_post_text(company, _clean_text(item.get("name")), location, description, self.platform),
                        "Post Link": link,
                        "Author Name": company or self.platform,
                        "All Links": link,
                    },
                    platform=self.platform,
                )
            )
        return rows

    def scan(self, query: str = "", keywords=None, companies=None, locations=None, career_urls=None, limit_per_source: int = DEFAULT_LIMIT_PER_SOURCE, max_pages: int = DEFAULT_MAX_PAGES, status_cb=None, direct_urls_only: bool = False, enforce_result_limit: bool = True, url_progress_state=None) -> SourceResult:
        urls = []
        if not direct_urls_only:
            for company in companies or []:
                slug = _slugify(company)
                if slug:
                    urls.append(self._api_url(slug))
        for url in career_urls or []:
            if detect_ats_platform_from_url(url) == self.name:
                company = self._company_from_url(url) or _slugify(url)
                if company:
                    urls.append(self._api_url(company))
        urls = _unique(urls)
        rows: List[Dict[str, str]] = []
        errors: List[str] = []
        scanned_urls: List[str] = []
        _emit(status_cb, "Scanning SmartRecruiters job boards.")
        for index, url in enumerate(urls, start=1):
            _emit_url_progress(status_cb, self.name, index, len(urls), url, progress_state=url_progress_state)
            scanned_urls.append(url)
            try:
                payload, _, _ = _fetch_json(url)
                company = self._company_from_url(url) or _slugify(url)
                rows.extend(self._parse_api(company, payload))
            except Exception as exc:
                errors.append(f"SmartRecruiters: {exc}")
        rows = self._filter_rows(rows, query, keywords, companies, locations)
        return SourceResult(self.name, _limit_rows(rows, limit_per_source, enforce_result_limit), scanned_urls or urls, errors)


class AshbyAdapter(CareerSourceAdapter):
    name = "ashby"
    platform = "ashby"

    def _company_from_url(self, url: str) -> str:
        parsed = urllib.parse.urlparse(url)
        if "jobs.ashbyhq.com" in parsed.netloc:
            parts = [part for part in parsed.path.split("/") if part]
            if parts:
                return parts[0]
        if parsed.netloc == "api.ashbyhq.com":
            parts = [part for part in parsed.path.split("/") if part]
            if len(parts) >= 3 and parts[0] == "posting-api" and parts[1] == "job-board":
                return parts[2]
        return ""

    def _candidate_urls(self, companies, career_urls) -> List[str]:
        urls = []
        for company in companies or []:
            slug = _slugify(company)
            if slug:
                urls.append(f"https://jobs.ashbyhq.com/{slug}")
        for url in career_urls or []:
            if detect_ats_platform_from_url(url) == self.name:
                urls.append(url)
        return _unique(urls)

    def _api_url(self, company_slug: str) -> str:
        return f"https://api.ashbyhq.com/posting-api/job-board/{company_slug}?includeCompensation=true"

    def _parse_api(self, company_slug: str, payload) -> List[Dict[str, str]]:
        if not isinstance(payload, dict):
            return []
        jobs = payload.get("jobs") or []
        if not isinstance(jobs, list):
            return []
        company_name = _clean_text(payload.get("name") or company_slug)
        rows = []
        for item in jobs:
            if not isinstance(item, dict):
                continue
            role = _clean_text(item.get("title"))
            if not role:
                continue
            location = _clean_text(item.get("location"))
            if _clean_text(item.get("isRemote")) == "True" or item.get("isRemote") is True:
                location = f"{location} (Remote)".strip() if location else "Remote"
            description = _strip_html(_clean_text(item.get("descriptionPlain") or item.get("descriptionHtml")))
            link = _clean_text(item.get("jobUrl") or item.get("applyUrl"))
            rows.append(
                _ensure_standard_row(
                    {
                        "Company": company_name or company_slug,
                        "Platform": self.platform,
                        "Role": role,
                        "Location": location,
                        "Date": _clean_text(item.get("publishedAt")),
                        "Primary Apply Link": link,
                        "Apply Links": link,
                        "Job Description": description,
                        "Post Text": _build_post_text(company_name, role, location, description, self.platform),
                        "Post Link": link,
                        "Author Name": company_name or self.platform,
                        "All Links": link,
                    },
                    platform=self.platform,
                )
            )
        return rows

    def _parse_html(self, url: str, html_text: str, company_hint: str = "") -> List[Dict[str, str]]:
        rows = _jobpostings_from_json_ld(url, html_text, self.platform, company_hint=company_hint)
        if rows:
            return rows
        return _generic_job_cards_from_html(url, html_text, self.platform, company_hint=company_hint)

    def scan(self, query: str = "", keywords=None, companies=None, locations=None, career_urls=None, limit_per_source: int = DEFAULT_LIMIT_PER_SOURCE, max_pages: int = DEFAULT_MAX_PAGES, status_cb=None, direct_urls_only: bool = False, enforce_result_limit: bool = True, url_progress_state=None) -> SourceResult:
        urls = _unique([_clean_text(url) for url in (career_urls or []) if detect_ats_platform_from_url(url) == self.name]) if direct_urls_only else self._candidate_urls(companies, career_urls)
        rows: List[Dict[str, str]] = []
        errors: List[str] = []
        scanned_urls: List[str] = []
        _emit(status_cb, "Scanning Ashby career pages.")
        for index, url in enumerate(urls, start=1):
            _emit_url_progress(status_cb, self.name, index, len(urls), url, progress_state=url_progress_state)
            company = self._company_from_url(url)
            company_slug = company or _slugify(url)
            try:
                if company_slug:
                    api_url = self._api_url(company_slug)
                    scanned_urls.append(api_url)
                    payload, _, _ = _fetch_json(api_url)
                    rows.extend(self._parse_api(company_slug, payload))
                else:
                    scanned_urls.append(url)
                    raise ValueError("Ashby slug not found")
            except Exception:
                try:
                    scanned_urls.append(url)
                    html_text, _, _ = _fetch_text(url)
                    rows.extend(self._parse_html(url, html_text, company_hint=company_slug))
                except Exception as exc:
                    errors.append(f"Ashby: {exc}")
        rows = self._filter_rows(rows, query, keywords, companies, locations)
        return SourceResult(self.name, _limit_rows(rows, limit_per_source, enforce_result_limit), scanned_urls or urls, errors)


class WorkdayAdapter(CareerSourceAdapter):
    name = "workday"
    platform = "workday"

    def _discover_params(self, board_url: str) -> Dict[str, str]:
        parsed = urllib.parse.urlparse(board_url)
        host_parts = [part for part in parsed.netloc.split(".") if part]
        tenant = host_parts[0] if host_parts else ""
        if not tenant:
            return {}
        path_parts = [part for part in parsed.path.split("/") if part]
        locale = path_parts[0] if path_parts and re.match(r"^[a-z]{2}-[A-Z]{2}$", path_parts[0]) else ""
        site = path_parts[1] if locale and len(path_parts) > 1 else (path_parts[0] if path_parts else "")
        if site:
            return {"origin": f"{parsed.scheme}://{parsed.netloc}", "tenant": tenant, "site": site, "locale": locale}
        html_text, _, _ = _fetch_text(board_url)
        job_link_patterns = [
            r"/([a-z]{2}[-_][A-Z]{2})/([^/]+)/job/",
            r"/([a-z]{2}[-_][A-Z]{2})/([^/]+)/details/",
            r'href=["\']/([a-z]{2}[-_][A-Z]{2})/([^/]+)/job/',
            r'href=["\']/([a-z]{2}[-_][A-Z]{2})/([^/]+)/details/',
        ]
        for pattern in job_link_patterns:
            match = re.search(pattern, html_text)
            if match:
                locale_value = match.group(1).replace("_", "-")
                return {
                    "origin": f"{parsed.scheme}://{parsed.netloc}",
                    "tenant": tenant,
                    "site": match.group(2),
                    "locale": locale_value,
                }
        site_match = (
            re.search(r'siteId:\s*"([^"]+)"', html_text)
            or re.search(r'"siteId"\s*:\s*"([^"]+)"', html_text)
            or re.search(r'"careerSiteId"\s*:\s*"([^"]+)"', html_text)
        )
        if site_match:
            return {"origin": f"{parsed.scheme}://{parsed.netloc}", "tenant": tenant, "site": site_match.group(1), "locale": locale or "en-US"}
        return {}

    def _fetch_api_rows(self, board_url: str, query: str = "") -> List[Dict[str, str]]:
        params = self._discover_params(board_url)
        if not params:
            return []
        api_url = f"{params['origin']}/wday/cxs/{params['tenant']}/{params['site']}/jobs"
        headers = {
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Origin": params["origin"],
            "Referer": board_url,
            "User-Agent": DEFAULT_USER_AGENT,
        }
        payload = {"appliedFacets": {}, "limit": 20, "offset": 0, "searchText": query or ""}
        initial = requests.post(api_url, headers=headers, json=payload, timeout=DEFAULT_TIMEOUT)
        initial.raise_for_status()
        data = initial.json() if initial.content else {}
        total = int(data.get("total") or 0)
        job_postings = list(data.get("jobPostings") or [])
        for offset in range(20, total, 20):
            page_payload = {"appliedFacets": {}, "limit": 20, "offset": offset, "searchText": query or ""}
            page = requests.post(api_url, headers=headers, json=page_payload, timeout=DEFAULT_TIMEOUT)
            if not page.ok:
                break
            page_data = page.json() if page.content else {}
            job_postings.extend(page_data.get("jobPostings") or [])
        company = _slugify(board_url)
        rows = []
        for item in job_postings:
            if not isinstance(item, dict):
                continue
            role = _clean_text(item.get("title"))
            if not role:
                continue
            external_path = _clean_text(item.get("externalPath"))
            link = external_path if external_path.startswith("http") else f"{params['origin']}{external_path if external_path.startswith('/') else '/' + external_path}" if external_path else board_url
            rows.append(
                _ensure_standard_row(
                    {
                        "Company": company,
                        "Platform": self.platform,
                        "Role": role,
                        "Location": _clean_text(item.get("locationsText") or ""),
                        "Date": _clean_text(item.get("postedOn") or item.get("postedOnDate") or ""),
                        "Primary Apply Link": link,
                        "Apply Links": link,
                        "Job Description": "",
                        "Post Text": _build_post_text(company, role, _clean_text(item.get("locationsText") or ""), "", self.platform),
                        "Post Link": link,
                        "Author Name": company or self.platform,
                        "All Links": link,
                    },
                    platform=self.platform,
                )
            )
        return rows

    def _parse_page(self, url: str, html_text: str, company_hint: str = "") -> List[Dict[str, str]]:
        rows = _jobpostings_from_json_ld(url, html_text, self.platform, company_hint=company_hint)
        if rows:
            return rows
        return _generic_job_cards_from_html(url, html_text, self.platform, company_hint=company_hint)

    def scan(self, query: str = "", keywords=None, companies=None, locations=None, career_urls=None, limit_per_source: int = DEFAULT_LIMIT_PER_SOURCE, max_pages: int = DEFAULT_MAX_PAGES, status_cb=None, direct_urls_only: bool = False, enforce_result_limit: bool = True, url_progress_state=None) -> SourceResult:
        urls = []
        for url in career_urls or []:
            if detect_ats_platform_from_url(url) == self.name:
                urls.append(url)
        if not urls and not direct_urls_only:
            for company in companies or []:
                slug = _slugify(company)
                if slug:
                    urls.extend(
                        [
                            f"https://{slug}.myworkdayjobs.com/en-US/{slug}",
                            f"https://{slug}.wd3.myworkdayjobs.com/en-US/{slug}",
                            f"https://{slug}.wd5.myworkdayjobs.com/en-US/{slug}",
                        ]
                    )
        urls = _unique(urls)
        rows: List[Dict[str, str]] = []
        errors: List[str] = []
        scanned_urls: List[str] = []
        _emit(status_cb, "Scanning Workday career pages.")
        for index, url in enumerate(urls, start=1):
            _emit_url_progress(status_cb, self.name, index, len(urls), url, progress_state=url_progress_state)
            scanned_urls.append(url)
            company = _slugify(url)
            try:
                page_rows = self._fetch_api_rows(url, query=query)
                if not page_rows:
                    html_text, _, _ = _fetch_text(url)
                    page_rows = self._parse_page(url, html_text, company_hint=company)
                if not page_rows:
                    try:
                        page_rows = _selenium_parse_job_page(url, self.platform, company_hint=company, status_cb=status_cb)
                    except Exception as exc:
                        errors.append(f"Workday Selenium: {exc}")
                rows.extend(page_rows)
            except Exception as exc:
                errors.append(f"Workday: {exc}")
                try:
                    rows.extend(_selenium_parse_job_page(url, self.platform, company_hint=company, status_cb=status_cb))
                except Exception as exc2:
                    errors.append(f"Workday Selenium: {exc2}")
        rows = self._filter_rows(rows, query, keywords, companies, locations)
        return SourceResult(self.name, _limit_rows(rows, limit_per_source, enforce_result_limit), scanned_urls or urls, errors)


class WorkableAdapter(CareerSourceAdapter):
    name = "workable"
    platform = "workable"

    def _slug_from_url(self, url: str) -> str:
        parsed = urllib.parse.urlparse(url)
        parts = [part for part in parsed.path.split("/") if part]
        if not parts:
            return ""
        if parts[0] == "j" and len(parts) > 1:
            return ""
        if parsed.netloc.endswith("jobs.workable.com") and parts[0] == "company" and len(parts) >= 3:
            return parts[-1]
        return parts[0]

    def _fetch_widget_rows(self, slug: str) -> List[Dict[str, str]]:
        api_url = f"https://apply.workable.com/api/v1/widget/accounts/{slug}"
        payload, _, _ = _fetch_json(api_url)
        jobs = []
        company_name = slug
        if isinstance(payload, dict):
            company_name = _clean_text(payload.get("name") or slug)
            jobs = payload.get("jobs") or payload.get("results") or payload.get("data") or []
        elif isinstance(payload, list):
            jobs = payload
        if not isinstance(jobs, list):
            return []
        rows = []
        for item in jobs:
            if not isinstance(item, dict):
                continue
            role = _clean_text(item.get("title"))
            if not role:
                continue
            shortcode = _clean_text(item.get("shortcode") or item.get("code"))
            location = _join_non_empty([item.get("city"), item.get("state"), item.get("country")], sep=", ")
            if not location and isinstance(item.get("locations"), list):
                formatted_locations = []
                for loc in item.get("locations") or []:
                    if not isinstance(loc, dict):
                        continue
                    formatted = _join_non_empty([loc.get("city"), loc.get("region"), loc.get("country")], sep=", ")
                    if formatted:
                        formatted_locations.append(formatted)
                location = "; ".join(formatted_locations)
            if item.get("telecommuting") is True:
                location = f"{location} (Remote)".strip() if location else "Remote"
            link = _clean_text(item.get("url") or item.get("shortlink") or item.get("application_url"))
            if not link and shortcode:
                link = f"https://apply.workable.com/{slug}/j/{shortcode}/"
            rows.append(
                _ensure_standard_row(
                    {
                        "Company": company_name,
                        "Platform": self.platform,
                        "Role": role,
                        "Location": location,
                        "Date": _clean_text(item.get("published_on") or item.get("created_at") or item.get("published")),
                        "Primary Apply Link": link,
                        "Apply Links": link,
                        "Job Description": _clean_text(item.get("description") or ""),
                        "Post Text": _build_post_text(company_name, role, location, _clean_text(item.get("description") or ""), self.platform),
                        "Post Link": link,
                        "Author Name": company_name or self.platform,
                        "All Links": link,
                    },
                    platform=self.platform,
                )
            )
        return rows

    def _fetch_api_rows(self, url: str) -> List[Dict[str, str]]:
        slug = self._slug_from_url(url)
        if not slug:
            return []
        widget_rows = self._fetch_widget_rows(slug)
        if widget_rows:
            return widget_rows
        api_url = f"https://apply.workable.com/api/v3/accounts/{slug}/jobs"
        headers = {
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Origin": "https://apply.workable.com",
            "Referer": f"https://apply.workable.com/{slug}",
            "User-Agent": DEFAULT_USER_AGENT,
        }
        payload = {"query": "", "location": [], "department": [], "worktype": [], "remote": []}
        response = requests.post(api_url, headers=headers, json=payload, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
        data = response.json() if response.content else {}
        jobs = list(data.get("results") or data.get("jobs") or [])
        next_page = data.get("nextPage")
        while next_page:
            page_payload = {"query": "", "location": [], "department": [], "worktype": [], "remote": [], "token": next_page}
            page = requests.post(api_url, headers=headers, json=page_payload, timeout=DEFAULT_TIMEOUT)
            if not page.ok:
                break
            page_data = page.json() if page.content else {}
            page_jobs = page_data.get("results") or []
            if not page_jobs:
                break
            jobs.extend(page_jobs)
            next_page = page_data.get("nextPage")
        rows = []
        for item in jobs:
            if not isinstance(item, dict):
                continue
            role = _clean_text(item.get("title"))
            shortcode = _clean_text(item.get("shortcode"))
            if not role or not shortcode:
                continue
            location_obj = item.get("location") if isinstance(item.get("location"), dict) else {}
            location = _join_non_empty([location_obj.get("city"), location_obj.get("region"), location_obj.get("country")], sep=", ")
            workplace = _clean_text(item.get("workplace"))
            if workplace == "remote":
                location = f"{location} (Remote)".strip() if location else "Remote"
            link = f"https://apply.workable.com/{slug}/j/{shortcode}/"
            rows.append(
                _ensure_standard_row(
                    {
                        "Company": slug,
                        "Platform": self.platform,
                        "Role": role,
                        "Location": location,
                        "Date": _clean_text(item.get("published") or item.get("published_on") or item.get("created_at")),
                        "Primary Apply Link": link,
                        "Apply Links": link,
                        "Job Description": "",
                        "Post Text": _build_post_text(slug, role, location, "", self.platform),
                        "Post Link": link,
                        "Author Name": slug or self.platform,
                        "All Links": link,
                    },
                    platform=self.platform,
                )
            )
        return rows

    def scan(self, query: str = "", keywords=None, companies=None, locations=None, career_urls=None, limit_per_source: int = DEFAULT_LIMIT_PER_SOURCE, max_pages: int = DEFAULT_MAX_PAGES, status_cb=None, direct_urls_only: bool = False, enforce_result_limit: bool = True, url_progress_state=None) -> SourceResult:
        urls = _unique([_clean_text(url) for url in (career_urls or []) if detect_ats_platform_from_url(url) == self.name])
        rows: List[Dict[str, str]] = []
        errors: List[str] = []
        scanned_urls: List[str] = []
        _emit(status_cb, "Scanning Workable job boards.")
        for index, url in enumerate(urls, start=1):
            _emit_url_progress(status_cb, self.name, index, len(urls), url, progress_state=url_progress_state)
            scanned_urls.append(url)
            try:
                rows.extend(self._fetch_api_rows(url))
            except Exception as exc:
                errors.append(f"Workable: {exc}")
        rows = self._filter_rows(rows, query, keywords, companies, locations)
        return SourceResult(self.name, _limit_rows(rows, limit_per_source, enforce_result_limit), scanned_urls or urls, errors)


class IcimsAdapter(CareerSourceAdapter):
    name = "icims"
    platform = "icims"

    def _search_url(self, url: str) -> str:
        parsed = urllib.parse.urlparse(url)
        query_items = dict(urllib.parse.parse_qsl(parsed.query, keep_blank_values=True))
        query_items["ss"] = query_items.get("ss") or "1"
        query_items["in_iframe"] = query_items.get("in_iframe") or "1"
        return urllib.parse.urlunparse(parsed._replace(path="/jobs/search", query=urllib.parse.urlencode(query_items), fragment=""))

    def _parse_jobs(self, page_url: str, html_text: str) -> List[Dict[str, str]]:
        soup = bs(html_text, "html.parser")
        rows: List[Dict[str, str]] = []
        seen = set()
        for anchor in soup.find_all("a", href=True):
            href = _normalize_url(anchor.get("href"), page_url)
            if "/jobs/" not in href:
                continue
            title = _clean_text(anchor.get_text(" "))
            if not title:
                title_node = anchor.find("h3")
                title = _clean_text(title_node.get_text(" ")) if title_node else ""
            if not title:
                continue
            container = anchor.find_parent(["div", "tr", "li", "article"]) or anchor
            snippet = _clean_text(container.get_text(" "))
            location_match = re.search(r"\b(remote|hybrid|onsite|bengaluru|bangalore|gurugram|gurgaon|noida|mumbai|pune|chennai|hyderabad|delhi|india)\b", snippet, flags=re.I)
            external_id_match = re.search(r"/jobs/(\d+)/", href)
            key = (title.lower(), href)
            if key in seen:
                continue
            seen.add(key)
            rows.append(
                _ensure_standard_row(
                    {
                        "Company": _slugify(page_url),
                        "Platform": self.platform,
                        "Role": title,
                        "Location": location_match.group(1) if location_match else "",
                        "Date": "",
                        "Primary Apply Link": href,
                        "Apply Links": href,
                        "Job Description": snippet[:500],
                        "Post Text": _build_post_text(_slugify(page_url), title, location_match.group(1) if location_match else "", snippet[:500], self.platform),
                        "Post Link": href,
                        "Author Name": _slugify(page_url) or self.platform,
                        "All Links": href + (f"; {external_id_match.group(1)}" if external_id_match else ""),
                    },
                    platform=self.platform,
                )
            )
        return rows

    def scan(self, query: str = "", keywords=None, companies=None, locations=None, career_urls=None, limit_per_source: int = DEFAULT_LIMIT_PER_SOURCE, max_pages: int = DEFAULT_MAX_PAGES, status_cb=None, direct_urls_only: bool = False, enforce_result_limit: bool = True, url_progress_state=None) -> SourceResult:
        urls = _unique([_clean_text(url) for url in (career_urls or []) if detect_ats_platform_from_url(url) == self.name])
        rows: List[Dict[str, str]] = []
        errors: List[str] = []
        scanned_urls: List[str] = []
        _emit(status_cb, "Scanning iCIMS job boards.")
        for index, url in enumerate(urls, start=1):
            _emit_url_progress(status_cb, self.name, index, len(urls), url, progress_state=url_progress_state)
            search_url = self._search_url(url)
            page_no = 0
            found_any = False
            while page_no < 25:
                paged_url = _url_with_query(search_url, {"pr": str(page_no)})
                scanned_urls.append(paged_url)
                try:
                    html_text, _, _ = _fetch_text(paged_url)
                    page_rows = self._parse_jobs(paged_url, html_text)
                except Exception as exc:
                    errors.append(f"iCIMS: {exc}")
                    break
                if not page_rows:
                    break
                found_any = True
                rows.extend(page_rows)
                page_no += 1
            if not found_any:
                try:
                    html_text, _, _ = _fetch_text(url)
                    rows.extend(self._parse_jobs(url, html_text))
                except Exception as exc:
                    errors.append(f"iCIMS fallback: {exc}")
        rows = self._filter_rows(rows, query, keywords, companies, locations)
        return SourceResult(self.name, _limit_rows(rows, limit_per_source, enforce_result_limit), scanned_urls or urls, errors)


class GenericCareerAdapter(CareerSourceAdapter):
    name = "generic"
    platform = "generic"

    def scan(self, query: str = "", keywords=None, companies=None, locations=None, career_urls=None, limit_per_source: int = DEFAULT_LIMIT_PER_SOURCE, max_pages: int = DEFAULT_MAX_PAGES, status_cb=None, direct_urls_only: bool = False, enforce_result_limit: bool = True, url_progress_state=None) -> SourceResult:
        supported_specific_sources = {"indeed", "naukri", "greenhouse", "lever", "smartrecruiters", "ashby", "workday", "workable", "icims"}
        urls = []
        for url in career_urls or []:
            platform_name = detect_ats_platform_from_url(url)
            if platform_name == "generic" or platform_name not in supported_specific_sources:
                urls.append(url)
        if not direct_urls_only:
            for company in companies or []:
                for url in discover_career_urls(company):
                    if detect_ats_platform_from_url(url) == "generic":
                        urls.append(url)
        urls = _unique(urls)
        rows: List[Dict[str, str]] = []
        errors: List[str] = []
        scanned_urls: List[str] = []
        selenium_fallbacks = 0
        selenium_budget = min(DEFAULT_INPUT_SELENIUM_BUDGET, len(urls)) if direct_urls_only else max(0, int(os.getenv("SCANNER_SELENIUM_FALLBACK_LIMIT", str(DEFAULT_SELENIUM_FALLBACK_LIMIT)) or DEFAULT_SELENIUM_FALLBACK_LIMIT))
        _emit(status_cb, "Scanning generic career pages.")
        for index, url in enumerate(urls, start=1):
            _emit_url_progress(status_cb, self.name, index, len(urls), url, progress_state=url_progress_state)
            platform = detect_ats_platform_from_url(url)
            company = _slugify(url)
            target_urls = _search_url_variants(url, query=query, keywords=keywords, locations=locations, platform_hint=platform, max_pages=max_pages)
            found_for_input = False
            for target_url in target_urls:
                scanned_urls.append(target_url)
                try:
                    html_text, _, _ = _fetch_text(target_url)
                    page_rows = _jobpostings_from_json_ld(target_url, html_text, platform, company_hint=company)
                    page_rows.extend(_generic_job_cards_from_html(target_url, html_text, platform, company_hint=company))
                    if page_rows:
                        found_for_input = True
                        rows.extend(page_rows)
                except Exception as exc:
                    errors.append(f"Generic: {exc}")
            if not found_for_input and selenium_fallbacks < selenium_budget:
                selenium_fallbacks += 1
                try:
                    rows.extend(_selenium_parse_job_page(url, platform, company_hint=company, status_cb=status_cb))
                except Exception as exc2:
                    errors.append(f"Generic Selenium: {exc2}")
        rows = self._filter_rows(rows, query, keywords, companies, locations)
        return SourceResult(self.name, _limit_rows(rows, limit_per_source, enforce_result_limit), scanned_urls or urls, errors)


def _adapter_registry() -> Dict[str, BaseSourceAdapter]:
    return {
        "indeed": IndeedAdapter(),
        "naukri": NaukriAdapter(),
        "greenhouse": GreenhouseAdapter(),
        "lever": LeverAdapter(),
        "smartrecruiters": SmartRecruitersAdapter(),
        "ashby": AshbyAdapter(),
        "workday": WorkdayAdapter(),
        "workable": WorkableAdapter(),
        "icims": IcimsAdapter(),
        "generic": GenericCareerAdapter(),
    }


def _resolve_source_names(source_names) -> List[str]:
    if source_names is None:
        return DEFAULT_SOURCE_NAMES[:]
    if isinstance(source_names, str):
        items = re.split(r"[,\n]+", source_names)
    else:
        items = list(source_names)
    names = []
    seen = set()
    for item in items:
        name = _clean_text(item).lower()
        if not name:
            continue
        if name == "all":
            return DEFAULT_SOURCE_NAMES[:]
        if name in seen:
            continue
        seen.add(name)
        names.append(name)
    return names or DEFAULT_SOURCE_NAMES[:]


def _scan_direct_input_urls(
    career_urls: List[str],
    query: str,
    keywords,
    companies,
    locations,
    source_names,
    limit_per_source: int,
    max_pages: int,
    status_cb=None,
) -> Tuple[pd.DataFrame, Dict[str, object]]:
    adapters = _adapter_registry()
    rows: List[Dict[str, str]] = []
    coverage: List[Dict[str, object]] = []
    source_counts: Dict[str, int] = {}
    source_errors: Dict[str, List[str]] = {}
    blocked_urls: List[Dict[str, str]] = []
    unsupported_urls: List[Dict[str, str]] = []
    resolved_targets: List[Dict[str, object]] = []
    scanned_target_set = set()

    def child_status_cb(message):
        text = str(message or "")
        if text.startswith("URL_PROGRESS::"):
            return
        _emit(status_cb, text)

    _emit(status_cb, "Preparing ATS-first URL scan.")

    for index, input_url in enumerate(career_urls, start=1):
        _emit_url_progress(status_cb, "input", index, len(career_urls), input_url)
        resolution = _resolve_input_targets(input_url, query=query, keywords=keywords, locations=locations, max_pages=max_pages)
        resolved = resolution.get("resolved_targets") or []
        blocked = resolution.get("blocked") or []
        unsupported = resolution.get("unsupported") or []
        targets = _unique(resolution.get("targets") or [])
        blocked_urls.extend(blocked)
        unsupported_urls.extend(unsupported)
        resolved_targets.extend(resolved)

        input_rows = 0
        input_errors: List[str] = []
        scanned_targets_for_input: List[str] = []

        for target_url in targets:
            platform = detect_ats_platform_from_url(target_url)
            adapter = adapters.get(platform) or adapters["generic"]
            try:
                result = adapter.scan(
                    query=query,
                    keywords=keywords,
                    companies=companies,
                    locations=locations,
                    career_urls=[target_url],
                    limit_per_source=0,
                    max_pages=max_pages,
                    status_cb=child_status_cb,
                    direct_urls_only=True,
                    enforce_result_limit=False,
                )
                rows.extend(result.rows)
                input_rows += len(result.rows)
                scanned_targets_for_input.extend(result.scanned_urls or [target_url])
                scanned_target_set.add(target_url.lower())
                for error in result.errors:
                    source_errors.setdefault(adapter.name, []).append(error)
            except Exception as exc:
                error_text = str(exc)
                input_errors.append(error_text)
                source_errors.setdefault(adapter.name, []).append(error_text)

        coverage.append(
            {
                "input_url": input_url,
                "status": "ok" if input_rows else ("blocked" if blocked else "unsupported" if unsupported else "empty"),
                "count": input_rows,
                "resolved_targets": targets,
                "scanned_urls": scanned_targets_for_input,
                "errors": input_errors + [item.get("reason", "") for item in blocked + unsupported],
            }
        )

    for row in rows:
        source_name = _clean_text(row.get("Platform")).lower() or "generic"
        source_counts[source_name] = source_counts.get(source_name, 0) + 1

    normalized_rows = [_ensure_standard_row(row, platform=_clean_text(row.get("Platform"))) for row in rows]
    df = _rows_to_dataframe(normalized_rows)
    if not df.empty:
        df = df.drop_duplicates(subset=["Company", "Role", "Location", "Primary Apply Link", "Post Link"], keep="first").reset_index(drop=True)

    meta = {
        "generated_at": _now_iso(),
        "query": query,
        "keywords": keywords,
        "companies": companies,
        "locations": locations,
        "career_urls": career_urls,
        "source_names": source_names,
        "direct_urls_only": True,
        "source_counts": source_counts,
        "source_errors": source_errors,
        "coverage": coverage,
        "row_count": int(len(df)),
        "normalized_columns": STANDARD_COLUMNS[:],
        "resolved_targets": resolved_targets,
        "blocked_urls": blocked_urls,
        "unsupported_urls": unsupported_urls,
        "unsupported_count": len(blocked_urls) + len(unsupported_urls),
        "resolved_url_count": len(scanned_target_set),
    }
    return df, meta


def scan_universal_jobs(
    query: str = "",
    keywords=None,
    companies=None,
    locations=None,
    career_urls=None,
    source_names=None,
    limit_per_source: int = DEFAULT_LIMIT_PER_SOURCE,
    max_pages: int = DEFAULT_MAX_PAGES,
    status_cb=None,
    direct_urls_only: bool = False,
) -> Tuple[pd.DataFrame, Dict[str, object]]:
    query = _clean_text(query)
    keywords = _split_text_list(keywords)
    companies = _split_text_list(companies)
    locations = _split_text_list(locations)
    career_urls = _unique([_clean_text(url) for url in (career_urls or []) if _clean_text(url)])
    if career_urls:
        career_urls = _unique([_canonicalize_ats_url(url) or url for url in career_urls if _clean_text(url)])
    source_names = _resolve_source_names(source_names)

    if direct_urls_only and career_urls:
        return _scan_direct_input_urls(
            career_urls=career_urls,
            query=query,
            keywords=keywords,
            companies=companies,
            locations=locations,
            source_names=source_names,
            limit_per_source=limit_per_source,
            max_pages=max_pages,
            status_cb=status_cb,
        )

    adapters = _adapter_registry()
    rows: List[Dict[str, str]] = []
    coverage: List[Dict[str, object]] = []
    source_counts: Dict[str, int] = {}
    source_errors: Dict[str, List[str]] = {}
    url_progress_state = {"count": 0, "total": len(career_urls)} if direct_urls_only and career_urls else None

    _emit(status_cb, "Preparing universal job scan.")

    for source_name in source_names:
        adapter = adapters.get(source_name)
        if not adapter:
            coverage.append({"source": source_name, "status": "skipped", "count": 0, "errors": ["Unsupported source"]})
            continue
        try:
            _emit(status_cb, f"{source_name.title()} scan started.")
            result = adapter.scan(
                query=query,
                keywords=keywords,
                companies=companies,
                locations=locations,
                career_urls=career_urls,
                limit_per_source=limit_per_source,
                max_pages=max_pages,
                status_cb=status_cb,
                direct_urls_only=direct_urls_only,
                enforce_result_limit=not direct_urls_only,
                url_progress_state=url_progress_state,
            )
            source_counts[source_name] = len(result.rows)
            source_errors[source_name] = result.errors[:]
            rows.extend(result.rows)
            coverage.append(
                {
                    "source": source_name,
                    "status": "ok" if result.rows else "empty",
                    "count": len(result.rows),
                    "scanned_urls": result.scanned_urls,
                    "errors": result.errors,
                }
            )
            _emit(status_cb, f"{source_name.title()} yielded {len(result.rows)} jobs.")
        except Exception as exc:
            source_counts[source_name] = 0
            source_errors[source_name] = [str(exc)]
            coverage.append({"source": source_name, "status": "error", "count": 0, "errors": [str(exc)]})

    normalized_rows = []
    for row in rows:
        normalized_rows.append(_ensure_standard_row(row, platform=_clean_text(row.get("Platform"))))

    df = _rows_to_dataframe(normalized_rows)
    if not df.empty:
        df = df.drop_duplicates(subset=["Company", "Role", "Location", "Primary Apply Link", "Post Link"], keep="first").reset_index(drop=True)

    meta = {
        "generated_at": _now_iso(),
        "query": query,
        "keywords": keywords,
        "companies": companies,
        "locations": locations,
        "career_urls": career_urls,
        "source_names": source_names,
        "direct_urls_only": bool(direct_urls_only),
        "source_counts": source_counts,
        "source_errors": source_errors,
        "coverage": coverage,
        "row_count": int(len(df)),
        "normalized_columns": STANDARD_COLUMNS[:],
        "resolved_targets": [],
        "blocked_urls": [],
        "unsupported_urls": [],
        "unsupported_count": 0,
        "resolved_url_count": 0,
    }
    return df, meta


__all__ = [
    "STANDARD_COLUMNS",
    "DEFAULT_SOURCE_NAMES",
    "detect_ats_platform_from_url",
    "discover_career_urls",
    "scan_universal_jobs",
]

# === app.py (inlined) ===
from flask import Flask, render_template, request, send_file, abort, redirect, url_for, jsonify
from jinja2 import DictLoader
from werkzeug.utils import secure_filename
from pathlib import Path
import re
import os
import time
import csv
import html
import hashlib
from datetime import datetime
import threading
import uuid
import smtplib
import mimetypes
import json
import urllib.parse
import urllib.request
import urllib.error
from email.message import EmailMessage
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import base64
from dotenv import load_dotenv

import pandas as pd
from bs4 import BeautifulSoup as bs
from PyPDF2 import PdfReader
import docx as docx_lib
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from dateutil.relativedelta import relativedelta

APP_ROOT = Path(__file__).parent
OUTPUT_DIR = APP_ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)
RESUME_DIR = OUTPUT_DIR / "resume_reviews"
RESUME_DIR.mkdir(exist_ok=True)
LINKEDIN_DIR = OUTPUT_DIR / "linkedin_reviews"
LINKEDIN_DIR.mkdir(exist_ok=True)
AUTO_APPLY_DIR = OUTPUT_DIR / "auto_apply"
AUTO_APPLY_DIR.mkdir(exist_ok=True)
AUTO_APPLY_SETTINGS_PATH = AUTO_APPLY_DIR / "settings.json"
AUTO_APPLY_HISTORY_PATH = AUTO_APPLY_DIR / "history.json"
AUTO_APPLY_RUNS_DIR = AUTO_APPLY_DIR / "runs"
AUTO_APPLY_RUNS_DIR.mkdir(exist_ok=True)
AUTO_APPLY_EXEC_DIR = AUTO_APPLY_DIR / "executions"
AUTO_APPLY_EXEC_DIR.mkdir(exist_ok=True)

load_dotenv(APP_ROOT / ".env")

TRACKING_BASE_URL = os.getenv("TRACKING_BASE_URL", "").strip().rstrip("/")
TRACKING_LOG_DIR = OUTPUT_DIR / "email_tracking"
TRACKING_LOG_DIR.mkdir(exist_ok=True)

EMAIL_REGEX_STRICT = r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,24}"
COMMON_TLDS = {
    "com","net","org","edu","gov","in","co","io","ai","us","uk","ca","au","sg","ae","de","fr","it","nl","se","no",
    "ch","jp","kr","cn","hk","me","info","biz","jobs","work","app","dev","bank","tech",
}
LONG_TLDS = {"company","careers","technology","solutions","consulting","finance","systems","digital","industries","services"}
APPLY_HINTS = [
    "apply",
    "job",
    "jobs",
    "career",
    "careers",
    "workday",
    "greenhouse",
    "lever",
    "icims",
    "smartrecruiters",
    "successfactors",
    "taleo",
    "oraclecloud",
    "recruit",
    "join-us",
]

COMMON_JOB_LOCATIONS = [
    "remote", "hybrid", "onsite", "work from home", "india",
    "bengaluru", "bangalore", "gurugram", "gurgaon", "delhi", "noida",
    "mumbai", "pune", "chennai", "hyderabad", "kolkata", "ahmedabad",
    "surat", "jaipur", "lucknow", "kochi", "coimbatore", "indore",
]

SCAN_EXPORT_COLUMNS = [
    "Company",
    "Platform",
    "Role",
    "Location",
    "Date",
    "Primary Apply Link",
    "Apply Links",
    "Job Description",
    "Post Text",
    "Post Link",
    "Author Name",
    "Emails",
    "Phone Numbers",
    "All Links",
    "Quality Score",
    "Quality Reasons",
    "Quality",
]

UNIVERSAL_SCAN_SOURCE_NAMES = [
    "Indeed",
    "Naukri",
    "Greenhouse",
    "Lever",
    "SmartRecruiters",
    "Ashby",
    "Workday",
    "Workable",
    "iCIMS",
    "Generic",
]

PUBLIC_ATS_FEED_URL = "https://storage.stapply.ai/jobs.csv"
PUBLIC_ATS_CACHE_PATH = OUTPUT_DIR / "ats_public_jobs.csv"
PUBLIC_ATS_CACHE_TTL_SECONDS = int(os.getenv("PUBLIC_ATS_CACHE_TTL_SECONDS", "21600"))
COMPILER_DATA_SOURCES = {
    "internal": "Native ATS scan",
    "public_ats": "Public ATS feed (stapply-ai)",
}
COMPILER_EXPORTS = {
    "career_feed": "Career-site feed JSON",
    "atlas": "Atlas map JSON",
}

AUTO_APPLY_SCAN_STRATEGIES = {
    "one_on_all": {
        "label": "All saved URLs",
        "description": "Default scanner mode. It scans every saved URL one by one, including Indeed and Naukri.",
        "sources": [],
        "use_reference_urls": False,
        "direct_urls_only": True,
    },
}
DEFAULT_AUTO_APPLY_SCAN_STRATEGY = "one_on_all"
AUTO_APPLY_SUPPORTED_SOURCES = ["indeed", "naukri", "greenhouse", "lever", "smartrecruiters", "ashby", "workday", "workable", "icims", "generic"]

EMBEDDED_TEMPLATES_B64 = {"auto_apply.html":"eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBjb250ZW50ICV9CiAgPGRpdiBjbGFzcz0icGFnZSI+CiAgICA8aGVhZGVyIGNsYXNzPSJoZWFkZXIiPgogICAgICA8ZGl2IGNsYXNzPSJpY29uLWJhZGdlIj4KICAgICAgICA8c3ZnIHdpZHRoPSIyNiIgaGVpZ2h0PSIyNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgIDxwYXRoIGQ9Ik01IDdoMTR2MTFINVY3eiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICAgIDxwYXRoIGQ9Ik05IDdWNWg2djIiIHN0cm9rZT0id2hpdGUiIHN0cm9rZS13aWR0aD0iMS42IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz4KICAgICAgICAgIDxwYXRoIGQ9Ik04IDExaDhNOCAxNGg1IiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjEuNiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIi8+CiAgICAgICAgPC9zdmc+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2PgogICAgICAgIDxoMT5BdXRvIEpvYiBBcHBseTwvaDE+CiAgICAgICAgPHAgY2xhc3M9InN1YnRpdGxlIj5TY2FubmVyLCBhcHBsaWVyLCBwYXN0IHNjYW5zLCBhbmQgYSBzaW1wbGUgdmlldyBvZiB3aGF0IHdhcyBmb3VuZCBhbmQgYXBwbGllZC48L3A+CiAgICAgIDwvZGl2PgogICAgPC9oZWFkZXI+CgogICAgeyUgaWYgbWVzc2FnZSAlfQogICAgICA8ZGl2IGNsYXNzPSJzdGF0dXMgZG9uZSI+e3sgbWVzc2FnZSB9fTwvZGl2PgogICAgeyUgZW5kaWYgJX0KICAgIHslIGlmIGVycm9yICV9CiAgICAgIDxkaXYgY2xhc3M9InN0YXR1cyBlcnJvciI+e3sgZXJyb3IgfX08L2Rpdj4KICAgIHslIGVuZGlmICV9CgogICAgPGRpdiBjbGFzcz0ic3RhdHMtZ3JpZCBhdXRvLXN1bW1hcnktZ3JpZCI+CiAgICAgIDxkaXYgY2xhc3M9InN0YXQiPgogICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LWxhYmVsIj5Gb3VuZCBpbiBsYXRlc3Qgc2Nhbjwvc3Bhbj4KICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC12YWx1ZSI+e3sgd29ya3NwYWNlX21ldHJpY3MubGF0ZXN0X3NjYW5fZm91bmQgfX08L3NwYW4+CiAgICAgICAgPHNwYW4gY2xhc3M9Im5vdGUiPnt7IHdvcmtzcGFjZV9tZXRyaWNzLmxhdGVzdF9zY2FuX3RpbWUgb3IgIk5vIHNjYW4geWV0IiB9fTwvc3Bhbj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9InN0YXQiPgogICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LWxhYmVsIj5TaG9ydGxpc3RlZDwvc3Bhbj4KICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC12YWx1ZSI+e3sgd29ya3NwYWNlX21ldHJpY3MubGF0ZXN0X3J1bl9zaG9ydGxpc3RlZCB9fTwvc3Bhbj4KICAgICAgICA8c3BhbiBjbGFzcz0ibm90ZSI+e3sgc3VtbWFyeS5sYXN0X3J1bl9zdGF0dXMgfX08L3NwYW4+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJzdGF0Ij4KICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC1sYWJlbCI+QXBwbGllZDwvc3Bhbj4KICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC12YWx1ZSI+e3sgd29ya3NwYWNlX21ldHJpY3Muc3VibWl0dGVkX3RvdGFsIH19PC9zcGFuPgogICAgICAgIDxzcGFuIGNsYXNzPSJub3RlIj57eyB3b3Jrc3BhY2VfbWV0cmljcy5sYXN0X2FwcGx5X3RpbWUgb3IgIk5vIGV4ZWN1dGlvbiB5ZXQiIH19PC9zcGFuPgogICAgICA8L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0ic3RhdCI+CiAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPlNhdmVkIHNjYW5zPC9zcGFuPgogICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LXZhbHVlIj57eyB3b3Jrc3BhY2VfbWV0cmljcy5zYXZlZF9zY2FucyB9fTwvc3Bhbj4KICAgICAgICA8c3BhbiBjbGFzcz0ibm90ZSI+e3sgd29ya3NwYWNlX21ldHJpY3Muc2F2ZWRfcnVucyB9fSBzYXZlZCBhcHBseSBydW5zPC9zcGFuPgogICAgICA8L2Rpdj4KICAgIDwvZGl2PgoKICAgIDxzZWN0aW9uIGNsYXNzPSJjYXJkIiBpZD0ic2Nhbm5lciI+CiAgICAgIDxkaXYgY2xhc3M9ImNhcmQtaGVhZCI+CiAgICAgICAgPGgzPlNjYW5uZXI8L2gzPgogICAgICAgIDxzcGFuIGNsYXNzPSJwaWxsIj5BbGwgU2F2ZWQgVVJMczwvc3Bhbj4KICAgICAgPC9kaXY+CiAgICAgIDxwIGNsYXNzPSJub3RlIj5UaGlzIHNjYW5uZXIgYWx3YXlzIHVzZXMgdGhlIHNhdmVkIFVSTCBiYXRjaCBhbmQgd2Fsa3MgdGhlIGZ1bGwgbGlzdCBvbmUgYnkgb25lLCByZXNvbHZpbmcgY29tcGFueSBjYXJlZXIgcGFnZXMgaW50byByZWFsIGpvYiBib2FyZHMgd2hlcmUgcG9zc2libGUgYW5kIHBsYWNpbmcgYmxvY2tlZCBvciB1bnN1cHBvcnRlZCBVUkxzIGludG8gYSBtYW51YWwgcmV2aWV3IGxpc3QuPC9wPgogICAgICB7JSBpZiBzYXZlZF9zY2FuX3VybF9jb3VudCAlfQogICAgICAgIDxwIGNsYXNzPSJub3RlIj5TYXZlZCBVUkwgYmF0Y2ggZGV0ZWN0ZWQ6IHt7IHNhdmVkX3NjYW5fdXJsX2NvdW50IH19IFVSTHMuIFJ1biBTY2FuIHdpbGwgcmV1c2UgdGhpcyBsaXN0IGF1dG9tYXRpY2FsbHkuPC9wPgogICAgICB7JSBlbmRpZiAlfQoKICAgICAgPGZvcm0gbWV0aG9kPSJwb3N0IiBhY3Rpb249Int7IHVybF9mb3IoJ2F1dG9fYXBwbHlfc2Nhbl9zdGFydCcpIH19IiBjbGFzcz0ic3RhZ2dlciI+CiAgICAgICAgPGRpdiBjbGFzcz0iZ3JpZCB0d28iPgogICAgICAgICAgPGRpdiBjbGFzcz0iZmllbGQiPgogICAgICAgICAgICA8bGFiZWwgZm9yPSJzY2FuX3F1ZXJ5Ij5TZWFyY2ggcXVlcnk8L2xhYmVsPgogICAgICAgICAgICA8aW5wdXQgaWQ9InNjYW5fcXVlcnkiIG5hbWU9InNjYW5fcXVlcnkiIHR5cGU9InRleHQiIHZhbHVlPSJ7eyBzY2FuX2RlZmF1bHRzLnF1ZXJ5IH19IiBwbGFjZWhvbGRlcj0icHJvZ3JhbSBtYW5hZ2VyIiAvPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJmaWVsZCI+CiAgICAgICAgICAgIDxsYWJlbCBmb3I9InNjYW5fbG9jYXRpb25zIj5Mb2NhdGlvbnM8L2xhYmVsPgogICAgICAgICAgICA8aW5wdXQgaWQ9InNjYW5fbG9jYXRpb25zIiBuYW1lPSJzY2FuX2xvY2F0aW9ucyIgdHlwZT0idGV4dCIgdmFsdWU9Int7IHNjYW5fZGVmYXVsdHMubG9jYXRpb25zIH19IiBwbGFjZWhvbGRlcj0iQmVuZ2FsdXJ1LCBHdXJ1Z3JhbSwgUmVtb3RlIiAvPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImdyaWQgdHdvIj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImZpZWxkIj4KICAgICAgICAgICAgPGxhYmVsIGZvcj0ic2Nhbl9rZXl3b3JkcyI+S2V5d29yZHM8L2xhYmVsPgogICAgICAgICAgICA8aW5wdXQgaWQ9InNjYW5fa2V5d29yZHMiIG5hbWU9InNjYW5fa2V5d29yZHMiIHR5cGU9InRleHQiIHZhbHVlPSJ7eyBzY2FuX2RlZmF1bHRzLmtleXdvcmRzIH19IiBwbGFjZWhvbGRlcj0ic3RyYXRlZ3ksIG9wZXJhdGlvbnMsIHByb2R1Y3QiIC8+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImZpZWxkIj4KICAgICAgICAgICAgPGxhYmVsIGZvcj0ic2Nhbl9jb21wYW5pZXMiPkNvbXBhbmllczwvbGFiZWw+CiAgICAgICAgICAgIDxpbnB1dCBpZD0ic2Nhbl9jb21wYW5pZXMiIG5hbWU9InNjYW5fY29tcGFuaWVzIiB0eXBlPSJ0ZXh0IiB2YWx1ZT0ie3sgc2Nhbl9kZWZhdWx0cy5jb21wYW5pZXMgfX0iIHBsYWNlaG9sZGVyPSJBZG9iZSwgQWlydGVsLCBNYXN0ZXJjYXJkIiAvPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImZpZWxkIj4KICAgICAgICAgIDxsYWJlbCBmb3I9InNjYW5fdXJscyI+VVJMcyB0byBzY2FuIG9uZSBieSBvbmU8L2xhYmVsPgogICAgICAgICAgPHRleHRhcmVhIGlkPSJzY2FuX3VybHMiIG5hbWU9InNjYW5fdXJscyIgcm93cz0iNiIgcGxhY2Vob2xkZXI9IlBhc3RlIGpvYiBwb3J0YWwgYW5kIGNvbXBhbnkgY2FyZWVyIFVSTHMgaGVyZSwgb25lIHBlciBsaW5lLiI+e3sgc2Nhbl9kZWZhdWx0cy51cmxzIH19PC90ZXh0YXJlYT4KICAgICAgICAgIDxwIGNsYXNzPSJub3RlIj5QYXN0ZSBhcyBtYW55IFVSTHMgYXMgeW91IHdhbnQuIFRoZSBzY2FubmVyIHdhbGtzIHRoZSBmdWxsIHNhdmVkIGxpc3QgaW5kaXZpZHVhbGx5IGFuZCBkb2VzIG5vdCBjYXAgVVJMIGNvdW50LjwvcD4KICAgICAgICA8L2Rpdj4KCiAgICAgICAgPGRpdiBjbGFzcz0iZmllbGQiPgogICAgICAgICAgPGxhYmVsIGZvcj0ic2Nhbl9saW1pdF9wZXJfc291cmNlIj5Kb2JzIHBlciBzb3VyY2U8L2xhYmVsPgogICAgICAgICAgPGlucHV0IGlkPSJzY2FuX2xpbWl0X3Blcl9zb3VyY2UiIG5hbWU9InNjYW5fbGltaXRfcGVyX3NvdXJjZSIgdHlwZT0ibnVtYmVyIiBtaW49IjUiIHN0ZXA9IjUiIHZhbHVlPSJ7eyBzY2FuX2RlZmF1bHRzLmxpbWl0X3Blcl9zb3VyY2UgfX0iIC8+CiAgICAgICAgICA8cCBjbGFzcz0ibm90ZSI+VVJMIGNvdW50IGlzIG5vdCBjYXBwZWQuIFRoZSBzY2FubmVyIHN0aWxsIHdhbGtzIHRoZSBmdWxsIHNhdmVkIGxpc3Qgb25lIGJ5IG9uZS48L3A+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InNjYW5fc3RyYXRlZ3kiIHZhbHVlPSJvbmVfb25fYWxsIiAvPgogICAgICAgIDxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InNjYW5fbWF4X3BhZ2VzIiB2YWx1ZT0ie3sgc2Nhbl9kZWZhdWx0cy5tYXhfcGFnZXMgfX0iIC8+CgogICAgICAgIDxkaXYgY2xhc3M9ImFjdGlvbnMiPgogICAgICAgICAgPGJ1dHRvbiBjbGFzcz0iYnRuIiB0eXBlPSJzdWJtaXQiPlJ1biBTY2FuPC9idXR0b24+CiAgICAgICAgPC9kaXY+CiAgICAgIDwvZm9ybT4KICAgIDwvc2VjdGlvbj4KCiAgICA8Zm9ybSBtZXRob2Q9InBvc3QiIGNsYXNzPSJhdXRvLWFwcGx5LWZvcm0iPgogICAgICA8c2VjdGlvbiBjbGFzcz0iY2FyZCIgaWQ9ImFwcGxpZXIiIHN0eWxlPSJtYXJnaW4tdG9wOiAxOHB4OyI+CiAgICAgICAgPGRpdiBjbGFzcz0iY2FyZC1oZWFkIj4KICAgICAgICAgIDxoMz5BcHBsaWVyPC9oMz4KICAgICAgICAgIDxzcGFuIGNsYXNzPSJwaWxsIj57eyBzdW1tYXJ5LnJlYWR5X3BsYXRmb3JtcyB9fSAvIHt7IHN1bW1hcnkuYWN0aXZlX3BsYXRmb3JtcyB9fSByZWFkeTwvc3Bhbj4KICAgICAgICA8L2Rpdj4KICAgICAgICA8cCBjbGFzcz0ibm90ZSI+VGhpcyBydW5zIGFnYWluc3QgdGhlIGxhdGVzdCBwcmVmZXJyZWQtam9icyBzY2FuLiBPbmx5IHRoZSBmaWVsZHMgbmVlZGVkIHRvIHNob3J0bGlzdCBhbmQgcHJlZmlsbCBhcHBsaWNhdGlvbnMgYXJlIHNob3duIGhlcmUuPC9wPgoKICAgICAgICA8ZGl2IGNsYXNzPSJncmlkIHR3byI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJmaWVsZCI+CiAgICAgICAgICAgIDxsYWJlbCBmb3I9InJvbGVzIj5Sb2xlczwvbGFiZWw+CiAgICAgICAgICAgIDx0ZXh0YXJlYSBpZD0icm9sZXMiIG5hbWU9InJvbGVzIiByb3dzPSIzIiBwbGFjZWhvbGRlcj0iUHJvZ3JhbSBNYW5hZ2VyLCBQcm9kdWN0IE9wZXJhdGlvbnMgTWFuYWdlciI+e3sgc2V0dGluZ3Muc2VhcmNoLnJvbGVzfGpvaW4oJywgJykgfX08L3RleHRhcmVhPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJmaWVsZCI+CiAgICAgICAgICAgIDxsYWJlbCBmb3I9ImtleXdvcmRzIj5LZXl3b3JkczwvbGFiZWw+CiAgICAgICAgICAgIDx0ZXh0YXJlYSBpZD0ia2V5d29yZHMiIG5hbWU9ImtleXdvcmRzIiByb3dzPSIzIiBwbGFjZWhvbGRlcj0ib3BlcmF0aW9ucywgc3RyYXRlZ3ksIGRlbGl2ZXJ5Ij57eyBzZXR0aW5ncy5zZWFyY2gua2V5d29yZHN8am9pbignLCAnKSB9fTwvdGV4dGFyZWE+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICA8L2Rpdj4KCiAgICAgICAgPGRpdiBjbGFzcz0iZ3JpZCB0d28iPgogICAgICAgICAgPGRpdiBjbGFzcz0iZmllbGQiPgogICAgICAgICAgICA8bGFiZWwgZm9yPSJjb21wYW5pZXMiPlRhcmdldCBjb21wYW5pZXM8L2xhYmVsPgogICAgICAgICAgICA8dGV4dGFyZWEgaWQ9ImNvbXBhbmllcyIgbmFtZT0iY29tcGFuaWVzIiByb3dzPSIzIiBwbGFjZWhvbGRlcj0iQWRvYmUsIEFpcnRlbCwgTWFzdGVyY2FyZCI+e3sgc2V0dGluZ3Muc2VhcmNoLmNvbXBhbmllc3xqb2luKCcsICcpIH19PC90ZXh0YXJlYT4KICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPGRpdiBjbGFzcz0iZmllbGQiPgogICAgICAgICAgICA8bGFiZWwgZm9yPSJsb2NhdGlvbnMiPkxvY2F0aW9uczwvbGFiZWw+CiAgICAgICAgICAgIDx0ZXh0YXJlYSBpZD0ibG9jYXRpb25zIiBuYW1lPSJsb2NhdGlvbnMiIHJvd3M9IjMiIHBsYWNlaG9sZGVyPSJCZW5nYWx1cnUsIFJlbW90ZSI+e3sgc2V0dGluZ3Muc2VhcmNoLmxvY2F0aW9uc3xqb2luKCcsICcpIH19PC90ZXh0YXJlYT4KICAgICAgICAgIDwvZGl2PgogICAgICAgIDwvZGl2PgoKICAgICAgICA8ZGl2IGNsYXNzPSJncmlkIHR3byI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJmaWVsZCI+CiAgICAgICAgICAgIDxsYWJlbCBmb3I9ImZ1bGxfbmFtZSI+RnVsbCBuYW1lPC9sYWJlbD4KICAgICAgICAgICAgPGlucHV0IGlkPSJmdWxsX25hbWUiIG5hbWU9ImZ1bGxfbmFtZSIgdHlwZT0idGV4dCIgdmFsdWU9Int7IHNldHRpbmdzLnByb2ZpbGUuZnVsbF9uYW1lIH19IiBwbGFjZWhvbGRlcj0iVmFpYmhhdiBLYXBvb3IiIC8+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImZpZWxkIj4KICAgICAgICAgICAgPGxhYmVsIGZvcj0iZW1haWwiPkVtYWlsPC9sYWJlbD4KICAgICAgICAgICAgPGlucHV0IGlkPSJlbWFpbCIgbmFtZT0iZW1haWwiIHR5cGU9InRleHQiIHZhbHVlPSJ7eyBzZXR0aW5ncy5wcm9maWxlLmVtYWlsIH19IiBwbGFjZWhvbGRlcj0idmFpYmhhdkBleGFtcGxlLmNvbSIgLz4KICAgICAgICAgIDwvZGl2PgogICAgICAgIDwvZGl2PgoKICAgICAgICA8ZGl2IGNsYXNzPSJncmlkIHR3byI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJmaWVsZCI+CiAgICAgICAgICAgIDxsYWJlbCBmb3I9InBob25lIj5QaG9uZTwvbGFiZWw+CiAgICAgICAgICAgIDxpbnB1dCBpZD0icGhvbmUiIG5hbWU9InBob25lIiB0eXBlPSJ0ZXh0IiB2YWx1ZT0ie3sgc2V0dGluZ3MucHJvZmlsZS5waG9uZSB9fSIgcGxhY2Vob2xkZXI9Iis5MSA5OFhYWFhYWFhYIiAvPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJmaWVsZCI+CiAgICAgICAgICAgIDxsYWJlbCBmb3I9ImN1cnJlbnRfbG9jYXRpb24iPkN1cnJlbnQgbG9jYXRpb248L2xhYmVsPgogICAgICAgICAgICA8aW5wdXQgaWQ9ImN1cnJlbnRfbG9jYXRpb24iIG5hbWU9ImN1cnJlbnRfbG9jYXRpb24iIHR5cGU9InRleHQiIHZhbHVlPSJ7eyBzZXR0aW5ncy5wcm9maWxlLmN1cnJlbnRfbG9jYXRpb24gfX0iIHBsYWNlaG9sZGVyPSJCZW5nYWx1cnUsIEluZGlhIiAvPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImdyaWQgdHdvIj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImZpZWxkIj4KICAgICAgICAgICAgPGxhYmVsIGZvcj0ieWVhcnNfZXhwZXJpZW5jZSI+WWVhcnMgb2YgZXhwZXJpZW5jZTwvbGFiZWw+CiAgICAgICAgICAgIDxpbnB1dCBpZD0ieWVhcnNfZXhwZXJpZW5jZSIgbmFtZT0ieWVhcnNfZXhwZXJpZW5jZSIgdHlwZT0idGV4dCIgdmFsdWU9Int7IHNldHRpbmdzLnByb2ZpbGUueWVhcnNfZXhwZXJpZW5jZSB9fSIgcGxhY2Vob2xkZXI9IjMiIC8+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImZpZWxkIj4KICAgICAgICAgICAgPGxhYmVsIGZvcj0ibGlua2VkaW5fdXJsIj5MaW5rZWRJbiBVUkw8L2xhYmVsPgogICAgICAgICAgICA8aW5wdXQgaWQ9ImxpbmtlZGluX3VybCIgbmFtZT0ibGlua2VkaW5fdXJsIiB0eXBlPSJ0ZXh0IiB2YWx1ZT0ie3sgc2V0dGluZ3MucHJvZmlsZS5saW5rZWRpbl91cmwgfX0iIHBsYWNlaG9sZGVyPSJodHRwczovL3d3dy5saW5rZWRpbi5jb20vaW4vLi4uIiAvPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImZpZWxkIj4KICAgICAgICAgIDxsYWJlbCBmb3I9InN1bW1hcnkiPlNob3J0IHN1bW1hcnk8L2xhYmVsPgogICAgICAgICAgPHRleHRhcmVhIGlkPSJzdW1tYXJ5IiBuYW1lPSJzdW1tYXJ5IiByb3dzPSI0IiBwbGFjZWhvbGRlcj0iVXNlZCBmb3IgcHJlZmlsbCBhbmQgY292ZXItbGV0dGVyIHN0eWxlIGZpZWxkcy4iPnt7IHNldHRpbmdzLnByb2ZpbGUuc3VtbWFyeSB9fTwvdGV4dGFyZWE+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImdyaWQgdHdvIj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImZpZWxkIj4KICAgICAgICAgICAgPGxhYmVsIGZvcj0ibWF4X2FwcGxpY2F0aW9uc19wZXJfcnVuIj5NYXggYXBwbGljYXRpb25zIHBlciBydW48L2xhYmVsPgogICAgICAgICAgICA8aW5wdXQgaWQ9Im1heF9hcHBsaWNhdGlvbnNfcGVyX3J1biIgbmFtZT0ibWF4X2FwcGxpY2F0aW9uc19wZXJfcnVuIiB0eXBlPSJudW1iZXIiIG1pbj0iMSIgbWF4PSIyNTAiIHZhbHVlPSJ7eyBzZXR0aW5ncy5hdXRvbWF0aW9uLm1heF9hcHBsaWNhdGlvbnNfcGVyX3J1biB9fSIgLz4KICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPGRpdiBjbGFzcz0iZmllbGQiPgogICAgICAgICAgICA8bGFiZWwgZm9yPSJ0cmlnZ2VyX25vdGUiPlJ1biBub3RlPC9sYWJlbD4KICAgICAgICAgICAgPGlucHV0IGlkPSJ0cmlnZ2VyX25vdGUiIG5hbWU9InRyaWdnZXJfbm90ZSIgdHlwZT0idGV4dCIgdmFsdWU9Int7IHNldHRpbmdzLmF1dG9tYXRpb24udHJpZ2dlcl9ub3RlIH19IiBwbGFjZWhvbGRlcj0iT25seSBoaWdoLWZpdCBqb2JzLiBTa2lwIHVuY2xlYXIgZm9ybXMuIiAvPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImNoZWNrLWdyaWQiPgogICAgICAgICAgPGxhYmVsIGNsYXNzPSJjaGVjay1waWxsIj4KICAgICAgICAgICAgPGlucHV0IHR5cGU9ImNoZWNrYm94IiBuYW1lPSJlbmFibGVkIiB7JSBpZiBzZXR0aW5ncy5hdXRvbWF0aW9uLmVuYWJsZWQgJX1jaGVja2VkeyUgZW5kaWYgJX0gLz4KICAgICAgICAgICAgPHNwYW4+RW5hYmxlIGFwcGx5IGZsb3c8L3NwYW4+CiAgICAgICAgICA8L2xhYmVsPgogICAgICAgICAgPGxhYmVsIGNsYXNzPSJjaGVjay1waWxsIj4KICAgICAgICAgICAgPGlucHV0IHR5cGU9ImNoZWNrYm94IiBuYW1lPSJyZXF1aXJlX3JldmlldyIgeyUgaWYgc2V0dGluZ3MuYXV0b21hdGlvbi5yZXF1aXJlX3JldmlldyAlfWNoZWNrZWR7JSBlbmRpZiAlfSAvPgogICAgICAgICAgICA8c3Bhbj5SZXF1aXJlIHJldmlldyBiZWZvcmUgc3VibWl0PC9zcGFuPgogICAgICAgICAgPC9sYWJlbD4KICAgICAgICA8L2Rpdj4KCiAgICAgICAgPGRpdiBjbGFzcz0iYXV0by1mb3JtLWZvb3RlciI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJub3RlIj57eyBzdW1tYXJ5LnRhcmdldF9zdW1tYXJ5IH19LiBCYWNrZW5kIGNyZWRlbnRpYWxzIGFuZCBzb3VyY2UgaW50ZXJuYWxzIHN0YXkgc2F2ZWQgb2ZmLXNjcmVlbi48L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImFjdGlvbnMiPgogICAgICAgICAgICA8YnV0dG9uIGNsYXNzPSJidG4gYnRuLWdob3N0IiB0eXBlPSJzdWJtaXQiIG5hbWU9ImFjdGlvbiIgdmFsdWU9InNhdmUiPlNhdmU8L2J1dHRvbj4KICAgICAgICAgICAgPGJ1dHRvbiBjbGFzcz0iYnRuIiB0eXBlPSJzdWJtaXQiIG5hbWU9ImFjdGlvbiIgdmFsdWU9InRyaWdnZXIiPlN0YXJ0IEFwcGx5PC9idXR0b24+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICA8L2Rpdj4KICAgICAgPC9zZWN0aW9uPgogICAgPC9mb3JtPgoKICAgIDxkaXYgY2xhc3M9ImRhc2hib2FyZC1ncmlkIHR3byIgc3R5bGU9Im1hcmdpbi10b3A6IDE4cHg7Ij4KICAgICAgPHNlY3Rpb24gY2xhc3M9ImNhcmQiPgogICAgICAgIDxkaXYgY2xhc3M9ImNhcmQtaGVhZCI+CiAgICAgICAgICA8aDM+UGFzdCBTY2FuczwvaDM+CiAgICAgICAgICA8c3BhbiBjbGFzcz0icGlsbCI+e3sgc2Nhbl9oaXN0b3J5fGxlbmd0aCB9fSBzaG93bjwvc3Bhbj4KICAgICAgICA8L2Rpdj4KICAgICAgICB7JSBpZiBzY2FuX2hpc3RvcnkgJX0KICAgICAgICAgIDxkaXYgY2xhc3M9InNjYW4taGlzdG9yeSI+CiAgICAgICAgICAgIHslIGZvciBzY2FuIGluIHNjYW5faGlzdG9yeSAlfQogICAgICAgICAgICAgIDxkaXYgY2xhc3M9InNjYW4taGlzdG9yeS1pdGVtIj4KICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9InNjYW4taGlzdG9yeS1tYWluIj4KICAgICAgICAgICAgICAgICAgPGRpdj4KICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJzY2FuLWhpc3RvcnktdGl0bGUiPnt7IHNjYW4ubGFiZWwgfX08L2Rpdj4KICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJzY2FuLWhpc3RvcnktY29tcGFuaWVzIj57eyBzY2FuLmNvbXBhbnlfdGV4dCB9fTwvZGl2PgogICAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ic2Nhbi1oaXN0b3J5LW1ldGEiPgogICAgICAgICAgICAgICAgICAgIDxzcGFuPnt7IHNjYW4udGltZXN0YW1wIH19PC9zcGFuPgogICAgICAgICAgICAgICAgICAgIDxzcGFuPnt7IHNjYW4uZmlsZV9jb3VudCB9fSBmaWxlczwvc3Bhbj4KICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImFjdGlvbnMiIHN0eWxlPSJtYXJnaW4tdG9wOiAxMnB4OyI+CiAgICAgICAgICAgICAgICAgIHslIGZvciBmaWxlIGluIHNjYW4uZmlsZXNbOjJdICV9CiAgICAgICAgICAgICAgICAgICAgPGEgY2xhc3M9ImxpbmstYnRuIiBocmVmPSJ7eyB1cmxfZm9yKCdkb3dubG9hZCcsIGZpbGVuYW1lPWZpbGUubmFtZSkgfX0iPnt7IGZpbGUubGFiZWwgfX08L2E+CiAgICAgICAgICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgICAgPC9kaXY+CiAgICAgICAgeyUgZWxzZSAlfQogICAgICAgICAgPHAgY2xhc3M9Im5vdGUiPk5vIHNjYW5zIHlldC48L3A+CiAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgPC9zZWN0aW9uPgoKICAgICAgPHNlY3Rpb24gY2xhc3M9ImNhcmQiPgogICAgICAgIDxkaXYgY2xhc3M9ImNhcmQtaGVhZCI+CiAgICAgICAgICA8aDM+UGFzdCBBcHBseSBSdW5zPC9oMz4KICAgICAgICAgIDxzcGFuIGNsYXNzPSJwaWxsIj57eyBoaXN0b3J5fGxlbmd0aCB9fSBzaG93bjwvc3Bhbj4KICAgICAgICA8L2Rpdj4KICAgICAgICB7JSBpZiBoaXN0b3J5ICV9CiAgICAgICAgICA8ZGl2IGNsYXNzPSJzY2FuLWhpc3RvcnkiPgogICAgICAgICAgICB7JSBmb3IgaXRlbSBpbiBoaXN0b3J5ICV9CiAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ic2Nhbi1oaXN0b3J5LWl0ZW0iPgogICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ic2Nhbi1oaXN0b3J5LW1haW4iPgogICAgICAgICAgICAgICAgICA8ZGl2PgogICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9InNjYW4taGlzdG9yeS10aXRsZSI+UnVuICN7eyBpdGVtLmlkIH19PC9kaXY+CiAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ic2Nhbi1oaXN0b3J5LWNvbXBhbmllcyI+e3sgaXRlbS5jb21wYW55X3RleHQgfX08L2Rpdj4KICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9InNjYW4taGlzdG9yeS1tZXRhIj4KICAgICAgICAgICAgICAgICAgICA8c3Bhbj57eyBpdGVtLnRpbWVzdGFtcCB9fTwvc3Bhbj4KICAgICAgICAgICAgICAgICAgICA8c3Bhbj57eyBpdGVtLnNlbGVjdGVkX2NvdW50IH19IHNob3J0bGlzdGVkPC9zcGFuPgogICAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0iYWN0aW9ucyIgc3R5bGU9Im1hcmdpbi10b3A6IDEycHg7Ij4KICAgICAgICAgICAgICAgICAgPGEgY2xhc3M9ImJ0biBidG4tZ2hvc3QiIGhyZWY9Int7IHVybF9mb3IoJ2F1dG9fYXBwbHlfcnVuX2RldGFpbCcsIHJ1bl9pZD1pdGVtLmlkKSB9fSI+T3BlbjwvYT4KICAgICAgICAgICAgICAgICAgeyUgZm9yIGZpbGUgaW4gaXRlbS5maWxlc1s6MV0gJX0KICAgICAgICAgICAgICAgICAgICA8YSBjbGFzcz0ibGluay1idG4iIGhyZWY9Int7IHVybF9mb3IoJ2Rvd25sb2FkJywgZmlsZW5hbWU9ZmlsZS5uYW1lKSB9fSI+e3sgZmlsZS5sYWJlbCB9fTwvYT4KICAgICAgICAgICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgICA8L2Rpdj4KICAgICAgICB7JSBlbHNlICV9CiAgICAgICAgICA8cCBjbGFzcz0ibm90ZSI+Tm8gYXBwbHkgcnVucyB5ZXQuPC9wPgogICAgICAgIHslIGVuZGlmICV9CiAgICAgIDwvc2VjdGlvbj4KICAgIDwvZGl2PgogIDwvZGl2Pgp7JSBlbmRibG9jayAlfQo=","auto_apply_execution.html":"eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBjb250ZW50ICV9CiAgPGRpdiBjbGFzcz0icGFnZSI+CiAgICA8aGVhZGVyIGNsYXNzPSJoZWFkZXIiPgogICAgICA8ZGl2IGNsYXNzPSJpY29uLWJhZGdlIj4KICAgICAgICA8c3ZnIHdpZHRoPSIyNiIgaGVpZ2h0PSIyNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgIDxwYXRoIGQ9Ik01IDZoMTR2MTJINVY2eiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICAgIDxwYXRoIGQ9Ik04IDEwaDhNOCAxNGg1IiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjEuNiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIi8+CiAgICAgICAgICA8cGF0aCBkPSJNOSA2VjRoNnYyIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjEuNiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIi8+CiAgICAgICAgPC9zdmc+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2PgogICAgICAgIDxoMT5BcHBseSBFeGVjdXRpb248L2gxPgogICAgICAgIDxwIGNsYXNzPSJzdWJ0aXRsZSI+UHJvZ3Jlc3MgZm9yIHRoZSBjdXJyZW50IGF1dG9tYXRlZCBhcHBseSBydW4uPC9wPgogICAgICA8L2Rpdj4KICAgIDwvaGVhZGVyPgoKICAgIDxkaXYgY2xhc3M9ImNhcmQiPgogICAgICB7JSBpZiBlcnJvciAlfQogICAgICAgIDxkaXYgY2xhc3M9InN0YXR1cyBlcnJvciI+e3sgZXJyb3IgfX08L2Rpdj4KICAgICAgeyUgZWxzZSAlfQogICAgICAgIDxkaXYgaWQ9InN0YXR1cyIgY2xhc3M9InN0YXR1cyI+U3RhcnRpbmcuLi48L2Rpdj4KICAgICAgICA8ZGl2IGlkPSJkZXRhaWwiIGNsYXNzPSJub3RlIj5UaGlzIHBhZ2UgdXBkYXRlcyBhdXRvbWF0aWNhbGx5LjwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9InN0YXRzLWdyaWQiIHN0eWxlPSJtYXJnaW4tdG9wOiAxOHB4OyI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJzdGF0Ij4KICAgICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPkNvbXBsZXRlZDwvc3Bhbj4KICAgICAgICAgICAgPHNwYW4gaWQ9ImNvbXBsZXRlZENvdW50IiBjbGFzcz0ic3RhdC12YWx1ZSI+MCAvIDA8L3NwYW4+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9InN0YXQiPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC1sYWJlbCI+U3VibWl0dGVkPC9zcGFuPgogICAgICAgICAgICA8c3BhbiBpZD0ic3VibWl0dGVkQ291bnQiIGNsYXNzPSJzdGF0LXZhbHVlIj4wPC9zcGFuPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJzdGF0Ij4KICAgICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPlByZXBhcmVkPC9zcGFuPgogICAgICAgICAgICA8c3BhbiBpZD0icHJlcGFyZWRDb3VudCIgY2xhc3M9InN0YXQtdmFsdWUiPjA8L3NwYW4+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9InN0YXQiPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC1sYWJlbCI+RmFpbGVkPC9zcGFuPgogICAgICAgICAgICA8c3BhbiBpZD0iZmFpbGVkQ291bnQiIGNsYXNzPSJzdGF0LXZhbHVlIj4wPC9zcGFuPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBpZD0iZG93bmxvYWRzIiBzdHlsZT0ibWFyZ2luLXRvcDogMThweDsiPjwvZGl2PgogICAgICB7JSBlbmRpZiAlfQogICAgPC9kaXY+CiAgPC9kaXY+CgogIHslIGlmIG5vdCBlcnJvciAlfQogICAgPHNjcmlwdD4KICAgICAgY29uc3Qgc3RhdHVzRWwgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgic3RhdHVzIik7CiAgICAgIGNvbnN0IGRldGFpbEVsID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoImRldGFpbCIpOwogICAgICBjb25zdCBjb21wbGV0ZWRDb3VudEVsID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoImNvbXBsZXRlZENvdW50Iik7CiAgICAgIGNvbnN0IHN1Ym1pdHRlZENvdW50RWwgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgic3VibWl0dGVkQ291bnQiKTsKICAgICAgY29uc3QgcHJlcGFyZWRDb3VudEVsID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInByZXBhcmVkQ291bnQiKTsKICAgICAgY29uc3QgZmFpbGVkQ291bnRFbCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJmYWlsZWRDb3VudCIpOwogICAgICBjb25zdCBkb3dubG9hZHNFbCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJkb3dubG9hZHMiKTsKICAgICAgY29uc3QgZXhlY0lkID0gInt7IGV4ZWNfaWQgfX0iOwogICAgICBjb25zdCBydW5JZCA9ICJ7eyBydW5faWQgfX0iOwoKICAgICAgYXN5bmMgZnVuY3Rpb24gcG9sbCgpIHsKICAgICAgICBjb25zdCByZXMgPSBhd2FpdCBmZXRjaChgL2F1dG8tYXBwbHkvZXhlY3V0aW9uLyR7ZXhlY0lkfS9zdGF0dXNgKTsKICAgICAgICBjb25zdCBkYXRhID0gYXdhaXQgcmVzLmpzb24oKTsKCiAgICAgICAgaWYgKGRhdGEuZXJyb3IpIHsKICAgICAgICAgIHN0YXR1c0VsLnRleHRDb250ZW50ID0gIkVycm9yIjsKICAgICAgICAgIHN0YXR1c0VsLmNsYXNzTmFtZSA9ICJzdGF0dXMgZXJyb3IiOwogICAgICAgICAgZGV0YWlsRWwudGV4dENvbnRlbnQgPSAiRXhlY3V0aW9uIGpvYiBub3QgZm91bmQuIjsKICAgICAgICAgIHJldHVybjsKICAgICAgICB9CgogICAgICAgIHN0YXR1c0VsLnRleHRDb250ZW50ID0gZGF0YS5zdGF0dXM7CiAgICAgICAgY29tcGxldGVkQ291bnRFbC50ZXh0Q29udGVudCA9IGAke2RhdGEuY29tcGxldGVkfS8ke2RhdGEudG90YWx9YDsKICAgICAgICBzdWJtaXR0ZWRDb3VudEVsLnRleHRDb250ZW50ID0gZGF0YS5zdWJtaXR0ZWQ7CiAgICAgICAgcHJlcGFyZWRDb3VudEVsLnRleHRDb250ZW50ID0gZGF0YS5wcmVwYXJlZDsKICAgICAgICBmYWlsZWRDb3VudEVsLnRleHRDb250ZW50ID0gZGF0YS5mYWlsZWQ7CiAgICAgICAgZGV0YWlsRWwudGV4dENvbnRlbnQgPSBkYXRhLmN1cnJlbnRfY29tcGFueQogICAgICAgICAgPyBgQ3VycmVudCB0YXJnZXQ6ICR7ZGF0YS5jdXJyZW50X2NvbXBhbnl9JHtkYXRhLmN1cnJlbnRfcm9sZSA/IGAgfCAke2RhdGEuY3VycmVudF9yb2xlfWAgOiAiIn1gCiAgICAgICAgICA6ICJXYWl0aW5nIGZvciB0aGUgbmV4dCBqb2IgdGFyZ2V0LiI7CgogICAgICAgIGlmIChkYXRhLmRvbmUpIHsKICAgICAgICAgIGlmIChkYXRhLmVycm9yKSB7CiAgICAgICAgICAgIHN0YXR1c0VsLmNsYXNzTmFtZSA9ICJzdGF0dXMgZXJyb3IiOwogICAgICAgICAgICBkZXRhaWxFbC50ZXh0Q29udGVudCA9IGRhdGEuZXJyb3I7CiAgICAgICAgICB9IGVsc2UgewogICAgICAgICAgICBzdGF0dXNFbC5jbGFzc05hbWUgPSAic3RhdHVzIGRvbmUiOwogICAgICAgICAgICBkZXRhaWxFbC50ZXh0Q29udGVudCA9ICJFeGVjdXRpb24gY29tcGxldGUuIjsKICAgICAgICAgICAgbGV0IGxpbmtzSHRtbCA9IGA8ZGl2IGNsYXNzPSJhY3Rpb25zIj48YSBjbGFzcz0iYnRuIGJ0bi1naG9zdCIgaHJlZj0iL2F1dG8tYXBwbHkvcnVuLyR7cnVuSWR9Ij5CYWNrIHRvIHJ1bjwvYT5gOwogICAgICAgICAgICBpZiAoZGF0YS5sb2dfZmlsZSkgewogICAgICAgICAgICAgIGxpbmtzSHRtbCArPSBgPGEgY2xhc3M9ImxpbmstYnRuIiBocmVmPSIvZG93bmxvYWQvJHtkYXRhLmxvZ19maWxlfSI+RG93bmxvYWQgbG9nPC9hPmA7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgbGlua3NIdG1sICs9IGA8L2Rpdj5gOwogICAgICAgICAgICBkb3dubG9hZHNFbC5pbm5lckhUTUwgPSBsaW5rc0h0bWw7CiAgICAgICAgICB9CiAgICAgICAgICByZXR1cm47CiAgICAgICAgfQoKICAgICAgICBzZXRUaW1lb3V0KHBvbGwsIDIwMDApOwogICAgICB9CgogICAgICBwb2xsKCk7CiAgICA8L3NjcmlwdD4KICB7JSBlbmRpZiAlfQp7JSBlbmRibG9jayAlfQo=","auto_apply_run.html":"eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBjb250ZW50ICV9CiAgPGRpdiBjbGFzcz0icGFnZSI+CiAgICA8aGVhZGVyIGNsYXNzPSJoZWFkZXIiPgogICAgICA8ZGl2IGNsYXNzPSJpY29uLWJhZGdlIj4KICAgICAgICA8c3ZnIHdpZHRoPSIyNiIgaGVpZ2h0PSIyNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgIDxwYXRoIGQ9Ik01IDZoMTR2MTJINVY2eiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICAgIDxwYXRoIGQ9Ik04IDEwaDhNOCAxNGg1IiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjEuNiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIi8+CiAgICAgICAgICA8cGF0aCBkPSJNOSA2VjRoNnYyIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjEuNiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIi8+CiAgICAgICAgPC9zdmc+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2PgogICAgICAgIDxoMT5BcHBseSBSdW4gI3t7IHJ1bi5pZCB9fTwvaDE+CiAgICAgICAgPHAgY2xhc3M9InN1YnRpdGxlIj57eyBydW4udGltZXN0YW1wIH19IHwge3sgcnVuLm1vZGUgfX08L3A+CiAgICAgIDwvZGl2PgogICAgPC9oZWFkZXI+CgogICAgPGRpdiBjbGFzcz0ic3RhdHVzIHt7ICdkb25lJyBpZiBydW4uc3RhdHVzID09ICdyZWFkeScgZWxzZSAnZXJyb3InIH19Ij4KICAgICAge3sgcnVuLnN0YXR1c19sYWJlbCB9fS4ge3sgcnVuLnNlbGVjdGVkX2NvdW50IH19IHNob3J0bGlzdGVkIGZyb20ge3sgcnVuLnNvdXJjZV9yb3dzIH19IGZvdW5kIGpvYnMuCiAgICA8L2Rpdj4KCiAgICB7JSBpZiBleGVjdXRpb25fZXJyb3IgJX0KICAgICAgPGRpdiBjbGFzcz0ic3RhdHVzIGVycm9yIiBzdHlsZT0ibWFyZ2luLXRvcDogMTJweDsiPnt7IGV4ZWN1dGlvbl9lcnJvciB9fTwvZGl2PgogICAgeyUgZW5kaWYgJX0KCiAgICB7JSBpZiBydW4uaXNzdWVzICV9CiAgICAgIDxkaXYgY2xhc3M9Imhpc3RvcnktaXNzdWVzIiBzdHlsZT0ibWFyZ2luLXRvcDogMTJweDsiPgogICAgICAgIHslIGZvciBpc3N1ZSBpbiBydW4uaXNzdWVzICV9CiAgICAgICAgICA8ZGl2IGNsYXNzPSJoaXN0b3J5LWlzc3VlIj57eyBpc3N1ZSB9fTwvZGl2PgogICAgICAgIHslIGVuZGZvciAlfQogICAgICA8L2Rpdj4KICAgIHslIGVuZGlmICV9CgogICAgPGRpdiBjbGFzcz0ic3RhdHMtZ3JpZCBhdXRvLXN1bW1hcnktZ3JpZCIgc3R5bGU9Im1hcmdpbi10b3A6IDE4cHg7Ij4KICAgICAgPGRpdiBjbGFzcz0ic3RhdCI+CiAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPk1hdGNoZWQ8L3NwYW4+CiAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtdmFsdWUiPnt7IHJ1bi5tYXRjaGVkX2NvdW50IH19PC9zcGFuPgogICAgICA8L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0ic3RhdCI+CiAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPlNob3J0bGlzdGVkPC9zcGFuPgogICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LXZhbHVlIj57eyBydW4uc2VsZWN0ZWRfY291bnQgfX08L3NwYW4+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJzdGF0Ij4KICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC1sYWJlbCI+UmVhZHkgcGxhdGZvcm1zPC9zcGFuPgogICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LXZhbHVlIGF1dG8tc3RhdC1jb21wYWN0Ij57eyBydW4ucmVhZHlfcGxhdGZvcm1zfGpvaW4oJywgJykgb3IgIk5vbmUiIH19PC9zcGFuPgogICAgICA8L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0ic3RhdCI+CiAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPlNvdXJjZSBmaWxlPC9zcGFuPgogICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LXZhbHVlIGF1dG8tc3RhdC1jb21wYWN0Ij57eyBydW4uc291cmNlX2ZpbGUgb3IgIk1pc3NpbmciIH19PC9zcGFuPgogICAgICA8L2Rpdj4KICAgIDwvZGl2PgoKICAgIDxzZWN0aW9uIGNsYXNzPSJjYXJkIiBzdHlsZT0ibWFyZ2luLXRvcDogMThweDsiPgogICAgICA8ZGl2IGNsYXNzPSJjYXJkLWhlYWQiPgogICAgICAgIDxoMz5BY3Rpb25zPC9oMz4KICAgICAgICA8c3BhbiBjbGFzcz0icGlsbCI+UnVuIG91dHB1dDwvc3Bhbj4KICAgICAgPC9kaXY+CiAgICAgIDxwIGNsYXNzPSJub3RlIj57eyBydW4udGFyZ2V0X3N1bW1hcnkgfX08L3A+CiAgICAgIDxwIGNsYXNzPSJub3RlIj5BdXRvbm9tb3VzIHN1Ym1pdDogPHN0cm9uZz57eyAiRW5hYmxlZCIgaWYgZXhlY3V0aW9uX3BvbGljeS5lZmZlY3RpdmVfYWxsb3dfc3VibWl0IGVsc2UgIkRpc2FibGVkIiB9fTwvc3Ryb25nPjwvcD4KICAgICAgPHAgY2xhc3M9Im5vdGUiPnt7IGV4ZWN1dGlvbl9wb2xpY3kubW9kZV9ub3RlIH19PC9wPgogICAgICA8ZGl2IGNsYXNzPSJhY3Rpb25zIj4KICAgICAgICA8YSBjbGFzcz0iYnRuIGJ0bi1naG9zdCIgaHJlZj0iL2F1dG8tYXBwbHkiPkJhY2s8L2E+CiAgICAgICAgeyUgaWYgcnVuLmV4cG9ydHMueGxzeCAlfQogICAgICAgICAgPGEgY2xhc3M9ImxpbmstYnRuIiBocmVmPSJ7eyB1cmxfZm9yKCdkb3dubG9hZCcsIGZpbGVuYW1lPXJ1bi5leHBvcnRzLnhsc3gpIH19Ij5Eb3dubG9hZCBzaG9ydGxpc3Q8L2E+CiAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgICB7JSBpZiBydW4uc2VsZWN0ZWRfY291bnQgYW5kIGV4ZWN1dGlvbl9wb2xpY3kuY2FuX2V4ZWN1dGUgJX0KICAgICAgICAgIDxmb3JtIG1ldGhvZD0icG9zdCIgYWN0aW9uPSJ7eyB1cmxfZm9yKCdhdXRvX2FwcGx5X3J1bl9leGVjdXRlJywgcnVuX2lkPXJ1bi5pZCkgfX0iPgogICAgICAgICAgICA8YnV0dG9uIGNsYXNzPSJidG4iIHR5cGU9InN1Ym1pdCI+e3sgZXhlY3V0aW9uX3BvbGljeS5hY3Rpb25fbGFiZWwgfX08L2J1dHRvbj4KICAgICAgICAgIDwvZm9ybT4KICAgICAgICB7JSBlbGlmIHJ1bi5zZWxlY3RlZF9jb3VudCAlfQogICAgICAgICAgPHNwYW4gY2xhc3M9Im5vdGUiPkV4ZWN1dGlvbiBpcyBkaXNhYmxlZCBmb3IgdGhpcyBydW4uPC9zcGFuPgogICAgICAgIHslIGVuZGlmICV9CiAgICAgIDwvZGl2PgogICAgPC9zZWN0aW9uPgoKICAgIHslIGlmIHJ1bi5sYXN0X2V4ZWN1dGlvbiAlfQogICAgICA8c2VjdGlvbiBjbGFzcz0iY2FyZCIgc3R5bGU9Im1hcmdpbi10b3A6IDE4cHg7Ij4KICAgICAgICA8ZGl2IGNsYXNzPSJjYXJkLWhlYWQiPgogICAgICAgICAgPGgzPkxhc3QgRXhlY3V0aW9uPC9oMz4KICAgICAgICAgIDxzcGFuIGNsYXNzPSJwaWxsIj57eyBydW4ubGFzdF9leGVjdXRpb24uc3RhdHVzIH19PC9zcGFuPgogICAgICAgIDwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9InN0YXRzLWdyaWQiPgogICAgICAgICAgPGRpdiBjbGFzcz0ic3RhdCI+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LWxhYmVsIj5TdWJtaXR0ZWQ8L3NwYW4+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LXZhbHVlIj57eyBydW4ubGFzdF9leGVjdXRpb24uc3VibWl0dGVkIH19PC9zcGFuPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJzdGF0Ij4KICAgICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPlByZXBhcmVkPC9zcGFuPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC12YWx1ZSI+e3sgcnVuLmxhc3RfZXhlY3V0aW9uLnByZXBhcmVkIH19PC9zcGFuPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJzdGF0Ij4KICAgICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPkZhaWxlZDwvc3Bhbj4KICAgICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtdmFsdWUiPnt7IHJ1bi5sYXN0X2V4ZWN1dGlvbi5mYWlsZWQgfX08L3NwYW4+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9InN0YXQiPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC1sYWJlbCI+U2tpcHBlZDwvc3Bhbj4KICAgICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtdmFsdWUiPnt7IHJ1bi5sYXN0X2V4ZWN1dGlvbi5za2lwcGVkIH19PC9zcGFuPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0iYWN0aW9ucyI+CiAgICAgICAgICA8YSBjbGFzcz0iYnRuIGJ0bi1naG9zdCIgaHJlZj0ie3sgdXJsX2ZvcignYXV0b19hcHBseV9leGVjdXRpb25fcGFnZScsIGV4ZWNfaWQ9cnVuLmxhc3RfZXhlY3V0aW9uLmlkKSB9fSI+T3BlbiBleGVjdXRpb248L2E+CiAgICAgICAgICB7JSBpZiBydW4ubGFzdF9leGVjdXRpb24ubG9nX2ZpbGUgJX0KICAgICAgICAgICAgPGEgY2xhc3M9ImxpbmstYnRuIiBocmVmPSJ7eyB1cmxfZm9yKCdkb3dubG9hZCcsIGZpbGVuYW1lPXJ1bi5sYXN0X2V4ZWN1dGlvbi5sb2dfZmlsZSkgfX0iPkRvd25sb2FkIGxvZzwvYT4KICAgICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgPC9kaXY+CiAgICAgIDwvc2VjdGlvbj4KICAgIHslIGVuZGlmICV9CgogICAgPHNlY3Rpb24gY2xhc3M9ImNhcmQiIHN0eWxlPSJtYXJnaW4tdG9wOiAxOHB4OyI+CiAgICAgIDxkaXYgY2xhc3M9ImNhcmQtaGVhZCI+CiAgICAgICAgPGgzPlNob3J0bGlzdDwvaDM+CiAgICAgICAgPHNwYW4gY2xhc3M9InBpbGwiPnt7IHJ1bi5zZWxlY3RlZF9jb3VudCB9fSBqb2JzPC9zcGFuPgogICAgICA8L2Rpdj4KCiAgICAgIHslIGlmIHJ1bi5tYXRjaGVzICV9CiAgICAgICAgPHRhYmxlIGNsYXNzPSJ0YWJsZSI+CiAgICAgICAgICA8dGhlYWQ+CiAgICAgICAgICAgIDx0cj4KICAgICAgICAgICAgICA8dGg+Q29tcGFueTwvdGg+CiAgICAgICAgICAgICAgPHRoPlJvbGU8L3RoPgogICAgICAgICAgICAgIDx0aD5GaXQ8L3RoPgogICAgICAgICAgICAgIDx0aD5BY3Rpb248L3RoPgogICAgICAgICAgICA8L3RyPgogICAgICAgICAgPC90aGVhZD4KICAgICAgICAgIDx0Ym9keT4KICAgICAgICAgICAgeyUgZm9yIGl0ZW0gaW4gcnVuLm1hdGNoZXMgJX0KICAgICAgICAgICAgICA8dHI+CiAgICAgICAgICAgICAgICA8dGQ+e3sgaXRlbS5jb21wYW55IG9yICJVbmtub3duIGNvbXBhbnkiIH19PC90ZD4KICAgICAgICAgICAgICAgIDx0ZD57eyBpdGVtLnJvbGUgb3IgIlJvbGUgbm90IGV4dHJhY3RlZCIgfX08L3RkPgogICAgICAgICAgICAgICAgPHRkPnt7IGl0ZW0uZml0X3Njb3JlIH19PC90ZD4KICAgICAgICAgICAgICAgIDx0ZD4KICAgICAgICAgICAgICAgICAgeyUgaWYgaXRlbS5hcHBseV9saW5rcyAlfQogICAgICAgICAgICAgICAgICAgIDxhIGNsYXNzPSJ0YWJsZS1saW5rIiBocmVmPSJ7eyBpdGVtLmFwcGx5X2xpbmtzWzBdIH19IiB0YXJnZXQ9Il9ibGFuayIgcmVsPSJub29wZW5lciI+T3BlbiBhcHBseSBsaW5rPC9hPgogICAgICAgICAgICAgICAgICB7JSBlbGlmIGl0ZW0uZW1haWxzICV9CiAgICAgICAgICAgICAgICAgICAgPGEgY2xhc3M9InRhYmxlLWxpbmsiIGhyZWY9Im1haWx0bzp7eyBpdGVtLmVtYWlsc1swXSB9fSI+e3sgaXRlbS5lbWFpbHNbMF0gfX08L2E+CiAgICAgICAgICAgICAgICAgIHslIGVsc2UgJX0KICAgICAgICAgICAgICAgICAgICA8c3BhbiBjbGFzcz0ibm90ZSI+TWFudWFsIHJldmlldzwvc3Bhbj4KICAgICAgICAgICAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgICAgICAgICAgIDwvdGQ+CiAgICAgICAgICAgICAgPC90cj4KICAgICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgICA8L3Rib2R5PgogICAgICAgIDwvdGFibGU+CiAgICAgIHslIGVsc2UgJX0KICAgICAgICA8cCBjbGFzcz0ibm90ZSI+Tm8gc2hvcnRsaXN0ZWQgb3Bwb3J0dW5pdGllcyB3ZXJlIGdlbmVyYXRlZCBmb3IgdGhpcyBydW4uPC9wPgogICAgICB7JSBlbmRpZiAlfQogICAgPC9zZWN0aW9uPgogIDwvZGl2Pgp7JSBlbmRibG9jayAlfQo=","base.html":"PCFkb2N0eXBlIGh0bWw+CjxodG1sIGxhbmc9ImVuIj4KICA8aGVhZD4KICAgIDxtZXRhIGNoYXJzZXQ9InV0Zi04IiAvPgogICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xIiAvPgogICAgPHRpdGxlPnt7IHRpdGxlIG9yICJDYXJlZXIgU3VpdGUiIH19PC90aXRsZT4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0ie3sgdXJsX2Zvcignc3RhdGljJywgZmlsZW5hbWU9J2FwcC5jc3MnKSB9fSIgLz4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi50YWlsd2luZGNzcy5jb20iPjwvc2NyaXB0PgogICAgeyUgYmxvY2sgaGVhZCAlfXslIGVuZGJsb2NrICV9CiAgPC9oZWFkPgogIDxib2R5PgogICAgPGRpdiBjbGFzcz0ibGF5b3V0Ij4KICAgICAgPGFzaWRlIGNsYXNzPSJzaWRlYmFyIiBpZD0ic2lkZWJhciI+CiAgICAgICAgPGRpdiBjbGFzcz0iYnJhbmQiPgogICAgICAgICAgPGRpdiBjbGFzcz0iYnJhbmQtaWNvbiI+Q1M8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImJyYW5kLXRleHQiPgogICAgICAgICAgICA8c3Ryb25nPkNhcmVlciBTdWl0ZTwvc3Ryb25nPgogICAgICAgICAgICA8c3Bhbj5CeSBWYWliaGF2IEthcG9vcjwvc3Bhbj4KICAgICAgICAgIDwvZGl2PgogICAgICAgIDwvZGl2PgogICAgICAgIDxuYXYgY2xhc3M9Im5hdiI+CiAgICAgICAgICA8YSBocmVmPSIvIiBjbGFzcz0ibmF2LWxpbmsge3sgJ2FjdGl2ZScgaWYgcmVxdWVzdC5wYXRoID09ICcvJyBlbHNlICcnIH19IiBhcmlhLWxhYmVsPSJEYXNoYm9hcmQiPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ibmF2LWljb24iPgogICAgICAgICAgICAgIDxzdmcgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik00IDRoN3Y3SDRWNHpNMTMgNGg3djRoLTdWNHpNMTMgMTBoN3YxMGgtN1YxMHpNNCAxM2g3djdINHYtN3oiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNiIvPgogICAgICAgICAgICAgIDwvc3ZnPgogICAgICAgICAgICA8L3NwYW4+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJuYXYtbGFiZWwiPkRhc2hib2FyZDwvc3Bhbj4KICAgICAgICAgIDwvYT4KICAgICAgICAgIDxhIGhyZWY9Ii9zY2FuIiBjbGFzcz0ibmF2LWxpbmsge3sgJ2FjdGl2ZScgaWYgcmVxdWVzdC5wYXRoLnN0YXJ0c3dpdGgoJy9zY2FuJykgb3IgcmVxdWVzdC5wYXRoLnN0YXJ0c3dpdGgoJy9qb2InKSBlbHNlICcnIH19IiBhcmlhLWxhYmVsPSJMaW5rZWRJbiBTY3JhcGVyIj4KICAgICAgICAgICAgPHNwYW4gY2xhc3M9Im5hdi1pY29uIj4KICAgICAgICAgICAgICA8c3ZnIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSI+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNNCA2aDEwTTQgMTJoMTZNNCAxOGgxMiIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS42IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz4KICAgICAgICAgICAgICAgIDxjaXJjbGUgY3g9IjE4IiBjeT0iNiIgcj0iMyIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS42Ii8+CiAgICAgICAgICAgICAgPC9zdmc+CiAgICAgICAgICAgIDwvc3Bhbj4KICAgICAgICAgICAgPHNwYW4gY2xhc3M9Im5hdi1sYWJlbCI+TGlua2VkSW4gU2NyYXBlcjwvc3Bhbj4KICAgICAgICAgIDwvYT4KICAgICAgICAgIDxhIGhyZWY9Ii9yZXN1bWUtcmV2aWV3IiBjbGFzcz0ibmF2LWxpbmsge3sgJ2FjdGl2ZScgaWYgcmVxdWVzdC5wYXRoLnN0YXJ0c3dpdGgoJy9yZXN1bWUtcmV2aWV3JykgZWxzZSAnJyB9fSIgYXJpYS1sYWJlbD0iUmVzdW1lIFJldmlldyI+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJuYXYtaWNvbiI+CiAgICAgICAgICAgICAgPHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiPgogICAgICAgICAgICAgICAgPHBhdGggZD0iTTYgNGg5bDMgM3YxM0g2VjR6IiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik05IDEwaDZNOSAxNGg2TTkgMThoNCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS42IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz4KICAgICAgICAgICAgICA8L3N2Zz4KICAgICAgICAgICAgPC9zcGFuPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ibmF2LWxhYmVsIj5SZXN1bWUgUmV2aWV3PC9zcGFuPgogICAgICAgICAgPC9hPgogICAgICAgICAgPGEgaHJlZj0iL2xpbmtlZGluLXJldmlldyIgY2xhc3M9Im5hdi1saW5rIHt7ICdhY3RpdmUnIGlmIHJlcXVlc3QucGF0aC5zdGFydHN3aXRoKCcvbGlua2VkaW4tcmV2aWV3JykgZWxzZSAnJyB9fSIgYXJpYS1sYWJlbD0iTGlua2VkSW4gQW5hbHl6ZXIiPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ibmF2LWljb24iPgogICAgICAgICAgICAgIDxzdmcgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik00IDIwVjhtNiAxMlY0bTYgMTZ2LTZtNiA2VjEwIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogICAgICAgICAgICAgIDwvc3ZnPgogICAgICAgICAgICA8L3NwYW4+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJuYXYtbGFiZWwiPkxpbmtlZEluIEFuYWx5emVyPC9zcGFuPgogICAgICAgICAgPC9hPgogICAgICAgICAgPGEgaHJlZj0iL2xpbmtlZGluLXBvc3RzIiBjbGFzcz0ibmF2LWxpbmsge3sgJ2FjdGl2ZScgaWYgcmVxdWVzdC5wYXRoLnN0YXJ0c3dpdGgoJy9saW5rZWRpbi1wb3N0cycpIGVsc2UgJycgfX0iIGFyaWEtbGFiZWw9IkxpbmtlZEluIEFJIFBvc3RzIj4KICAgICAgICAgICAgPHNwYW4gY2xhc3M9Im5hdi1pY29uIj4KICAgICAgICAgICAgICA8c3ZnIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSI+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNNCAxOS41VjdhMiAyIDAgMCAxIDItMmg3bDUgNXY5LjVhMiAyIDAgMCAxLTIgMkg2YTIgMiAwIDAgMS0yLTJ6IiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik04IDEyaDhNOCAxNmg2IiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogICAgICAgICAgICAgICAgPHBhdGggZD0iTTEzIDV2NGg0IiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogICAgICAgICAgICAgIDwvc3ZnPgogICAgICAgICAgICA8L3NwYW4+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJuYXYtbGFiZWwiPkxpbmtlZEluIEFJIFBvc3RzPC9zcGFuPgogICAgICAgICAgPC9hPgogICAgICAgICAgPGEgaHJlZj0iL2F1dG8tYXBwbHkiIGNsYXNzPSJuYXYtbGluayB7eyAnYWN0aXZlJyBpZiByZXF1ZXN0LnBhdGguc3RhcnRzd2l0aCgnL2F1dG8tYXBwbHknKSBlbHNlICcnIH19IiBhcmlhLWxhYmVsPSJBdXRvIEpvYiBBcHBseSI+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJuYXYtaWNvbiI+CiAgICAgICAgICAgICAgPHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiPgogICAgICAgICAgICAgICAgPHBhdGggZD0iTTUgN2gxNHYxMUg1Vjd6IiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik05IDdWNWg2djIiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIi8+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNOCAxMWg4TTggMTRoNSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS42IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz4KICAgICAgICAgICAgICA8L3N2Zz4KICAgICAgICAgICAgPC9zcGFuPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ibmF2LWxhYmVsIj5BdXRvIEpvYiBBcHBseTwvc3Bhbj4KICAgICAgICAgIDwvYT4KICAgICAgICAgIDxhIGhyZWY9Ii9qb2ItY29tcGlsZXIiIGNsYXNzPSJuYXYtbGluayB7eyAnYWN0aXZlJyBpZiByZXF1ZXN0LnBhdGguc3RhcnRzd2l0aCgnL2pvYi1jb21waWxlcicpIGVsc2UgJycgfX0iIGFyaWEtbGFiZWw9IkppYiBDb21waWxlciI+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJuYXYtaWNvbiI+CiAgICAgICAgICAgICAgPHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiPgogICAgICAgICAgICAgICAgPHBhdGggZD0iTTQgN2gxNnYxMEg0Vjd6IiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik04IDExaDhNOCAxNGg1IiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogICAgICAgICAgICAgICAgPHBhdGggZD0iTTcgN1Y1aDEwdjIiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIi8+CiAgICAgICAgICAgICAgPC9zdmc+CiAgICAgICAgICAgIDwvc3Bhbj4KICAgICAgICAgICAgPHNwYW4gY2xhc3M9Im5hdi1sYWJlbCI+SmliIENvbXBpbGVyPC9zcGFuPgogICAgICAgICAgPC9hPgogICAgICAgICAgPGEgaHJlZj0iL2VtYWlsIiBjbGFzcz0ibmF2LWxpbmsge3sgJ2FjdGl2ZScgaWYgcmVxdWVzdC5wYXRoLnN0YXJ0c3dpdGgoJy9lbWFpbCcpIGVsc2UgJycgfX0iIGFyaWEtbGFiZWw9IkVtYWlsIEF1dG9tYXRpb24iPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ibmF2LWljb24iPgogICAgICAgICAgICAgIDxzdmcgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik00IDZoMTZ2MTJINFY2eiIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS42Ii8+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNNCA3bDggNiA4LTYiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNiIvPgogICAgICAgICAgICAgIDwvc3ZnPgogICAgICAgICAgICA8L3NwYW4+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJuYXYtbGFiZWwiPkVtYWlsIEF1dG9tYXRpb248L3NwYW4+CiAgICAgICAgICA8L2E+CiAgICAgICAgPC9uYXY+CiAgICAgICAgPGJ1dHRvbiBjbGFzcz0idG9nZ2xlIiB0eXBlPSJidXR0b24iIG9uY2xpY2s9InRvZ2dsZVNpZGViYXIoKSI+Q29sbGFwc2U8L2J1dHRvbj4KICAgICAgPC9hc2lkZT4KCiAgICAgIDxtYWluIGNsYXNzPSJtYWluIj4KICAgICAgICB7JSBibG9jayBjb250ZW50ICV9eyUgZW5kYmxvY2sgJX0KICAgICAgPC9tYWluPgogICAgPC9kaXY+CgogICAgPGRpdiBjbGFzcz0ic2lnbmF0dXJlIj4KICAgICAgQnkgVmFpYmhhdiBLYXBvb3IsPGJyIC8+CiAgICAgIHZhaWJoYXZrYXBvb3J3b3JrQGdtYWlsLmNvbQogICAgPC9kaXY+CgogICAgPHNjcmlwdD4KICAgICAgZnVuY3Rpb24gdG9nZ2xlU2lkZWJhcigpIHsKICAgICAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgic2lkZWJhciIpLmNsYXNzTGlzdC50b2dnbGUoImNvbGxhcHNlZCIpOwogICAgICB9CiAgICA8L3NjcmlwdD4KICAgIHslIGJsb2NrIHNjcmlwdHMgJX17JSBlbmRibG9jayAlfQogIDwvYm9keT4KPC9odG1sPgo=","coming_soon.html":"eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBjb250ZW50ICV9CiAgPGRpdiBjbGFzcz0icGFnZSI+CiAgICA8aGVhZGVyIGNsYXNzPSJoZWFkZXIiPgogICAgICA8ZGl2IGNsYXNzPSJpY29uLWJhZGdlIj4KICAgICAgICA8c3ZnIHdpZHRoPSIyNiIgaGVpZ2h0PSIyNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgIDxwYXRoIGQ9Ik0xMiA0djE2TTQgMTJoMTYiIHN0cm9rZT0id2hpdGUiIHN0cm9rZS13aWR0aD0iMS42IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz4KICAgICAgICA8L3N2Zz4KICAgICAgPC9kaXY+CiAgICAgIDxkaXY+CiAgICAgICAgPGgxPnt7IHRpdGxlIH19PC9oMT4KICAgICAgICA8cCBjbGFzcz0ic3VidGl0bGUiPkNvbWluZyBzb29uLjwvcD4KICAgICAgPC9kaXY+CiAgICA8L2hlYWRlcj4KCiAgICA8ZGl2IGNsYXNzPSJjYXJkIj4KICAgICAgPHAgY2xhc3M9Im5vdGUiPnt7IGRlc2NyaXB0aW9uIH19PC9wPgogICAgICA8ZGl2IGNsYXNzPSJhY3Rpb25zIj4KICAgICAgICA8YSBjbGFzcz0ibGluay1idG4iIGhyZWY9Ii8iPkJhY2sgdG8gRGFzaGJvYXJkPC9hPgogICAgICA8L2Rpdj4KICAgIDwvZGl2PgogIDwvZGl2Pgp7JSBlbmRibG9jayAlfQo=","email_compose.html":"eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBjb250ZW50ICV9CiAgPGRpdiBjbGFzcz0icGFnZSI+CiAgICA8aGVhZGVyIGNsYXNzPSJoZWFkZXIiPgogICAgICA8ZGl2IGNsYXNzPSJpY29uLWJhZGdlIj4KICAgICAgICA8c3ZnIHdpZHRoPSIyNiIgaGVpZ2h0PSIyNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgIDxwYXRoIGQ9Ik00IDZoMTZ2MTJINFY2eiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICAgIDxwYXRoIGQ9Ik00IDdsOCA2IDgtNiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICA8L3N2Zz4KICAgICAgPC9kaXY+CiAgICAgIDxkaXY+CiAgICAgICAgPGgxPkNvbXBvc2UgRW1haWxzPC9oMT4KICAgICAgICA8cCBjbGFzcz0ic3VidGl0bGUiPlBlcnNvbmFsaXplZCBvdXRyZWFjaCB3aXRoIHRlbXBsYXRlcywgdG9rZW5zLCBhbmQgdGhyb3R0bGluZy48L3A+CiAgICAgIDwvZGl2PgogICAgPC9oZWFkZXI+CgogICAgPGRpdiBjbGFzcz0iY2FyZCI+CiAgICAgIHslIGlmIGVycm9yICV9CiAgICAgICAgPGRpdiBjbGFzcz0ic3RhdHVzIGVycm9yIj57eyBlcnJvciB9fTwvZGl2PgogICAgICB7JSBlbmRpZiAlfQogICAgICA8ZGl2IGNsYXNzPSJzdGF0cy1ncmlkIj4KICAgICAgICA8ZGl2IGNsYXNzPSJzdGF0Ij4KICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LWxhYmVsIj5SZWNpcGllbnRzPC9zcGFuPgogICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtdmFsdWUiPnt7IGNvdW50IH19PC9zcGFuPgogICAgICAgIDwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9InN0YXQiPgogICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPkNvbXBhbmllczwvc3Bhbj4KICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LXZhbHVlIj57eyBzdGF0cy5jb21wYW5pZXMgfX08L3NwYW4+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0ic3RhdCI+CiAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC1sYWJlbCI+TWlzc2luZyBSb2xlczwvc3Bhbj4KICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LXZhbHVlIj57eyBzdGF0cy5taXNzaW5nX3JvbGUgfX08L3NwYW4+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0ic3RhdCI+CiAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC1sYWJlbCI+TWlzc2luZyBBcHBseSBMaW5rczwvc3Bhbj4KICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LXZhbHVlIj57eyBzdGF0cy5taXNzaW5nX2FwcGx5IH19PC9zcGFuPgogICAgICAgIDwvZGl2PgogICAgICA8L2Rpdj4KICAgICAgPHAgY2xhc3M9Im5vdGUiPkR1cGxpY2F0ZXMgcmVtb3ZlZDogPHN0cm9uZz57eyBkdXBsaWNhdGVzIH19PC9zdHJvbmc+PC9wPgogICAgPC9kaXY+CgogICAgPGZvcm0gbWV0aG9kPSJwb3N0IiBhY3Rpb249Ii9lbWFpbC9zZW5kL3t7IGpvYl9pZCB9fSIgY2xhc3M9InN0YWdnZXIiIGlkPSJlbWFpbEZvcm0iPgogICAgICA8ZGl2IGNsYXNzPSJjYXJkIj4KICAgICAgICA8ZGl2IGNsYXNzPSJjYXJkLWhlYWQiPgogICAgICAgICAgPGgzPlRlbXBsYXRlICZhbXA7IFBlcnNvbmFsaXphdGlvbjwvaDM+CiAgICAgICAgICA8c3BhbiBjbGFzcz0icGlsbCI+U2VxdWVuY2UgY29udHJvbHM8L3NwYW4+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9InRlbXBsYXRlLWdyaWQiIGlkPSJ0ZW1wbGF0ZUdyaWQiPgogICAgICAgICAgeyUgZm9yIHRlbXBsYXRlIGluIGVtYWlsX3RlbXBsYXRlcyAlfQogICAgICAgICAgPGxhYmVsIGNsYXNzPSJ0ZW1wbGF0ZS1jYXJkeyUgaWYgdGVtcGxhdGUuaWQgPT0gdGVtcGxhdGVfaWQgJX0gYWN0aXZleyUgZW5kaWYgJX0iIGRhdGEtdGVtcGxhdGUtY2FyZD4KICAgICAgICAgICAgPGlucHV0CiAgICAgICAgICAgICAgdHlwZT0icmFkaW8iCiAgICAgICAgICAgICAgbmFtZT0idGVtcGxhdGVfaWQiCiAgICAgICAgICAgICAgdmFsdWU9Int7IHRlbXBsYXRlLmlkIH19IgogICAgICAgICAgICAgIHslIGlmIHRlbXBsYXRlLmlkID09IHRlbXBsYXRlX2lkICV9Y2hlY2tlZHslIGVuZGlmICV9CiAgICAgICAgICAgIC8+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9InRlbXBsYXRlLXRpdGxlIj57eyB0ZW1wbGF0ZS5sYWJlbCB9fTwvZGl2PgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJub3RlIj57eyB0ZW1wbGF0ZS5kZXNjcmlwdGlvbiB9fTwvZGl2PgogICAgICAgICAgPC9sYWJlbD4KICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgIDwvZGl2PgoKICAgICAgICA8ZGl2IGNsYXNzPSJncmlkIHR3byIgc3R5bGU9Im1hcmdpbi10b3A6MTJweDsiPgogICAgICAgICAgPGRpdiBjbGFzcz0iZmllbGQiPgogICAgICAgICAgICA8bGFiZWwgZm9yPSJzZW5kX2RlbGF5Ij5TZW5kIGRlbGF5IChzZWNvbmRzKTwvbGFiZWw+CiAgICAgICAgICAgIDxpbnB1dCBpZD0ic2VuZF9kZWxheSIgbmFtZT0ic2VuZF9kZWxheSIgdHlwZT0ibnVtYmVyIiBtaW49IjAiIG1heD0iNjAiIHZhbHVlPSI2IiAvPgogICAgICAgICAgICA8cCBjbGFzcz0ibm90ZSI+QWRkcyBhIHBhdXNlIGJldHdlZW4gZW1haWxzIHRvIGF2b2lkIHJhdGUgbGltaXRzLjwvcD4KICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPGRpdiBjbGFzcz0iZmllbGQiPgogICAgICAgICAgICA8bGFiZWw+QXR0YWNobWVudHM8L2xhYmVsPgogICAgICAgICAgICA8bGFiZWwgY2xhc3M9InRvZ2dsZS1saW5lIj4KICAgICAgICAgICAgICA8aW5wdXQgdHlwZT0iY2hlY2tib3giIG5hbWU9ImF0dGFjaF9yZXN1bWUiIGNoZWNrZWQgLz4KICAgICAgICAgICAgICBBdHRhY2ggcmVzdW1lIFBERgogICAgICAgICAgICA8L2xhYmVsPgogICAgICAgICAgICA8cCBjbGFzcz0ibm90ZSI+UmVzdW1lIGlzIHN0aWxsIHVzZWQgdG8gcGVyc29uYWxpemUgY29weS48L3A+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICA8L2Rpdj4KCiAgICAgICAgPGRpdiBjbGFzcz0iZ3JpZCB0d28iIHN0eWxlPSJtYXJnaW4tdG9wOjEycHg7Ij4KICAgICAgICAgIDxsYWJlbCBjbGFzcz0idG9nZ2xlLWxpbmUiPgogICAgICAgICAgICA8aW5wdXQgdHlwZT0iY2hlY2tib3giIGlkPSJpbmNsdWRlTGlua3MiIG5hbWU9ImluY2x1ZGVfbGlua3MiIGNoZWNrZWQgLz4KICAgICAgICAgICAgSW5jbHVkZSBhcHBseS9wb3N0IGxpbmtzCiAgICAgICAgICA8L2xhYmVsPgogICAgICAgICAgPGxhYmVsIGNsYXNzPSJ0b2dnbGUtbGluZSI+CiAgICAgICAgICAgIDxpbnB1dCB0eXBlPSJjaGVja2JveCIgaWQ9ImluY2x1ZGVBY2hpZXZlbWVudHMiIG5hbWU9ImluY2x1ZGVfYWNoaWV2ZW1lbnRzIiBjaGVja2VkIC8+CiAgICAgICAgICAgIEluY2x1ZGUgaW1wYWN0IGJ1bGxldHMKICAgICAgICAgIDwvbGFiZWw+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImZpZWxkIiBzdHlsZT0ibWFyZ2luLXRvcDoxMnB4OyI+CiAgICAgICAgICA8bGFiZWwgZm9yPSJzdWJqZWN0VGVtcGxhdGUiPlN1YmplY3QgdGVtcGxhdGU8L2xhYmVsPgogICAgICAgICAgPGlucHV0IGlkPSJzdWJqZWN0VGVtcGxhdGUiIG5hbWU9InN1YmplY3RfdGVtcGxhdGUiIHR5cGU9InRleHQiIHZhbHVlPSJ7eyBzdWJqZWN0X3RlbXBsYXRlIH19IiAvPgogICAgICAgIDwvZGl2PgoKICAgICAgICA8ZGl2IGNsYXNzPSJmaWVsZCIgc3R5bGU9Im1hcmdpbi10b3A6MTJweDsiPgogICAgICAgICAgPGxhYmVsIGZvcj0iYm9keVRlbXBsYXRlIj5Cb2R5IHRlbXBsYXRlPC9sYWJlbD4KICAgICAgICAgIDx0ZXh0YXJlYSBpZD0iYm9keVRlbXBsYXRlIiBuYW1lPSJib2R5X3RlbXBsYXRlIiByb3dzPSIxMCI+e3sgYm9keV90ZW1wbGF0ZSB9fTwvdGV4dGFyZWE+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImNoaXBzIj4KICAgICAgICAgIHslIGZvciB0b2tlbiBpbiB0b2tlbnMgJX0KICAgICAgICAgIDxzcGFuIGNsYXNzPSJjaGlwIHNvZnQiPnt7IHRva2VuIH19PC9zcGFuPgogICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgPC9kaXY+CiAgICAgICAgPHAgY2xhc3M9Im5vdGUiPlRva2VucyBhcmUgcmVwbGFjZWQgcGVyIHJlY2lwaWVudC4gRW1wdHkgdG9rZW5zIGFyZSByZW1vdmVkLjwvcD4KICAgICAgPC9kaXY+CgogICAgICA8ZGl2IGNsYXNzPSJjYXJkIj4KICAgICAgICA8ZGl2IGNsYXNzPSJjYXJkLWhlYWQiPgogICAgICAgICAgPGgzPkxpdmUgUHJldmlldzwvaDM+CiAgICAgICAgICA8c3BhbiBjbGFzcz0icGlsbCI+UmVjaXBpZW50IDE8L3NwYW4+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0icHJldmlldy1ibG9jayI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJwcmV2aWV3LXN1YmplY3QiIGlkPSJwcmV2aWV3U3ViamVjdCI+e3sgc2FtcGxlX3N1YmplY3QgfX08L2Rpdj4KICAgICAgICAgIDxwcmUgY2xhc3M9InByZXZpZXctYm9keSIgaWQ9InByZXZpZXdCb2R5Ij57eyBzYW1wbGVfYm9keSB9fTwvcHJlPgogICAgICAgIDwvZGl2PgogICAgICA8L2Rpdj4KCiAgICAgIDxkaXYgY2xhc3M9ImNhcmQiPgogICAgICAgIDxkaXYgY2xhc3M9ImNhcmQtaGVhZCI+CiAgICAgICAgICA8aDM+U2VuZGVyPC9oMz4KICAgICAgICAgIDxzcGFuIGNsYXNzPSJwaWxsIj5TaWduYXR1cmU8L3NwYW4+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0iZ3JpZCB0d28iPgogICAgICAgICAgPGRpdiBjbGFzcz0iZmllbGQiPgogICAgICAgICAgICA8bGFiZWwgZm9yPSJzZW5kZXJfbmFtZSI+WW91ciBuYW1lPC9sYWJlbD4KICAgICAgICAgICAgPGlucHV0IGlkPSJzZW5kZXJfbmFtZSIgbmFtZT0ic2VuZGVyX25hbWUiIHR5cGU9InRleHQiIHBsYWNlaG9sZGVyPSJZb3VyIE5hbWUiIHJlcXVpcmVkIC8+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImZpZWxkIj4KICAgICAgICAgICAgPGxhYmVsIGZvcj0ic2VuZGVyX2NvbnRhY3QiPkNvbnRhY3QgKG9wdGlvbmFsKTwvbGFiZWw+CiAgICAgICAgICAgIDxpbnB1dCBpZD0ic2VuZGVyX2NvbnRhY3QiIG5hbWU9InNlbmRlcl9jb250YWN0IiB0eXBlPSJ0ZXh0IiBwbGFjZWhvbGRlcj0iUGhvbmUgLyBMaW5rZWRJbiAvIFBvcnRmb2xpbyIgLz4KICAgICAgICAgIDwvZGl2PgogICAgICAgIDwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9ImFjdGlvbnMiPgogICAgICAgICAgPGJ1dHRvbiBjbGFzcz0iYnRuIiB0eXBlPSJzdWJtaXQiPlNlbmQgRW1haWxzPC9idXR0b24+CiAgICAgICAgPC9kaXY+CiAgICAgIDwvZGl2PgogICAgPC9mb3JtPgogIDwvZGl2PgoKICA8c2NyaXB0PgogICAgY29uc3Qgc2FtcGxlQ29udGV4dCA9IHt7IHNhbXBsZV9jb250ZXh0fHRvanNvbiB9fTsKICAgIGNvbnN0IHRlbXBsYXRlcyA9IHt7IGVtYWlsX3RlbXBsYXRlc3x0b2pzb24gfX07CiAgICBjb25zdCB0ZW1wbGF0ZU1hcCA9IHt9OwogICAgdGVtcGxhdGVzLmZvckVhY2goKHRwbCkgPT4gewogICAgICB0ZW1wbGF0ZU1hcFt0cGwuaWRdID0gdHBsOwogICAgfSk7CiAgICBjb25zdCBzdWJqZWN0SW5wdXQgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgic3ViamVjdFRlbXBsYXRlIik7CiAgICBjb25zdCBib2R5SW5wdXQgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiYm9keVRlbXBsYXRlIik7CiAgICBjb25zdCBwcmV2aWV3U3ViamVjdCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJwcmV2aWV3U3ViamVjdCIpOwogICAgY29uc3QgcHJldmlld0JvZHkgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgicHJldmlld0JvZHkiKTsKICAgIGNvbnN0IGluY2x1ZGVMaW5rcyA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJpbmNsdWRlTGlua3MiKTsKICAgIGNvbnN0IGluY2x1ZGVBY2hpZXZlbWVudHMgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiaW5jbHVkZUFjaGlldmVtZW50cyIpOwogICAgY29uc3Qgc2VuZGVyTmFtZSA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJzZW5kZXJfbmFtZSIpOwogICAgY29uc3Qgc2VuZGVyQ29udGFjdCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJzZW5kZXJfY29udGFjdCIpOwoKICAgIGZ1bmN0aW9uIHJlbmRlclRlbXBsYXRlKHRlbXBsYXRlLCBjb250ZXh0KSB7CiAgICAgIGxldCByZW5kZXJlZCA9IHRlbXBsYXRlIHx8ICIiOwogICAgICBPYmplY3Qua2V5cyhjb250ZXh0IHx8IHt9KS5mb3JFYWNoKChrZXkpID0+IHsKICAgICAgICBjb25zdCB2YWx1ZSA9IGNvbnRleHRba2V5XSB8fCAiIjsKICAgICAgICByZW5kZXJlZCA9IHJlbmRlcmVkLnNwbGl0KGB7JHtrZXl9fWApLmpvaW4odmFsdWUpOwogICAgICB9KTsKICAgICAgcmVuZGVyZWQgPSByZW5kZXJlZC5yZXBsYWNlKC9ce1thLXpBLVowLTlfXStcfS9nLCAiIik7CiAgICAgIGNvbnN0IGxpbmVzID0gcmVuZGVyZWQuc3BsaXQoL1xyP1xuLyk7CiAgICAgIGNvbnN0IGNsZWFuZWQgPSBbXTsKICAgICAgbGluZXMuZm9yRWFjaCgobGluZSkgPT4gewogICAgICAgIGNvbnN0IHN0cmlwcGVkID0gbGluZS50cmltKCk7CiAgICAgICAgaWYgKCFzdHJpcHBlZCkgewogICAgICAgICAgaWYgKGNsZWFuZWQubGVuZ3RoICYmIGNsZWFuZWRbY2xlYW5lZC5sZW5ndGggLSAxXSA9PT0gIiIpIHsKICAgICAgICAgICAgcmV0dXJuOwogICAgICAgICAgfQogICAgICAgICAgY2xlYW5lZC5wdXNoKCIiKTsKICAgICAgICAgIHJldHVybjsKICAgICAgICB9CiAgICAgICAgaWYgKC9eWy3igKJdXHMqJC8udGVzdChzdHJpcHBlZCkpIHsKICAgICAgICAgIHJldHVybjsKICAgICAgICB9CiAgICAgICAgaWYgKC86XHMqJC8udGVzdChzdHJpcHBlZCkpIHsKICAgICAgICAgIHJldHVybjsKICAgICAgICB9CiAgICAgICAgY2xlYW5lZC5wdXNoKGxpbmUpOwogICAgICB9KTsKICAgICAgcmV0dXJuIGNsZWFuZWQuam9pbigiXG4iKS50cmltKCk7CiAgICB9CgogICAgZnVuY3Rpb24gY3VycmVudENvbnRleHQoKSB7CiAgICAgIGNvbnN0IGN0eCA9IHsgLi4uc2FtcGxlQ29udGV4dCB9OwogICAgICBpZiAoIWluY2x1ZGVMaW5rcy5jaGVja2VkKSB7CiAgICAgICAgY3R4LmFwcGx5X2xpbmtzID0gIiI7CiAgICAgICAgY3R4LnBvc3RfbGluayA9ICIiOwogICAgICB9CiAgICAgIGlmICghaW5jbHVkZUFjaGlldmVtZW50cy5jaGVja2VkKSB7CiAgICAgICAgY3R4LmFjaGlldmVtZW50cyA9ICIiOwogICAgICB9CiAgICAgIGN0eC5zZW5kZXJfbmFtZSA9IHNlbmRlck5hbWUudmFsdWUgfHwgY3R4LnNlbmRlcl9uYW1lIHx8ICJZb3VyIE5hbWUiOwogICAgICBjdHguc2VuZGVyX2NvbnRhY3QgPSBzZW5kZXJDb250YWN0LnZhbHVlIHx8ICIiOwogICAgICByZXR1cm4gY3R4OwogICAgfQoKICAgIGZ1bmN0aW9uIHVwZGF0ZVByZXZpZXcoKSB7CiAgICAgIGNvbnN0IGN0eCA9IGN1cnJlbnRDb250ZXh0KCk7CiAgICAgIGlmIChwcmV2aWV3U3ViamVjdCkgewogICAgICAgIHByZXZpZXdTdWJqZWN0LnRleHRDb250ZW50ID0gcmVuZGVyVGVtcGxhdGUoc3ViamVjdElucHV0LnZhbHVlLCBjdHgpOwogICAgICB9CiAgICAgIGlmIChwcmV2aWV3Qm9keSkgewogICAgICAgIHByZXZpZXdCb2R5LnRleHRDb250ZW50ID0gcmVuZGVyVGVtcGxhdGUoYm9keUlucHV0LnZhbHVlLCBjdHgpOwogICAgICB9CiAgICB9CgogICAgaWYgKHN1YmplY3RJbnB1dCAmJiBib2R5SW5wdXQpIHsKICAgICAgc3ViamVjdElucHV0LmFkZEV2ZW50TGlzdGVuZXIoImlucHV0IiwgdXBkYXRlUHJldmlldyk7CiAgICAgIGJvZHlJbnB1dC5hZGRFdmVudExpc3RlbmVyKCJpbnB1dCIsIHVwZGF0ZVByZXZpZXcpOwogICAgfQogICAgaWYgKGluY2x1ZGVMaW5rcykgewogICAgICBpbmNsdWRlTGlua3MuYWRkRXZlbnRMaXN0ZW5lcigiY2hhbmdlIiwgdXBkYXRlUHJldmlldyk7CiAgICB9CiAgICBpZiAoaW5jbHVkZUFjaGlldmVtZW50cykgewogICAgICBpbmNsdWRlQWNoaWV2ZW1lbnRzLmFkZEV2ZW50TGlzdGVuZXIoImNoYW5nZSIsIHVwZGF0ZVByZXZpZXcpOwogICAgfQogICAgaWYgKHNlbmRlck5hbWUpIHsKICAgICAgc2VuZGVyTmFtZS5hZGRFdmVudExpc3RlbmVyKCJpbnB1dCIsIHVwZGF0ZVByZXZpZXcpOwogICAgfQogICAgaWYgKHNlbmRlckNvbnRhY3QpIHsKICAgICAgc2VuZGVyQ29udGFjdC5hZGRFdmVudExpc3RlbmVyKCJpbnB1dCIsIHVwZGF0ZVByZXZpZXcpOwogICAgfQoKICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoIltkYXRhLXRlbXBsYXRlLWNhcmRdIGlucHV0W3R5cGU9J3JhZGlvJ10iKS5mb3JFYWNoKChpbnB1dCkgPT4gewogICAgICBpbnB1dC5hZGRFdmVudExpc3RlbmVyKCJjaGFuZ2UiLCAoKSA9PiB7CiAgICAgICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgiW2RhdGEtdGVtcGxhdGUtY2FyZF0iKS5mb3JFYWNoKChjYXJkKSA9PiB7CiAgICAgICAgICBjYXJkLmNsYXNzTGlzdC5yZW1vdmUoImFjdGl2ZSIpOwogICAgICAgIH0pOwogICAgICAgIGlucHV0LmNsb3Nlc3QoIltkYXRhLXRlbXBsYXRlLWNhcmRdIikuY2xhc3NMaXN0LmFkZCgiYWN0aXZlIik7CiAgICAgICAgY29uc3QgdHBsID0gdGVtcGxhdGVNYXBbaW5wdXQudmFsdWVdOwogICAgICAgIGlmICh0cGwgJiYgdHBsLnN1YmplY3QpIHsKICAgICAgICAgIHN1YmplY3RJbnB1dC52YWx1ZSA9IHRwbC5zdWJqZWN0OwogICAgICAgIH0KICAgICAgICBpZiAodHBsICYmIHRwbC5ib2R5KSB7CiAgICAgICAgICBib2R5SW5wdXQudmFsdWUgPSB0cGwuYm9keTsKICAgICAgICB9CiAgICAgICAgdXBkYXRlUHJldmlldygpOwogICAgICB9KTsKICAgIH0pOwoKICAgIHVwZGF0ZVByZXZpZXcoKTsKICA8L3NjcmlwdD4KeyUgZW5kYmxvY2sgJX0K","email_select.html":"eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBjb250ZW50ICV9CiAgPGRpdiBjbGFzcz0icGFnZSI+CiAgICA8aGVhZGVyIGNsYXNzPSJoZWFkZXIiPgogICAgICA8ZGl2IGNsYXNzPSJpY29uLWJhZGdlIj4KICAgICAgICA8c3ZnIHdpZHRoPSIyNiIgaGVpZ2h0PSIyNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgIDxwYXRoIGQ9Ik00IDZoMTZ2MTJINFY2eiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICAgIDxwYXRoIGQ9Ik00IDdsOCA2IDgtNiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICA8L3N2Zz4KICAgICAgPC9kaXY+CiAgICAgIDxkaXY+CiAgICAgICAgPGgxPlNlbGVjdCBSZWNpcGllbnRzPC9oMT4KICAgICAgICA8cCBjbGFzcz0ic3VidGl0bGUiPkNob29zZSB3aG8gcmVjZWl2ZXMgYSBwZXJzb25hbGl6ZWQgZW1haWwsIG9yIGFkZCBjdXN0b20gcm93cy48L3A+CiAgICAgIDwvZGl2PgogICAgPC9oZWFkZXI+CgogICAgPGRpdiBjbGFzcz0iY2FyZCI+CiAgICAgIHslIGlmIGVycm9yICV9CiAgICAgICAgPGRpdiBjbGFzcz0ic3RhdHVzIGVycm9yIj57eyBlcnJvciB9fTwvZGl2PgogICAgICB7JSBlbHNlICV9CiAgICAgICAgPGRpdiBjbGFzcz0ic3RhdHMtZ3JpZCI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJzdGF0Ij4KICAgICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPlRvdGFsIExlYWRzPC9zcGFuPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC12YWx1ZSI+e3sgc3RhdHMudG90YWxfcm93cyB9fTwvc3Bhbj4KICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPGRpdiBjbGFzcz0ic3RhdCI+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LWxhYmVsIj5VbmlxdWUgRW1haWxzPC9zcGFuPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC12YWx1ZSI+e3sgc3RhdHMudW5pcXVlX2VtYWlscyB9fTwvc3Bhbj4KICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPGRpdiBjbGFzcz0ic3RhdCI+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LWxhYmVsIj5Db21wYW5pZXM8L3NwYW4+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LXZhbHVlIj57eyBzdGF0cy5jb21wYW5pZXMgfX08L3NwYW4+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9InN0YXQiPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC1sYWJlbCI+TWlzc2luZyBBcHBseSBMaW5rczwvc3Bhbj4KICAgICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtdmFsdWUiPnt7IHN0YXRzLm1pc3NpbmdfYXBwbHkgfX08L3NwYW4+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICA8L2Rpdj4KICAgICAgICA8cCBjbGFzcz0ibm90ZSI+TG9hZGVkIGZyb206IDxzdHJvbmc+e3sgZmlsZV9uYW1lIH19PC9zdHJvbmc+PC9wPgogICAgICAgIDxmb3JtIG1ldGhvZD0icG9zdCIgYWN0aW9uPSIvZW1haWwvY29tcG9zZSI+CiAgICAgICAgICA8aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJzZXRfaWQiIHZhbHVlPSJ7eyBzZXRfaWQgfX0iIC8+CgogICAgICAgICAgPGRpdiBjbGFzcz0iZmlsdGVyLWJhciI+CiAgICAgICAgICAgIDxpbnB1dCBpZD0iZmlsdGVySW5wdXQiIGNsYXNzPSJmaWx0ZXItaW5wdXQiIHR5cGU9InRleHQiIHBsYWNlaG9sZGVyPSJTZWFyY2ggYnkgZW1haWwsIGNvbXBhbnksIG9yIHBvc3QgdGV4dCIgLz4KICAgICAgICAgICAgPGRpdiBjbGFzcz0ibm90ZSI+VmlzaWJsZTogPHNwYW4gaWQ9InZpc2libGVDb3VudCI+e3sgcGFnZV9jb3VudCB9fTwvc3Bhbj4gLyB7eyBzdGF0cy50b3RhbF9yb3dzIH19PC9kaXY+CiAgICAgICAgICA8L2Rpdj4KCiAgICAgICAgICA8ZGl2IGNsYXNzPSJ0b29sYmFyIj4KICAgICAgICAgICAgPGxhYmVsPjxpbnB1dCB0eXBlPSJjaGVja2JveCIgaWQ9InNlbGVjdEFsbCIgLz4gU2VsZWN0IGFsbDwvbGFiZWw+CiAgICAgICAgICAgIDxidXR0b24gY2xhc3M9ImJ0biBidG4tc2Vjb25kYXJ5IiB0eXBlPSJzdWJtaXQiPkNvbnRpbnVlPC9idXR0b24+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9InBhZ2VyIj4KICAgICAgICAgICAgICB7JSBpZiB2aWV3X2FsbCAlfQogICAgICAgICAgICAgICAgPGEgY2xhc3M9ImJ0biBidG4tZ2hvc3QiIGhyZWY9Ii9lbWFpbD9wYWdlPTEiPlBhZ2luYXRlPC9hPgogICAgICAgICAgICAgIHslIGVsc2UgJX0KICAgICAgICAgICAgICAgIDxhIGNsYXNzPSJidG4gYnRuLWdob3N0IiBocmVmPSIvZW1haWw/dmlldz1hbGwiPkV4cGFuZCBhbGw8L2E+CiAgICAgICAgICAgICAgICB7JSBpZiBwYWdlID4gMSAlfQogICAgICAgICAgICAgICAgICA8YSBjbGFzcz0iYnRuIGJ0bi1naG9zdCIgaHJlZj0iL2VtYWlsP3BhZ2U9e3sgcGFnZSAtIDEgfX0iPlByZXY8L2E+CiAgICAgICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgICAgICAgeyUgaWYgcGFnZSA8IHRvdGFsX3BhZ2VzICV9CiAgICAgICAgICAgICAgICAgIDxhIGNsYXNzPSJidG4gYnRuLWdob3N0IiBocmVmPSIvZW1haWw/cGFnZT17eyBwYWdlICsgMSB9fSI+TmV4dDwvYT4KICAgICAgICAgICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgICAgICAgICA8c3BhbiBjbGFzcz0ibm90ZSI+UGFnZSB7eyBwYWdlIH19IC8ge3sgdG90YWxfcGFnZXMgfX08L3NwYW4+CiAgICAgICAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8L2Rpdj4KCiAgICAgICAgICA8dGFibGUgY2xhc3M9InRhYmxlIj4KICAgICAgICAgICAgPHRoZWFkPgogICAgICAgICAgICAgIDx0cj4KICAgICAgICAgICAgICAgIDx0aD48L3RoPgogICAgICAgICAgICAgICAgPHRoPkVtYWlsPC90aD4KICAgICAgICAgICAgICAgIDx0aD5Db21wYW55PC90aD4KICAgICAgICAgICAgICAgIDx0aD5BcHBseSBMaW5rczwvdGg+CiAgICAgICAgICAgICAgICA8dGg+UG9zdCBUZXh0PC90aD4KICAgICAgICAgICAgICA8L3RyPgogICAgICAgICAgICA8L3RoZWFkPgogICAgICAgICAgICA8dGJvZHk+CiAgICAgICAgICAgICAgeyUgZm9yIHJvdyBpbiByb3dzICV9CiAgICAgICAgICAgICAgICA8dHI+CiAgICAgICAgICAgICAgICAgIDx0ZD48aW5wdXQgdHlwZT0iY2hlY2tib3giIG5hbWU9InNlbGVjdGVkIiB2YWx1ZT0ie3sgcm93Ll9pZHggfX0iIC8+PC90ZD4KICAgICAgICAgICAgICAgICAgPHRkPnt7IHJvdy5lbWFpbCB9fTwvdGQ+CiAgICAgICAgICAgICAgICAgIDx0ZD57eyByb3cuY29tcGFueSB9fTwvdGQ+CiAgICAgICAgICAgICAgICAgIDx0ZCBjbGFzcz0idHJ1bmNhdGUiPgogICAgICAgICAgICAgICAgICAgIHslIGlmIHJvdy5hcHBseV9saW5rcyAlfQogICAgICAgICAgICAgICAgICAgICAgeyUgc2V0IGxpbmtzID0gcm93LmFwcGx5X2xpbmtzLnJlcGxhY2UoJywnLCAnOycpLnNwbGl0KCc7JykgJX0KICAgICAgICAgICAgICAgICAgICAgIHslIGZvciBsaW5rIGluIGxpbmtzICV9CiAgICAgICAgICAgICAgICAgICAgICAgIHslIHNldCB0cmltbWVkID0gbGlua3x0cmltICV9CiAgICAgICAgICAgICAgICAgICAgICAgIHslIGlmIHRyaW1tZWQgJX0KICAgICAgICAgICAgICAgICAgICAgICAgICA8YSBjbGFzcz0idGFibGUtbGluayIgaHJlZj0ie3sgdHJpbW1lZCB9fSIgdGFyZ2V0PSJfYmxhbmsiIHJlbD0ibm9vcGVuZXIiPnt7IHRyaW1tZWQgfX08L2E+eyUgaWYgbm90IGxvb3AubGFzdCAlfTxicj57JSBlbmRpZiAlfQogICAgICAgICAgICAgICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgICAgICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgICAgICAgICAgICAgeyUgZWxzZSAlfQogICAgICAgICAgICAgICAgICAgICAg4oCUCiAgICAgICAgICAgICAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgICAgICAgICAgICAgPC90ZD4KICAgICAgICAgICAgICAgICAgPHRkPgogICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9InBvc3QtdGV4dC1jZWxsIj4KICAgICAgICAgICAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJ0cnVuY2F0ZSI+e3sgcm93LnBvc3RfdGV4dFs6MTQwXSBpZiByb3cucG9zdF90ZXh0IGVsc2UgIiIgfX08L3NwYW4+CiAgICAgICAgICAgICAgICAgICAgICB7JSBpZiByb3cucG9zdF90ZXh0ICV9CiAgICAgICAgICAgICAgICAgICAgICAgIDxidXR0b24gdHlwZT0iYnV0dG9uIiBjbGFzcz0icG9zdC12aWV3LWJ0biIgYXJpYS1sYWJlbD0iVmlldyBmdWxsIHBvc3QiIGRhdGEtcG9zdD0ie3sgcm93LnBvc3RfdGV4dCB8IGUgfX0iPgogICAgICAgICAgICAgICAgICAgICAgICAgIDxzdmcgdmlld0JveD0iMCAwIDI0IDI0IiBhcmlhLWhpZGRlbj0idHJ1ZSI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8cGF0aCBkPSJNNiA0aDlsMyAzdjEzSDZWNHoiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNiIvPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTkgMTBoNk05IDE0aDZNOSAxOGg0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogICAgICAgICAgICAgICAgICAgICAgICAgIDwvc3ZnPgogICAgICAgICAgICAgICAgICAgICAgICA8L2J1dHRvbj4KICAgICAgICAgICAgICAgICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICAgIDwvdGQ+CiAgICAgICAgICAgICAgICA8L3RyPgogICAgICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgICAgICA8L3Rib2R5PgogICAgICAgICAgPC90YWJsZT4KCiAgICAgICAgICA8ZGl2IGNsYXNzPSJjYXJkIiBzdHlsZT0ibWFyZ2luLXRvcDoxOHB4OyI+CiAgICAgICAgICAgIDxoMz5BZGQgQ3VzdG9tIFJvd3M8L2gzPgogICAgICAgICAgICA8ZGl2IGlkPSJjdXN0b21Sb3dzIj4KICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJncmlkIHR3byI+CiAgICAgICAgICAgICAgICA8aW5wdXQgbmFtZT0iY3VzdG9tX2VtYWlsIiBwbGFjZWhvbGRlcj0iZW1haWxAZXhhbXBsZS5jb20iIC8+CiAgICAgICAgICAgICAgICA8aW5wdXQgbmFtZT0iY3VzdG9tX2NvbXBhbnkiIHBsYWNlaG9sZGVyPSJDb21wYW55IChvcHRpb25hbCkiIC8+CiAgICAgICAgICAgICAgICA8aW5wdXQgbmFtZT0iY3VzdG9tX3Bvc3RfbGluayIgcGxhY2Vob2xkZXI9IlBvc3QgbGluayAob3B0aW9uYWwpIiAvPgogICAgICAgICAgICAgICAgPGlucHV0IG5hbWU9ImN1c3RvbV9hcHBseV9saW5rcyIgcGxhY2Vob2xkZXI9IkFwcGx5IGxpbmsgKG9wdGlvbmFsKSIgLz4KICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImFjdGlvbnMiPgogICAgICAgICAgICAgIDxidXR0b24gY2xhc3M9ImJ0biBidG4tZ2hvc3QiIHR5cGU9ImJ1dHRvbiIgb25jbGljaz0iYWRkUm93KCkiPkFkZCBSb3c8L2J1dHRvbj4KICAgICAgICAgICAgICA8YnV0dG9uIGNsYXNzPSJidG4gYnRuLXNlY29uZGFyeSIgdHlwZT0ic3VibWl0Ij5Db250aW51ZTwvYnV0dG9uPgogICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDwvZGl2PgogICAgICAgIDwvZm9ybT4KICAgICAgeyUgZW5kaWYgJX0KICAgIDwvZGl2PgogIDwvZGl2PgoKICA8ZGl2IGlkPSJwb3N0TW9kYWwiIGNsYXNzPSJwb3N0LW1vZGFsIiBhcmlhLWhpZGRlbj0idHJ1ZSI+CiAgICA8ZGl2IGNsYXNzPSJwb3N0LW1vZGFsLWJhY2tkcm9wIj48L2Rpdj4KICAgIDxkaXYgY2xhc3M9InBvc3QtbW9kYWwtY2FyZCI+CiAgICAgIDxkaXYgY2xhc3M9InBvc3QtbW9kYWwtaGVhZCI+CiAgICAgICAgPGgzPlBvc3QgdGV4dDwvaDM+CiAgICAgICAgPGJ1dHRvbiB0eXBlPSJidXR0b24iIGNsYXNzPSJwb3N0LW1vZGFsLWNsb3NlIiBkYXRhLWNsb3NlLXBvc3QtbW9kYWw+Q2xvc2U8L2J1dHRvbj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgaWQ9InBvc3RNb2RhbENvbnRlbnQiIGNsYXNzPSJwb3N0LW1vZGFsLWJvZHkiPjwvZGl2PgogICAgPC9kaXY+CiAgPC9kaXY+CgogIDxzY3JpcHQ+CiAgICBjb25zdCBzZWxlY3RBbGwgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgic2VsZWN0QWxsIik7CiAgICBpZiAoc2VsZWN0QWxsKSB7CiAgICAgIHNlbGVjdEFsbC5hZGRFdmVudExpc3RlbmVyKCJjaGFuZ2UiLCAoZSkgPT4gewogICAgICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJ2lucHV0W25hbWU9InNlbGVjdGVkIl0nKS5mb3JFYWNoKChjYikgPT4gewogICAgICAgICAgY2IuY2hlY2tlZCA9IGUudGFyZ2V0LmNoZWNrZWQ7CiAgICAgICAgfSk7CiAgICAgIH0pOwogICAgfQogICAgY29uc3QgZmlsdGVySW5wdXQgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiZmlsdGVySW5wdXQiKTsKICAgIGNvbnN0IHZpc2libGVDb3VudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJ2aXNpYmxlQ291bnQiKTsKICAgIGlmIChmaWx0ZXJJbnB1dCkgewogICAgICBjb25zdCByb3dzID0gQXJyYXkuZnJvbShkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCJ0Ym9keSB0ciIpKTsKICAgICAgZmlsdGVySW5wdXQuYWRkRXZlbnRMaXN0ZW5lcigiaW5wdXQiLCAoKSA9PiB7CiAgICAgICAgY29uc3QgcXVlcnkgPSBmaWx0ZXJJbnB1dC52YWx1ZS50cmltKCkudG9Mb3dlckNhc2UoKTsKICAgICAgICBsZXQgdmlzaWJsZSA9IDA7CiAgICAgICAgcm93cy5mb3JFYWNoKChyb3cpID0+IHsKICAgICAgICAgIGNvbnN0IHRleHQgPSByb3cudGV4dENvbnRlbnQudG9Mb3dlckNhc2UoKTsKICAgICAgICAgIGNvbnN0IHNob3cgPSAhcXVlcnkgfHwgdGV4dC5pbmNsdWRlcyhxdWVyeSk7CiAgICAgICAgICByb3cuc3R5bGUuZGlzcGxheSA9IHNob3cgPyAiIiA6ICJub25lIjsKICAgICAgICAgIGlmIChzaG93KSB2aXNpYmxlICs9IDE7CiAgICAgICAgfSk7CiAgICAgICAgaWYgKHZpc2libGVDb3VudCkgewogICAgICAgICAgdmlzaWJsZUNvdW50LnRleHRDb250ZW50ID0gdmlzaWJsZTsKICAgICAgICB9CiAgICAgIH0pOwogICAgfQogICAgZnVuY3Rpb24gYWRkUm93KCkgewogICAgICBjb25zdCBjb250YWluZXIgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiY3VzdG9tUm93cyIpOwogICAgICBjb25zdCBkaXYgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCJkaXYiKTsKICAgICAgZGl2LmNsYXNzTmFtZSA9ICJncmlkIHR3byI7CiAgICAgIGRpdi5pbm5lckhUTUwgPSBgCiAgICAgICAgPGlucHV0IG5hbWU9ImN1c3RvbV9lbWFpbCIgcGxhY2Vob2xkZXI9ImVtYWlsQGV4YW1wbGUuY29tIiAvPgogICAgICAgIDxpbnB1dCBuYW1lPSJjdXN0b21fY29tcGFueSIgcGxhY2Vob2xkZXI9IkNvbXBhbnkgKG9wdGlvbmFsKSIgLz4KICAgICAgICA8aW5wdXQgbmFtZT0iY3VzdG9tX3Bvc3RfbGluayIgcGxhY2Vob2xkZXI9IlBvc3QgbGluayAob3B0aW9uYWwpIiAvPgogICAgICAgIDxpbnB1dCBuYW1lPSJjdXN0b21fYXBwbHlfbGlua3MiIHBsYWNlaG9sZGVyPSJBcHBseSBsaW5rIChvcHRpb25hbCkiIC8+CiAgICAgIGA7CiAgICAgIGNvbnRhaW5lci5hcHBlbmRDaGlsZChkaXYpOwogICAgfQoKICAgIGNvbnN0IHBvc3RNb2RhbCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJwb3N0TW9kYWwiKTsKICAgIGNvbnN0IHBvc3RNb2RhbENvbnRlbnQgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgicG9zdE1vZGFsQ29udGVudCIpOwogICAgY29uc3QgY2xvc2VNb2RhbEJ1dHRvbnMgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCJbZGF0YS1jbG9zZS1wb3N0LW1vZGFsXSIpOwogICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgiLnBvc3Qtdmlldy1idG4iKS5mb3JFYWNoKChidG4pID0+IHsKICAgICAgYnRuLmFkZEV2ZW50TGlzdGVuZXIoImNsaWNrIiwgKCkgPT4gewogICAgICAgIGNvbnN0IHRleHQgPSBidG4uZ2V0QXR0cmlidXRlKCJkYXRhLXBvc3QiKSB8fCAiIjsKICAgICAgICBpZiAocG9zdE1vZGFsQ29udGVudCkgewogICAgICAgICAgcG9zdE1vZGFsQ29udGVudC50ZXh0Q29udGVudCA9IHRleHQ7CiAgICAgICAgfQogICAgICAgIGlmIChwb3N0TW9kYWwpIHsKICAgICAgICAgIHBvc3RNb2RhbC5jbGFzc0xpc3QuYWRkKCJvcGVuIik7CiAgICAgICAgICBwb3N0TW9kYWwuc2V0QXR0cmlidXRlKCJhcmlhLWhpZGRlbiIsICJmYWxzZSIpOwogICAgICAgIH0KICAgICAgfSk7CiAgICB9KTsKICAgIGNsb3NlTW9kYWxCdXR0b25zLmZvckVhY2goKGJ0bikgPT4gewogICAgICBidG4uYWRkRXZlbnRMaXN0ZW5lcigiY2xpY2siLCAoKSA9PiB7CiAgICAgICAgaWYgKHBvc3RNb2RhbCkgewogICAgICAgICAgcG9zdE1vZGFsLmNsYXNzTGlzdC5yZW1vdmUoIm9wZW4iKTsKICAgICAgICAgIHBvc3RNb2RhbC5zZXRBdHRyaWJ1dGUoImFyaWEtaGlkZGVuIiwgInRydWUiKTsKICAgICAgICB9CiAgICAgIH0pOwogICAgfSk7CiAgICBpZiAocG9zdE1vZGFsKSB7CiAgICAgIHBvc3RNb2RhbC5hZGRFdmVudExpc3RlbmVyKCJjbGljayIsIChlKSA9PiB7CiAgICAgICAgaWYgKGUudGFyZ2V0LmNsYXNzTGlzdC5jb250YWlucygicG9zdC1tb2RhbC1iYWNrZHJvcCIpKSB7CiAgICAgICAgICBwb3N0TW9kYWwuY2xhc3NMaXN0LnJlbW92ZSgib3BlbiIpOwogICAgICAgICAgcG9zdE1vZGFsLnNldEF0dHJpYnV0ZSgiYXJpYS1oaWRkZW4iLCAidHJ1ZSIpOwogICAgICAgIH0KICAgICAgfSk7CiAgICB9CiAgICBkb2N1bWVudC5hZGRFdmVudExpc3RlbmVyKCJrZXlkb3duIiwgKGUpID0+IHsKICAgICAgaWYgKGUua2V5ID09PSAiRXNjYXBlIiAmJiBwb3N0TW9kYWwgJiYgcG9zdE1vZGFsLmNsYXNzTGlzdC5jb250YWlucygib3BlbiIpKSB7CiAgICAgICAgcG9zdE1vZGFsLmNsYXNzTGlzdC5yZW1vdmUoIm9wZW4iKTsKICAgICAgICBwb3N0TW9kYWwuc2V0QXR0cmlidXRlKCJhcmlhLWhpZGRlbiIsICJ0cnVlIik7CiAgICAgIH0KICAgIH0pOwogIDwvc2NyaXB0Pgp7JSBlbmRibG9jayAlfQo=","email_start.html":"eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBjb250ZW50ICV9CiAgICA8ZGl2IGNsYXNzPSJwYWdlIj4KICAgIDxoZWFkZXIgY2xhc3M9ImhlYWRlciI+CiAgICAgIDxkaXYgY2xhc3M9Imljb24tYmFkZ2UiPgogICAgICAgIDxzdmcgd2lkdGg9IjI2IiBoZWlnaHQ9IjI2IiB2aWV3Qm94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiPgogICAgICAgICAgPHBhdGggZD0iTTQgNmgxNnYxMkg0VjZ6IiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjEuNiIvPgogICAgICAgICAgPHBhdGggZD0iTTQgN2w4IDYgOC02IiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjEuNiIvPgogICAgICAgIDwvc3ZnPgogICAgICA8L2Rpdj4KICAgICAgPGRpdj4KICAgICAgICA8aDE+RW1haWwgQXV0b21hdGlvbjwvaDE+CiAgICAgICAgPHAgY2xhc3M9InN1YnRpdGxlIj5VcGxvYWQgeW91ciByZXN1bWUgYW5kIGxldCB0aGUgYWdlbnQgcHJlcGFyZSBwcm9mZXNzaW9uYWwgb3V0cmVhY2guPC9wPgogICAgICA8L2Rpdj4KICAgIDwvaGVhZGVyPgoKICAgIDxkaXYgY2xhc3M9ImNhcmQiPgogICAgICB7JSBpZiBlcnJvciAlfQogICAgICAgIDxkaXYgY2xhc3M9InN0YXR1cyBlcnJvciI+e3sgZXJyb3IgfX08L2Rpdj4KICAgICAgeyUgZW5kaWYgJX0KICAgICAgeyUgaWYgZmlsZV9uYW1lICV9CiAgICAgICAgPHAgY2xhc3M9Im5vdGUiPlVzaW5nIGZpbGU6IDxzdHJvbmc+e3sgZmlsZV9uYW1lIH19PC9zdHJvbmc+PC9wPgogICAgICB7JSBlbmRpZiAlfQoKICAgICAgPGZvcm0gbWV0aG9kPSJwb3N0IiBhY3Rpb249Ii9lbWFpbC9zdGFydCIgZW5jdHlwZT0ibXVsdGlwYXJ0L2Zvcm0tZGF0YSIgY2xhc3M9InN0YWdnZXIiPgogICAgICAgIDxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InNldF9pZCIgdmFsdWU9Int7IHNldF9pZCB9fSIgLz4KICAgICAgICA8ZGl2IGNsYXNzPSJmaWVsZCI+CiAgICAgICAgICA8bGFiZWwgZm9yPSJyZXN1bWUiPlVwbG9hZCByZXN1bWUgKFBERiBvciBET0NYKTwvbGFiZWw+CiAgICAgICAgICA8aW5wdXQgaWQ9InJlc3VtZSIgbmFtZT0icmVzdW1lIiB0eXBlPSJmaWxlIiByZXF1aXJlZCAvPgogICAgICAgIDwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9ImFjdGlvbnMiPgogICAgICAgICAgPGJ1dHRvbiBjbGFzcz0iYnRuIiB0eXBlPSJzdWJtaXQiPkNvbnRpbnVlPC9idXR0b24+CiAgICAgICAgPC9kaXY+CiAgICAgIDwvZm9ybT4KICAgIDwvZGl2PgogIDwvZGl2Pgp7JSBlbmRibG9jayAlfQo=","email_status.html":"eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBjb250ZW50ICV9CiAgPGRpdiBjbGFzcz0icGFnZSI+CiAgICA8aGVhZGVyIGNsYXNzPSJoZWFkZXIiPgogICAgICA8ZGl2IGNsYXNzPSJpY29uLWJhZGdlIj4KICAgICAgICA8c3ZnIHdpZHRoPSIyNiIgaGVpZ2h0PSIyNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgIDxwYXRoIGQ9Ik00IDZoMTZ2MTJINFY2eiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICAgIDxwYXRoIGQ9Ik00IDdsOCA2IDgtNiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICA8L3N2Zz4KICAgICAgPC9kaXY+CiAgICAgIDxkaXY+CiAgICAgICAgPGgxPkVtYWlsIFByb2dyZXNzPC9oMT4KICAgICAgICA8cCBjbGFzcz0ic3VidGl0bGUiPlNlbmRpbmcgcGVyc29uYWxpemVkIGVtYWlscyBvbmUgYnkgb25lLjwvcD4KICAgICAgPC9kaXY+CiAgICA8L2hlYWRlcj4KCiAgICA8ZGl2IGNsYXNzPSJjYXJkIj4KICAgICAgeyUgaWYgZXJyb3IgJX0KICAgICAgICA8ZGl2IGNsYXNzPSJzdGF0dXMgZXJyb3IiPnt7IGVycm9yIH19PC9kaXY+CiAgICAgIHslIGVsc2UgJX0KICAgICAgICA8ZGl2IGlkPSJzdGF0dXMiIGNsYXNzPSJzdGF0dXMiPlN0YXJ0aW5n4oCmPC9kaXY+CiAgICAgICAgPGRpdiBpZD0iZGV0YWlsIiBjbGFzcz0ibm90ZSI+PC9kaXY+CiAgICAgICAgPGRpdiBpZD0iZG93bmxvYWQiIGNsYXNzPSJub3RlIj48L2Rpdj4KICAgICAgeyUgZW5kaWYgJX0KICAgIDwvZGl2PgogIDwvZGl2PgoKICB7JSBpZiBub3QgZXJyb3IgJX0KICA8c2NyaXB0PgogICAgY29uc3Qgam9iSWQgPSAie3sgam9iX2lkIH19IjsKICAgIGNvbnN0IHN0YXR1c0VsID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInN0YXR1cyIpOwogICAgY29uc3QgZGV0YWlsRWwgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiZGV0YWlsIik7CiAgICBjb25zdCBkb3dubG9hZEVsID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoImRvd25sb2FkIik7CgogICAgYXN5bmMgZnVuY3Rpb24gcG9sbCgpIHsKICAgICAgY29uc3QgcmVzID0gYXdhaXQgZmV0Y2goYC9lbWFpbC9zdGF0dXMvJHtqb2JJZH1gKTsKICAgICAgY29uc3QgZGF0YSA9IGF3YWl0IHJlcy5qc29uKCk7CgogICAgICBpZiAoZGF0YS5lcnJvcikgewogICAgICAgIHN0YXR1c0VsLnRleHRDb250ZW50ID0gIkVycm9yIjsKICAgICAgICBzdGF0dXNFbC5jbGFzc05hbWUgPSAic3RhdHVzIGVycm9yIjsKICAgICAgICBkZXRhaWxFbC50ZXh0Q29udGVudCA9IGRhdGEuZXJyb3I7CiAgICAgICAgcmV0dXJuOwogICAgICB9CgogICAgICBzdGF0dXNFbC50ZXh0Q29udGVudCA9IGRhdGEuc3RhdHVzOwogICAgICBkZXRhaWxFbC50ZXh0Q29udGVudCA9IGBTZW50OiAke2RhdGEuc2VudH0gfCBGYWlsZWQ6ICR7ZGF0YS5mYWlsZWR9IHwgVG90YWw6ICR7ZGF0YS50b3RhbH0gfCBVcGRhdGVkOiAke2RhdGEudXBkYXRlZF9hdH1gOwoKICAgICAgaWYgKGRhdGEuZG9uZSkgewogICAgICAgIGlmIChkYXRhLmVycm9yKSB7CiAgICAgICAgICBzdGF0dXNFbC5jbGFzc05hbWUgPSAic3RhdHVzIGVycm9yIjsKICAgICAgICAgIGRldGFpbEVsLnRleHRDb250ZW50ID0gZGF0YS5lcnJvcjsKICAgICAgICB9IGVsc2UgewogICAgICAgICAgc3RhdHVzRWwuY2xhc3NOYW1lID0gInN0YXR1cyBkb25lIjsKICAgICAgICAgIGlmIChkYXRhLmxvZ19maWxlKSB7CiAgICAgICAgICAgIGRvd25sb2FkRWwuaW5uZXJIVE1MID0gYDxhIGNsYXNzPSJsaW5rLWJ0biIgaHJlZj0iL2Rvd25sb2FkLyR7ZGF0YS5sb2dfZmlsZX0iPkRvd25sb2FkIHNlbmQgbG9nPC9hPmA7CiAgICAgICAgICB9CiAgICAgICAgfQogICAgICAgIHJldHVybjsKICAgICAgfQogICAgICBzZXRUaW1lb3V0KHBvbGwsIDIwMDApOwogICAgfQogICAgcG9sbCgpOwogIDwvc2NyaXB0PgogIHslIGVuZGlmICV9CnslIGVuZGJsb2NrICV9Cg==","home.html":"eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBjb250ZW50ICV9CiAgPGRpdiBjbGFzcz0icGFnZSI+CiAgICA8aGVhZGVyIGNsYXNzPSJoZWFkZXIiPgogICAgICA8ZGl2IGNsYXNzPSJpY29uLWJhZGdlIj4KICAgICAgICA8c3ZnIHdpZHRoPSIyNiIgaGVpZ2h0PSIyNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgIDxwYXRoIGQ9Ik00IDdoMTZ2MTBINFY3eiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICAgIDxwYXRoIGQ9Ik04IDd2LTJoOHYyIiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjEuNiIvPgogICAgICAgIDwvc3ZnPgogICAgICA8L2Rpdj4KICAgICAgPGRpdj4KICAgICAgICA8aDE+RGFzaGJvYXJkPC9oMT4KICAgICAgICA8cCBjbGFzcz0ic3VidGl0bGUiPk1ldHJpY3MsIHNjb3JlcywgYW5kIGF1dG9tYXRpb24gYXQgYSBnbGFuY2UuPC9wPgogICAgICA8L2Rpdj4KICAgIDwvaGVhZGVyPgoKICAgIDxkaXYgY2xhc3M9Im1ldHJpY3MiPgogICAgICA8ZGl2IGNsYXNzPSJtZXRyaWMtY2FyZCI+CiAgICAgICAgPGg0PlRvdGFsIEVtYWlscyBGb3VuZDwvaDQ+CiAgICAgICAgPGRpdiBjbGFzcz0ibWV0cmljLXZhbHVlIj57eyBtZXRyaWNzLnRvdGFsX2VtYWlscyB9fTwvZGl2PgogICAgICAgIDxwIGNsYXNzPSJub3RlIj5Gcm9tIGxhdGVzdCBtYXN0ZXIgcXVhbGl0eSBzY2FuLjwvcD4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9Im1ldHJpYy1jYXJkIj4KICAgICAgICA8aDQ+VG90YWwgRW1haWxzIFNlbnQ8L2g0PgogICAgICAgIDxkaXYgY2xhc3M9Im1ldHJpYy12YWx1ZSI+e3sgbWV0cmljcy50b3RhbF9zZW50IH19PC9kaXY+CiAgICAgICAgPHAgY2xhc3M9Im5vdGUiPkxhdGVzdCBlbWFpbCBhdXRvbWF0aW9uIHJ1bi48L3A+CiAgICAgIDwvZGl2PgogICAgICA8YnV0dG9uCiAgICAgICAgdHlwZT0iYnV0dG9uIgogICAgICAgIGNsYXNzPSJtZXRyaWMtY2FyZCBtZXRyaWMtY2FyZC1idXR0b24iCiAgICAgICAgaWQ9Im9wZW5SYXRlQW5hbHl0aWNzQnV0dG9uIgogICAgICAgIGFyaWEtaGFzcG9wdXA9ImRpYWxvZyIKICAgICAgICBhcmlhLWNvbnRyb2xzPSJ0cmFja2luZ0FuYWx5dGljc01vZGFsIgogICAgICA+CiAgICAgICAgPGRpdiBjbGFzcz0ibWV0cmljLWNhcmQtaGVhZCI+CiAgICAgICAgICA8aDQ+T3BlbiBSYXRlPC9oND4KICAgICAgICAgIDxzcGFuIGNsYXNzPSJtZXRyaWMtb3Blbi1pY29uIiBhcmlhLWhpZGRlbj0idHJ1ZSI+CiAgICAgICAgICAgIDxzdmcgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgICAgICA8cGF0aCBkPSJNNyAxN0wxNyA3IiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjgiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogICAgICAgICAgICAgIDxwYXRoIGQ9Ik05IDdoOHY4IiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIxLjgiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPgogICAgICAgICAgICA8L3N2Zz4KICAgICAgICAgIDwvc3Bhbj4KICAgICAgICA8L2Rpdj4KICAgICAgICA8ZGl2IGNsYXNzPSJtZXRyaWMtdmFsdWUiPnt7IG1ldHJpY3Mub3Blbl9yYXRlIH19JTwvZGl2PgogICAgICAgIDxwIGNsYXNzPSJub3RlIj57eyBtZXRyaWNzLnRyYWNraW5nX25vdGUgfX08L3A+CiAgICAgIDwvYnV0dG9uPgogICAgPC9kaXY+CgogICAgPGRpdiBpZD0idHJhY2tpbmdBbmFseXRpY3NNb2RhbCIgY2xhc3M9InBvc3QtbW9kYWwiIGFyaWEtaGlkZGVuPSJ0cnVlIj4KICAgICAgPGRpdiBjbGFzcz0icG9zdC1tb2RhbC1iYWNrZHJvcCI+PC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9InBvc3QtbW9kYWwtY2FyZCB0cmFja2luZy1tb2RhbC1jYXJkIiByb2xlPSJkaWFsb2ciIGFyaWEtbW9kYWw9InRydWUiIGFyaWEtbGFiZWxsZWRieT0idHJhY2tpbmdBbmFseXRpY3NUaXRsZSI+CiAgICAgICAgPGRpdiBjbGFzcz0icG9zdC1tb2RhbC1oZWFkIj4KICAgICAgICAgIDxkaXY+CiAgICAgICAgICAgIDxoMyBpZD0idHJhY2tpbmdBbmFseXRpY3NUaXRsZSI+RW1haWwgVHJhY2tpbmcgQW5hbHl0aWNzPC9oMz4KICAgICAgICAgICAgPHAgY2xhc3M9Im5vdGUiPk9wZW4tcmF0ZSBkZXRhaWwgYWNyb3NzIHRyYWNrZWQgZW1haWxzLjwvcD4KICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPGJ1dHRvbiB0eXBlPSJidXR0b24iIGNsYXNzPSJwb3N0LW1vZGFsLWNsb3NlIiBkYXRhLWNsb3NlLXRyYWNraW5nLW1vZGFsPkNsb3NlPC9idXR0b24+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9InRyYWNraW5nLXN0YXRzLWdyaWQiPgogICAgICAgICAgPGRpdiBjbGFzcz0ic3RhdCI+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LWxhYmVsIj5PcGVuIHJhdGU8L3NwYW4+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LXZhbHVlIj57eyBtZXRyaWNzLm9wZW5fcmF0ZSB9fSU8L3NwYW4+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9InN0YXQiPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC1sYWJlbCI+VHJhY2tlZCBlbWFpbHM8L3NwYW4+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LXZhbHVlIj57eyBtZXRyaWNzLnRyYWNrZWRfZW1haWxzIH19PC9zcGFuPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJzdGF0Ij4KICAgICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPk9wZW5lZCBlbWFpbHM8L3NwYW4+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LXZhbHVlIj57eyBtZXRyaWNzLm9wZW5lZF9lbWFpbHMgfX08L3NwYW4+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9InN0YXQiPgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC1sYWJlbCI+VG90YWwgb3BlbiBldmVudHM8L3NwYW4+CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LXZhbHVlIj57eyBtZXRyaWNzLnRvdGFsX29wZW5fZXZlbnRzIH19PC9zcGFuPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9InRyYWNraW5nLWhpZ2hsaWdodCI+CiAgICAgICAgICA8ZGl2PgogICAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC1sYWJlbCI+VG9wIHRyYWNrZWQgZW1haWw8L3NwYW4+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImtwaSI+e3sgbWV0cmljcy50b3Bfb3Blbl9zdWJqZWN0IG9yICJObyBvcGVucyB5ZXQiIH19PC9kaXY+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxzcGFuIGNsYXNzPSJwaWxsIj57eyBtZXRyaWNzLnRvcF9vcGVuX2NvdW50IH19IG9wZW5zPC9zcGFuPgogICAgICAgIDwvZGl2PgoKICAgICAgICA8ZGl2IGNsYXNzPSJ0cmFja2luZy10YWJsZS13cmFwIj4KICAgICAgICAgIDx0YWJsZSBjbGFzcz0idGFibGUiPgogICAgICAgICAgICA8dGhlYWQ+CiAgICAgICAgICAgICAgPHRyPgogICAgICAgICAgICAgICAgPHRoPlNlbnQgYXQ8L3RoPgogICAgICAgICAgICAgICAgPHRoPkVtYWlsPC90aD4KICAgICAgICAgICAgICAgIDx0aD5TdWJqZWN0PC90aD4KICAgICAgICAgICAgICAgIDx0aD5PcGVuczwvdGg+CiAgICAgICAgICAgICAgICA8dGg+U3RhdHVzPC90aD4KICAgICAgICAgICAgICA8L3RyPgogICAgICAgICAgICA8L3RoZWFkPgogICAgICAgICAgICA8dGJvZHk+CiAgICAgICAgICAgICAgeyUgaWYgbWV0cmljcy50cmFja2luZ19pdGVtcyAlfQogICAgICAgICAgICAgICAgeyUgZm9yIGl0ZW0gaW4gbWV0cmljcy50cmFja2luZ19pdGVtcyAlfQogICAgICAgICAgICAgICAgICA8dHI+CiAgICAgICAgICAgICAgICAgICAgPHRkPnt7IGl0ZW0udGltZXN0YW1wIH19PC90ZD4KICAgICAgICAgICAgICAgICAgICA8dGQ+e3sgaXRlbS5lbWFpbCB9fTwvdGQ+CiAgICAgICAgICAgICAgICAgICAgPHRkPnt7IGl0ZW0uc3ViamVjdCB9fTwvdGQ+CiAgICAgICAgICAgICAgICAgICAgPHRkPnt7IGl0ZW0ub3BlbnMgfX08L3RkPgogICAgICAgICAgICAgICAgICAgIDx0ZD57eyBpdGVtLnN0YXR1cyB9fTwvdGQ+CiAgICAgICAgICAgICAgICAgIDwvdHI+CiAgICAgICAgICAgICAgICB7JSBlbmRmb3IgJX0KICAgICAgICAgICAgICB7JSBlbHNlICV9CiAgICAgICAgICAgICAgICA8dHI+CiAgICAgICAgICAgICAgICAgIDx0ZCBjb2xzcGFuPSI1IiBjbGFzcz0ibm90ZSI+Tm8gdHJhY2tlZCBlbWFpbHMgeWV0LjwvdGQ+CiAgICAgICAgICAgICAgICA8L3RyPgogICAgICAgICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgICAgIDwvdGJvZHk+CiAgICAgICAgICA8L3RhYmxlPgogICAgICAgIDwvZGl2PgogICAgICA8L2Rpdj4KICAgIDwvZGl2PgoKICAgIDxkaXYgY2xhc3M9ImNhcmQiIHN0eWxlPSJtYXJnaW4tdG9wOjE4cHg7Ij4KICAgICAgPGRpdiBjbGFzcz0iY2FyZC1oZWFkIj4KICAgICAgICA8aDM+RW1haWwgQXV0b21hdGlvbjwvaDM+CiAgICAgICAgPHNwYW4gY2xhc3M9InBpbGwiPk91dHJlYWNoPC9zcGFuPgogICAgICA8L2Rpdj4KICAgICAgPHAgY2xhc3M9Im5vdGUiPkxhdW5jaCBwZXJzb25hbGl6ZWQgb3V0cmVhY2ggZnJvbSB5b3VyIGxhdGVzdCBzY2FuIHdpdGggdGVtcGxhdGVzLCB0aHJvdHRsaW5nLCBhbmQgZGVkdXBlZCBsZWFkcy48L3A+CiAgICAgIDxkaXYgY2xhc3M9ImFjdGlvbnMiPgogICAgICAgIDxhIGNsYXNzPSJsaW5rLWJ0biIgaHJlZj0iL2VtYWlsIj5MYXVuY2ggYXV0b21hdGlvbjwvYT4KICAgICAgICA8YSBjbGFzcz0iYnRuIGJ0bi1naG9zdCIgaHJlZj0iL3NjYW4iPlJ1biBuZXcgc2NhbjwvYT4KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KCiAgICA8ZGl2IGNsYXNzPSJjYXJkIiBzdHlsZT0ibWFyZ2luLXRvcDoxOHB4OyI+CiAgICAgIDxkaXYgY2xhc3M9ImNhcmQtaGVhZCI+CiAgICAgICAgPGgzPkF1dG8gSm9iIEFwcGx5PC9oMz4KICAgICAgICA8c3BhbiBjbGFzcz0icGlsbCI+QmV0YTwvc3Bhbj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9InN0YXRzLWdyaWQiPgogICAgICAgIDxkaXYgY2xhc3M9InN0YXQiPgogICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPlByb2ZpbGUgY29tcGxldGlvbjwvc3Bhbj4KICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LXZhbHVlIj57eyBtZXRyaWNzLmF1dG9fYXBwbHlfcHJvZmlsZV9jb21wbGV0aW9uIH19JTwvc3Bhbj4KICAgICAgICA8L2Rpdj4KICAgICAgICA8ZGl2IGNsYXNzPSJzdGF0Ij4KICAgICAgICAgIDxzcGFuIGNsYXNzPSJzdGF0LWxhYmVsIj5SZWFkeSBwbGF0Zm9ybXM8L3NwYW4+CiAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC12YWx1ZSI+e3sgbWV0cmljcy5hdXRvX2FwcGx5X3JlYWR5X3BsYXRmb3JtcyB9fSAvIHt7IG1ldHJpY3MuYXV0b19hcHBseV9hY3RpdmVfcGxhdGZvcm1zIH19PC9zcGFuPgogICAgICAgIDwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9InN0YXQiPgogICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPlNhdmVkIHRyaWdnZXJzPC9zcGFuPgogICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtdmFsdWUiPnt7IG1ldHJpY3MuYXV0b19hcHBseV9zYXZlZF9ydW5zIH19PC9zcGFuPgogICAgICAgIDwvZGl2PgogICAgICA8L2Rpdj4KICAgICAgPHAgY2xhc3M9Im5vdGUiPkxhc3QgdHJpZ2dlcjoge3sgbWV0cmljcy5hdXRvX2FwcGx5X2xhc3RfcnVuX3N0YXR1cyB9fXslIGlmIG1ldHJpY3MuYXV0b19hcHBseV9sYXN0X3J1bl90aW1lc3RhbXAgJX0g4oCiIHt7IG1ldHJpY3MuYXV0b19hcHBseV9sYXN0X3J1bl90aW1lc3RhbXAgfX17JSBlbmRpZiAlfTwvcD4KICAgICAgPGRpdiBjbGFzcz0iYWN0aW9ucyI+CiAgICAgICAgPGEgY2xhc3M9ImxpbmstYnRuIiBocmVmPSIvYXV0by1hcHBseSI+T3BlbiBhdXRvLWFwcGx5PC9hPgogICAgICA8L2Rpdj4KICAgIDwvZGl2PgoKICAgIDxkaXYgY2xhc3M9ImNhcmQiIHN0eWxlPSJtYXJnaW4tdG9wOjE4cHg7Ij4KICAgICAgPGgzPlJlc3VtZSBTY29yZTwvaDM+CiAgICAgIDxkaXYgY2xhc3M9ImNoYXJ0Ij48ZGl2IGNsYXNzPSJjaGFydC1iYXIiIHN0eWxlPSJ3aWR0aDoge3sgbWV0cmljcy5yZXN1bWVfc2NvcmUgfX0lOyI+PC9kaXY+PC9kaXY+CiAgICAgIDxwIGNsYXNzPSJub3RlIj5TY29yZToge3sgbWV0cmljcy5yZXN1bWVfc2NvcmUgfX0vMTAwPC9wPgogICAgICA8cCBjbGFzcz0ibm90ZSI+UHJvYmxlbXMgdG8gZml4OiB7eyBtZXRyaWNzLnJlc3VtZV9pc3N1ZXNfY291bnQgfX08L3A+CiAgICA8L2Rpdj4KCiAgICA8ZGl2IGNsYXNzPSJjYXJkIj4KICAgICAgPGgzPkxpbmtlZEluIFByb2ZpbGUgU2NvcmU8L2gzPgogICAgICA8ZGl2IGNsYXNzPSJjaGFydCI+PGRpdiBjbGFzcz0iY2hhcnQtYmFyIiBzdHlsZT0id2lkdGg6IHt7IG1ldHJpY3MubGlua2VkaW5fc2NvcmUgfX0lOyI+PC9kaXY+PC9kaXY+CiAgICAgIDxwIGNsYXNzPSJub3RlIj5TY29yZToge3sgbWV0cmljcy5saW5rZWRpbl9zY29yZSB9fS8xMDA8L3A+CiAgICAgIDxwIGNsYXNzPSJub3RlIj5Qcm9ibGVtcyB0byBmaXg6IHt7IG1ldHJpY3MubGlua2VkaW5faXNzdWVzX2NvdW50IH19PC9wPgogICAgPC9kaXY+CiAgPC9kaXY+CnslIGVuZGJsb2NrICV9Cgp7JSBibG9jayBzY3JpcHRzICV9CiAgPHNjcmlwdD4KICAgICgoKSA9PiB7CiAgICAgIGNvbnN0IG9wZW5CdXR0b24gPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgib3BlblJhdGVBbmFseXRpY3NCdXR0b24iKTsKICAgICAgY29uc3QgbW9kYWwgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgidHJhY2tpbmdBbmFseXRpY3NNb2RhbCIpOwogICAgICBpZiAoIW9wZW5CdXR0b24gfHwgIW1vZGFsKSByZXR1cm47CgogICAgICBjb25zdCBjbG9zZUJ1dHRvbnMgPSBtb2RhbC5xdWVyeVNlbGVjdG9yQWxsKCJbZGF0YS1jbG9zZS10cmFja2luZy1tb2RhbF0iKTsKICAgICAgY29uc3QgYmFja2Ryb3AgPSBtb2RhbC5xdWVyeVNlbGVjdG9yKCIucG9zdC1tb2RhbC1iYWNrZHJvcCIpOwoKICAgICAgZnVuY3Rpb24gb3Blbk1vZGFsKCkgewogICAgICAgIG1vZGFsLmNsYXNzTGlzdC5hZGQoIm9wZW4iKTsKICAgICAgICBtb2RhbC5zZXRBdHRyaWJ1dGUoImFyaWEtaGlkZGVuIiwgImZhbHNlIik7CiAgICAgIH0KCiAgICAgIGZ1bmN0aW9uIGNsb3NlTW9kYWwoKSB7CiAgICAgICAgbW9kYWwuY2xhc3NMaXN0LnJlbW92ZSgib3BlbiIpOwogICAgICAgIG1vZGFsLnNldEF0dHJpYnV0ZSgiYXJpYS1oaWRkZW4iLCAidHJ1ZSIpOwogICAgICB9CgogICAgICBvcGVuQnV0dG9uLmFkZEV2ZW50TGlzdGVuZXIoImNsaWNrIiwgb3Blbk1vZGFsKTsKICAgICAgY2xvc2VCdXR0b25zLmZvckVhY2goKGJ1dHRvbikgPT4gYnV0dG9uLmFkZEV2ZW50TGlzdGVuZXIoImNsaWNrIiwgY2xvc2VNb2RhbCkpOwogICAgICBpZiAoYmFja2Ryb3ApIGJhY2tkcm9wLmFkZEV2ZW50TGlzdGVuZXIoImNsaWNrIiwgY2xvc2VNb2RhbCk7CiAgICAgIGRvY3VtZW50LmFkZEV2ZW50TGlzdGVuZXIoImtleWRvd24iLCAoZXZlbnQpID0+IHsKICAgICAgICBpZiAoZXZlbnQua2V5ID09PSAiRXNjYXBlIiAmJiBtb2RhbC5jbGFzc0xpc3QuY29udGFpbnMoIm9wZW4iKSkgewogICAgICAgICAgY2xvc2VNb2RhbCgpOwogICAgICAgIH0KICAgICAgfSk7CiAgICB9KSgpOwogIDwvc2NyaXB0Pgp7JSBlbmRibG9jayAlfQo=","index.html":"eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBjb250ZW50ICV9CiAgPGRpdiBjbGFzcz0icGFnZSI+CiAgICA8aGVhZGVyIGNsYXNzPSJoZWFkZXIiPgogICAgICA8ZGl2IGNsYXNzPSJpY29uLWJhZGdlIj4KICAgICAgICA8c3ZnIHdpZHRoPSIyNiIgaGVpZ2h0PSIyNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgIDxwYXRoIGQ9Ik00IDVoMTZ2MTBIN2wtMyAzVjV6IiBzdHJva2U9IndoaXRlIiBzdHJva2Utd2lkdGg9IjEuNiIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPgogICAgICAgICAgPHBhdGggZD0iTTggOWg4TTggMTJoNiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgogICAgICAgIDwvc3ZnPgogICAgICA8L2Rpdj4KICAgICAgPGRpdj4KICAgICAgICA8aDE+TGlua2VkSW4gU2NyYXBlcjwvaDE+CiAgICAgICAgPHAgY2xhc3M9InN1YnRpdGxlIj5SdW4gZm9jdXNlZCBzY2FucyBhbmQgdW5sb2NrIGF1dG9tYXRpb24gd29ya2Zsb3dzLjwvcD4KICAgICAgPC9kaXY+CiAgICA8L2hlYWRlcj4KCiAgICA8ZGl2IGNsYXNzPSJjYXJkIj4KICAgICAgPGZvcm0gbWV0aG9kPSJwb3N0IiBhY3Rpb249Ii9zdGFydCIgY2xhc3M9InN0YWdnZXIiPgogICAgICAgIDxkaXYgY2xhc3M9ImZpZWxkIj4KICAgICAgICAgIDxsYWJlbCBmb3I9InF1ZXJ5Ij5TZWFyY2ggcXVlcnk8L2xhYmVsPgogICAgICAgICAgPGlucHV0IGlkPSJxdWVyeSIgbmFtZT0icXVlcnkiIHR5cGU9InRleHQiIHBsYWNlaG9sZGVyPSJoaXJpbmcgZGVsb2l0dGUiIHJlcXVpcmVkIC8+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImZpZWxkIj4KICAgICAgICAgIDxsYWJlbCBmb3I9ImNvbXBhbmllcyI+Q29tcGFuaWVzIChjb21tYSBzZXBhcmF0ZWQpPC9sYWJlbD4KICAgICAgICAgIDxpbnB1dCBpZD0iY29tcGFuaWVzIiBuYW1lPSJjb21wYW5pZXMiIHR5cGU9InRleHQiIHBsYWNlaG9sZGVyPSJkZWxvaXR0ZSwgbmlrZSwgdGNzIiAvPgogICAgICAgIDwvZGl2PgoKICAgICAgICA8ZGl2IGNsYXNzPSJncmlkIHR3byI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJmaWVsZCI+CiAgICAgICAgICAgIDxsYWJlbCBmb3I9Im1pbl9wb3N0cyI+UG9zdHMgdG8gc2NhbiAocGVyIGNvbXBhbnkpPC9sYWJlbD4KICAgICAgICAgICAgPGlucHV0IGlkPSJtaW5fcG9zdHMiIG5hbWU9Im1pbl9wb3N0cyIgdHlwZT0ibnVtYmVyIiBtaW49IjIwIiBzdGVwPSIxMCIgdmFsdWU9IjEwMCIgcmVxdWlyZWQgLz4KICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPGRpdiBjbGFzcz0iZmllbGQiPgogICAgICAgICAgICA8bGFiZWwgZm9yPSJtYXhfc2Nyb2xscyI+TWF4IHNjcm9sbHMgKG9wdGlvbmFsKTwvbGFiZWw+CiAgICAgICAgICAgIDxpbnB1dCBpZD0ibWF4X3Njcm9sbHMiIG5hbWU9Im1heF9zY3JvbGxzIiB0eXBlPSJudW1iZXIiIG1pbj0iMSIgc3RlcD0iMSIgcGxhY2Vob2xkZXI9IjQwIiAvPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImFjdGlvbnMiPgogICAgICAgICAgPGJ1dHRvbiBjbGFzcz0iYnRuIiB0eXBlPSJzdWJtaXQiPlJ1biBTY2FuPC9idXR0b24+CiAgICAgICAgPC9kaXY+CiAgICAgIDwvZm9ybT4KCiAgICAgIHslIGlmIGVycm9yICV9CiAgICAgICAgPGRpdiBjbGFzcz0ic3RhdHVzIGVycm9yIj57eyBlcnJvciB9fTwvZGl2PgogICAgICB7JSBlbmRpZiAlfQogICAgPC9kaXY+CgogICAgPGRpdiBjbGFzcz0iY2FyZCIgc3R5bGU9Im1hcmdpbi10b3A6MThweDsiPgogICAgICA8ZGl2IGNsYXNzPSJjYXJkLWhlYWQiPgogICAgICAgIDxoMz5QYXN0IHNjYW5zPC9oMz4KICAgICAgICA8c3BhbiBjbGFzcz0icGlsbCI+e3sgc2Nhbl9oaXN0b3J5fGxlbmd0aCB9fSBzYXZlZDwvc3Bhbj4KICAgICAgPC9kaXY+CgogICAgICB7JSBpZiBzY2FuX2hpc3RvcnkgJX0KICAgICAgICA8ZGl2IGNsYXNzPSJzY2FuLWhpc3RvcnkiPgogICAgICAgICAgeyUgZm9yIHNjYW4gaW4gc2Nhbl9oaXN0b3J5ICV9CiAgICAgICAgICAgIDxkaXYgY2xhc3M9InNjYW4taGlzdG9yeS1pdGVtIj4KICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJzY2FuLWhpc3RvcnktbWFpbiI+CiAgICAgICAgICAgICAgICA8ZGl2PgogICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJzY2FuLWhpc3RvcnktdGl0bGUiPnt7IHNjYW4ubGFiZWwgfX08L2Rpdj4KICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ic2Nhbi1oaXN0b3J5LWNvbXBhbmllcyI+e3sgc2Nhbi5jb21wYW55X3RleHQgfX08L2Rpdj4KICAgICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ic2Nhbi1oaXN0b3J5LW1ldGEiPgogICAgICAgICAgICAgICAgICA8c3Bhbj57eyBzY2FuLnRpbWVzdGFtcCB9fTwvc3Bhbj4KICAgICAgICAgICAgICAgICAgPHNwYW4+e3sgc2Nhbi5jb21wYW55X2NvdW50IH19IGNvbXBhbnt7ICJ5IiBpZiBzY2FuLmNvbXBhbnlfY291bnQgPT0gMSBlbHNlICJpZXMiIH19PC9zcGFuPgogICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICA8YnV0dG9uCiAgICAgICAgICAgICAgICAgIHR5cGU9ImJ1dHRvbiIKICAgICAgICAgICAgICAgICAgY2xhc3M9InNjYW4tb3Blbi1idG4iCiAgICAgICAgICAgICAgICAgIGRhdGEtb3Blbi1zY2FuCiAgICAgICAgICAgICAgICAgIGRhdGEtc2Nhbi10aXRsZT0ie3sgc2Nhbi5sYWJlbHxlIH19IgogICAgICAgICAgICAgICAgICBkYXRhLXNjYW4tdGltZT0ie3sgc2Nhbi50aW1lc3RhbXB8ZSB9fSIKICAgICAgICAgICAgICAgICAgZGF0YS1zY2FuLWNvbXBhbmllcz0ie3sgc2Nhbi5jb21wYW55X3RleHR8ZSB9fSIKICAgICAgICAgICAgICAgICAgZGF0YS1zY2FuLWZpbGVzPSd7eyBzY2FuLmZpbGVzfHRvanNvbnxmb3JjZWVzY2FwZSB9fScKICAgICAgICAgICAgICAgICAgYXJpYS1sYWJlbD0iT3BlbiBwYXN0IHNjYW4gZmlsZXMiCiAgICAgICAgICAgICAgICA+CiAgICAgICAgICAgICAgICAgIDxzdmcgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBhcmlhLWhpZGRlbj0idHJ1ZSI+CiAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTIuNSAxMnMzLjUtNS41IDkuNS01LjVTMjEuNSAxMiAyMS41IDEycy0zLjUgNS41LTkuNSA1LjVTMi41IDEyIDIuNSAxMloiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNyIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPgogICAgICAgICAgICAgICAgICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjIuNiIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS43Ii8+CiAgICAgICAgICAgICAgICAgIDwvc3ZnPgogICAgICAgICAgICAgICAgPC9idXR0b24+CiAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgPC9kaXY+CiAgICAgIHslIGVsc2UgJX0KICAgICAgICA8cCBjbGFzcz0ibm90ZSI+Tm8gcGFzdCBzY2FucyB5ZXQuIFJ1biB5b3VyIGZpcnN0IHNjcmFwZSB0byBidWlsZCBkb3dubG9hZGFibGUgaGlzdG9yeS48L3A+CiAgICAgIHslIGVuZGlmICV9CiAgICA8L2Rpdj4KICA8L2Rpdj4KCiAgPGRpdiBpZD0ic2Nhbkhpc3RvcnlNb2RhbCIgY2xhc3M9InBvc3QtbW9kYWwiIGFyaWEtaGlkZGVuPSJ0cnVlIj4KICAgIDxkaXYgY2xhc3M9InBvc3QtbW9kYWwtYmFja2Ryb3AiPjwvZGl2PgogICAgPGRpdiBjbGFzcz0icG9zdC1tb2RhbC1jYXJkIiByb2xlPSJkaWFsb2ciIGFyaWEtbW9kYWw9InRydWUiIGFyaWEtbGFiZWxsZWRieT0ic2Nhbkhpc3RvcnlUaXRsZSI+CiAgICAgIDxkaXYgY2xhc3M9InBvc3QtbW9kYWwtaGVhZCI+CiAgICAgICAgPGRpdj4KICAgICAgICAgIDxoMyBpZD0ic2Nhbkhpc3RvcnlUaXRsZSI+UGFzdCBzY2FuIGZpbGVzPC9oMz4KICAgICAgICAgIDxwIGlkPSJzY2FuSGlzdG9yeU1ldGEiIGNsYXNzPSJub3RlIj48L3A+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGJ1dHRvbiB0eXBlPSJidXR0b24iIGNsYXNzPSJwb3N0LW1vZGFsLWNsb3NlIiBkYXRhLWNsb3NlLXNjYW4tbW9kYWw+Q2xvc2U8L2J1dHRvbj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgaWQ9InNjYW5IaXN0b3J5Qm9keSIgY2xhc3M9InNjYW4tbW9kYWwtYm9keSI+PC9kaXY+CiAgICA8L2Rpdj4KICA8L2Rpdj4KeyUgZW5kYmxvY2sgJX0KCnslIGJsb2NrIHNjcmlwdHMgJX0KICA8c2NyaXB0PgogICAgKCgpID0+IHsKICAgICAgY29uc3QgbW9kYWwgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgic2Nhbkhpc3RvcnlNb2RhbCIpOwogICAgICBjb25zdCBtb2RhbEJvZHkgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgic2Nhbkhpc3RvcnlCb2R5Iik7CiAgICAgIGNvbnN0IG1vZGFsVGl0bGUgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgic2Nhbkhpc3RvcnlUaXRsZSIpOwogICAgICBjb25zdCBtb2RhbE1ldGEgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgic2Nhbkhpc3RvcnlNZXRhIik7CiAgICAgIGlmICghbW9kYWwgfHwgIW1vZGFsQm9keSB8fCAhbW9kYWxUaXRsZSB8fCAhbW9kYWxNZXRhKSByZXR1cm47CgogICAgICBmdW5jdGlvbiBlc2NhcGVIdG1sKHZhbHVlKSB7CiAgICAgICAgcmV0dXJuIFN0cmluZyh2YWx1ZSB8fCAiIikKICAgICAgICAgIC5yZXBsYWNlKC8mL2csICImYW1wOyIpCiAgICAgICAgICAucmVwbGFjZSgvPC9nLCAiJmx0OyIpCiAgICAgICAgICAucmVwbGFjZSgvPi9nLCAiJmd0OyIpCiAgICAgICAgICAucmVwbGFjZSgvXCIvZywgIiZxdW90OyIpCiAgICAgICAgICAucmVwbGFjZSgvJy9nLCAiJiMzOTsiKTsKICAgICAgfQoKICAgICAgZnVuY3Rpb24gY2xvc2VNb2RhbCgpIHsKICAgICAgICBtb2RhbC5jbGFzc0xpc3QucmVtb3ZlKCJvcGVuIik7CiAgICAgICAgbW9kYWwuc2V0QXR0cmlidXRlKCJhcmlhLWhpZGRlbiIsICJ0cnVlIik7CiAgICAgIH0KCiAgICAgIGZ1bmN0aW9uIG9wZW5Nb2RhbChidXR0b24pIHsKICAgICAgICBjb25zdCB0aXRsZSA9IGJ1dHRvbi5nZXRBdHRyaWJ1dGUoImRhdGEtc2Nhbi10aXRsZSIpIHx8ICJQYXN0IHNjYW4iOwogICAgICAgIGNvbnN0IHRpbWVzdGFtcCA9IGJ1dHRvbi5nZXRBdHRyaWJ1dGUoImRhdGEtc2Nhbi10aW1lIikgfHwgIiI7CiAgICAgICAgY29uc3QgY29tcGFuaWVzID0gYnV0dG9uLmdldEF0dHJpYnV0ZSgiZGF0YS1zY2FuLWNvbXBhbmllcyIpIHx8ICIiOwogICAgICAgIGxldCBmaWxlcyA9IFtdOwogICAgICAgIHRyeSB7CiAgICAgICAgICBmaWxlcyA9IEpTT04ucGFyc2UoYnV0dG9uLmdldEF0dHJpYnV0ZSgiZGF0YS1zY2FuLWZpbGVzIikgfHwgIltdIik7CiAgICAgICAgfSBjYXRjaCAoZXJyb3IpIHsKICAgICAgICAgIGZpbGVzID0gW107CiAgICAgICAgfQoKICAgICAgICBtb2RhbFRpdGxlLnRleHRDb250ZW50ID0gdGl0bGU7CiAgICAgICAgbW9kYWxNZXRhLnRleHRDb250ZW50ID0gW3RpbWVzdGFtcCwgY29tcGFuaWVzXS5maWx0ZXIoQm9vbGVhbikuam9pbigiIHwgIik7CgogICAgICAgIGlmICghZmlsZXMubGVuZ3RoKSB7CiAgICAgICAgICBtb2RhbEJvZHkuaW5uZXJIVE1MID0gYDxwIGNsYXNzPSJub3RlIj5ObyBmaWxlcyBzYXZlZCBmb3IgdGhpcyBzY2FuLjwvcD5gOwogICAgICAgIH0gZWxzZSB7CiAgICAgICAgICBtb2RhbEJvZHkuaW5uZXJIVE1MID0gZmlsZXMubWFwKChmaWxlKSA9PiBgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9InNjYW4tZmlsZS1yb3ciPgogICAgICAgICAgICAgIDxkaXYgY2xhc3M9InNjYW4tZmlsZS1tZXRhIj4KICAgICAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJzY2FuLWZpbGUtbmFtZSI+JHtlc2NhcGVIdG1sKGZpbGUubGFiZWwpfTwvc3Bhbj4KICAgICAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJzY2FuLWZpbGUtc2l6ZSI+JHtlc2NhcGVIdG1sKGZpbGUuc2l6ZV9rYil9IEtCPC9zcGFuPgogICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICAgIDxkaXYgY2xhc3M9InNjYW4tZmlsZS1hY3Rpb25zIj4KICAgICAgICAgICAgICAgIDxhIGNsYXNzPSJzY2FuLWZpbGUtbGluayIgaHJlZj0iL2Rvd25sb2FkLyR7ZW5jb2RlVVJJQ29tcG9uZW50KGZpbGUubmFtZSkucmVwbGFjZSgvJTJGL2csICIvIil9Ij5Eb3dubG9hZDwvYT4KICAgICAgICAgICAgICAgIDxhIGNsYXNzPSJzY2FuLWZpbGUtbWFpbCIgaHJlZj0iL3NjYW4tZmlsZS1lbWFpbC8ke2VuY29kZVVSSUNvbXBvbmVudChmaWxlLm5hbWUpLnJlcGxhY2UoLyUyRi9nLCAiLyIpfSI+U2VuZCBvdmVyIG1haWw8L2E+CiAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgYCkuam9pbigiIik7CiAgICAgICAgfQoKICAgICAgICBtb2RhbC5jbGFzc0xpc3QuYWRkKCJvcGVuIik7CiAgICAgICAgbW9kYWwuc2V0QXR0cmlidXRlKCJhcmlhLWhpZGRlbiIsICJmYWxzZSIpOwogICAgICB9CgogICAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCJbZGF0YS1vcGVuLXNjYW5dIikuZm9yRWFjaCgoYnV0dG9uKSA9PiB7CiAgICAgICAgYnV0dG9uLmFkZEV2ZW50TGlzdGVuZXIoImNsaWNrIiwgKCkgPT4gb3Blbk1vZGFsKGJ1dHRvbikpOwogICAgICB9KTsKICAgICAgbW9kYWwucXVlcnlTZWxlY3RvckFsbCgiW2RhdGEtY2xvc2Utc2Nhbi1tb2RhbF0iKS5mb3JFYWNoKChidXR0b24pID0+IHsKICAgICAgICBidXR0b24uYWRkRXZlbnRMaXN0ZW5lcigiY2xpY2siLCBjbG9zZU1vZGFsKTsKICAgICAgfSk7CiAgICAgIGNvbnN0IGJhY2tkcm9wID0gbW9kYWwucXVlcnlTZWxlY3RvcigiLnBvc3QtbW9kYWwtYmFja2Ryb3AiKTsKICAgICAgaWYgKGJhY2tkcm9wKSBiYWNrZHJvcC5hZGRFdmVudExpc3RlbmVyKCJjbGljayIsIGNsb3NlTW9kYWwpOwogICAgICBkb2N1bWVudC5hZGRFdmVudExpc3RlbmVyKCJrZXlkb3duIiwgKGV2ZW50KSA9PiB7CiAgICAgICAgaWYgKGV2ZW50LmtleSA9PT0gIkVzY2FwZSIgJiYgbW9kYWwuY2xhc3NMaXN0LmNvbnRhaW5zKCJvcGVuIikpIHsKICAgICAgICAgIGNsb3NlTW9kYWwoKTsKICAgICAgICB9CiAgICAgIH0pOwogICAgfSkoKTsKICA8L3NjcmlwdD4KeyUgZW5kYmxvY2sgJX0K","job.html":"eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBjb250ZW50ICV9CiAgPGRpdiBjbGFzcz0icGFnZSI+CiAgICA8aGVhZGVyIGNsYXNzPSJoZWFkZXIiPgogICAgICA8ZGl2IGNsYXNzPSJpY29uLWJhZGdlIj4KICAgICAgICA8c3ZnIHdpZHRoPSIyNiIgaGVpZ2h0PSIyNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgIDxwYXRoIGQ9Ik00IDEyaDE2TTEyIDR2MTYiIHN0cm9rZT0id2hpdGUiIHN0cm9rZS13aWR0aD0iMS42IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz4KICAgICAgICA8L3N2Zz4KICAgICAgPC9kaXY+CiAgICAgIDxkaXY+CiAgICAgICAgPGgxPlNjYW4gUHJvZ3Jlc3M8L2gxPgogICAgICAgIDxwIGNsYXNzPSJzdWJ0aXRsZSI+T25seSB0aGUgdXNlZnVsIHNjYW4gc3RhdHVzIHN0YXlzIGhlcmUuIFNvdXJjZSBpbnRlcm5hbHMgc3RheSBpbiB0aGUgYmFja2VuZC48L3A+CiAgICAgIDwvZGl2PgogICAgPC9oZWFkZXI+CgogICAgPGRpdiBjbGFzcz0iY2FyZCI+CiAgICAgIDxkaXYgY2xhc3M9ImFjdGlvbnMiIHN0eWxlPSJtYXJnaW4tYm90dG9tOiAxMnB4OyI+CiAgICAgICAgPGEgY2xhc3M9ImJ0biBidG4tZ2hvc3QiIGhyZWY9Int7IGJhY2tfaHJlZiBvciAnL3NjYW4nIH19Ij57eyBiYWNrX2xhYmVsIG9yICdCYWNrIHRvIFNjYW5uZXInIH19PC9hPgogICAgICA8L2Rpdj4KICAgICAgPGRpdiBpZD0ic3RhdHVzIiBjbGFzcz0ic3RhdHVzIj5TdGFydGluZy4uLjwvZGl2PgogICAgICA8ZGl2IGlkPSJkZXRhaWwiIGNsYXNzPSJub3RlIj5UaGlzIHBhZ2UgdXBkYXRlcyBhdXRvbWF0aWNhbGx5LjwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJzdGF0cy1ncmlkIiBzdHlsZT0ibWFyZ2luLXRvcDogMThweDsiPgogICAgICAgIDxkaXYgY2xhc3M9InN0YXQiPgogICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPkZvdW5kPC9zcGFuPgogICAgICAgICAgPHNwYW4gaWQ9ImZvdW5kQ291bnQiIGNsYXNzPSJzdGF0LXZhbHVlIj4wPC9zcGFuPgogICAgICAgIDwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9InN0YXQiPgogICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPlByZWZlcnJlZDwvc3Bhbj4KICAgICAgICAgIDxzcGFuIGlkPSJwcmVmZXJyZWRDb3VudCIgY2xhc3M9InN0YXQtdmFsdWUiPjA8L3NwYW4+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0ic3RhdCI+CiAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC1sYWJlbCI+UHJvZ3Jlc3M8L3NwYW4+CiAgICAgICAgICA8c3BhbiBpZD0icHJvZ3Jlc3NDb3VudCIgY2xhc3M9InN0YXQtdmFsdWUgYXV0by1zdGF0LWNvbXBhY3QiPjAgLyAwPC9zcGFuPgogICAgICAgIDwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9InN0YXQiPgogICAgICAgICAgPHNwYW4gY2xhc3M9InN0YXQtbGFiZWwiPk1vZGU8L3NwYW4+CiAgICAgICAgICA8c3BhbiBpZD0ic3RyYXRlZ3lMYWJlbCIgY2xhc3M9InN0YXQtdmFsdWUgYXV0by1zdGF0LWNvbXBhY3QiPi08L3NwYW4+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0ic3RhdCI+CiAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC1sYWJlbCI+UmVzb2x2ZWQ8L3NwYW4+CiAgICAgICAgICA8c3BhbiBpZD0icmVzb2x2ZWRDb3VudCIgY2xhc3M9InN0YXQtdmFsdWUgYXV0by1zdGF0LWNvbXBhY3QiPjA8L3NwYW4+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0ic3RhdCI+CiAgICAgICAgICA8c3BhbiBjbGFzcz0ic3RhdC1sYWJlbCI+UmV2aWV3PC9zcGFuPgogICAgICAgICAgPHNwYW4gaWQ9InJldmlld0NvdW50IiBjbGFzcz0ic3RhdC12YWx1ZSBhdXRvLXN0YXQtY29tcGFjdCI+MDwvc3Bhbj4KICAgICAgICA8L2Rpdj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgaWQ9ImRvd25sb2FkcyIgc3R5bGU9Im1hcmdpbi10b3A6IDE4cHg7Ij48L2Rpdj4KICAgIDwvZGl2PgogIDwvZGl2PgoKICA8c2NyaXB0PgogICAgY29uc3Qgc3RhdHVzRWwgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgic3RhdHVzIik7CiAgICBjb25zdCBkZXRhaWxFbCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJkZXRhaWwiKTsKICAgIGNvbnN0IGZvdW5kQ291bnRFbCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJmb3VuZENvdW50Iik7CiAgICBjb25zdCBwcmVmZXJyZWRDb3VudEVsID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInByZWZlcnJlZENvdW50Iik7CiAgICBjb25zdCBwcm9ncmVzc0NvdW50RWwgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgicHJvZ3Jlc3NDb3VudCIpOwogICAgY29uc3Qgc3RyYXRlZ3lMYWJlbEVsID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInN0cmF0ZWd5TGFiZWwiKTsKICAgIGNvbnN0IHJlc29sdmVkQ291bnRFbCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJyZXNvbHZlZENvdW50Iik7CiAgICBjb25zdCByZXZpZXdDb3VudEVsID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInJldmlld0NvdW50Iik7CiAgICBjb25zdCBkb3dubG9hZHNFbCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJkb3dubG9hZHMiKTsKICAgIGNvbnN0IGpvYklkID0gInt7IGpvYl9pZCB9fSI7CgogICAgYXN5bmMgZnVuY3Rpb24gcG9sbCgpIHsKICAgICAgY29uc3QgcmVzID0gYXdhaXQgZmV0Y2goYC9qb2IvJHtqb2JJZH0vc3RhdHVzYCk7CiAgICAgIGNvbnN0IGRhdGEgPSBhd2FpdCByZXMuanNvbigpOwoKICAgICAgaWYgKGRhdGEuZXJyb3IpIHsKICAgICAgICBzdGF0dXNFbC50ZXh0Q29udGVudCA9ICJFcnJvciI7CiAgICAgICAgc3RhdHVzRWwuY2xhc3NOYW1lID0gInN0YXR1cyBlcnJvciI7CiAgICAgICAgZGV0YWlsRWwudGV4dENvbnRlbnQgPSBkYXRhLmVycm9yOwogICAgICAgIHJldHVybjsKICAgICAgfQoKICAgICAgc3RhdHVzRWwudGV4dENvbnRlbnQgPSBkYXRhLnN0YXR1czsKICAgICAgZm91bmRDb3VudEVsLnRleHRDb250ZW50ID0gZGF0YS5yYXdfcm93cyB8fCAwOwogICAgICBwcmVmZXJyZWRDb3VudEVsLnRleHRDb250ZW50ID0gZGF0YS5xdWFsaXR5X3Jvd3MgfHwgMDsKICAgICAgcHJvZ3Jlc3NDb3VudEVsLnRleHRDb250ZW50ID0gYCR7ZGF0YS5jb21wYW55X2luZGV4IHx8IDB9IC8gJHtkYXRhLmNvbXBhbnlfdG90YWwgfHwgMH1gOwogICAgICBzdHJhdGVneUxhYmVsRWwudGV4dENvbnRlbnQgPSBkYXRhLnNjYW5fc3RyYXRlZ3lfbGFiZWwgfHwgIlNjYW4iOwogICAgICByZXNvbHZlZENvdW50RWwudGV4dENvbnRlbnQgPSBkYXRhLnJlc29sdmVkX3VybF9jb3VudCB8fCAwOwogICAgICByZXZpZXdDb3VudEVsLnRleHRDb250ZW50ID0gZGF0YS51bnN1cHBvcnRlZF9jb3VudCB8fCAwOwogICAgICBkZXRhaWxFbC50ZXh0Q29udGVudCA9IGRhdGEuZG9uZQogICAgICAgID8gIlNjYW4gZmluaXNoZWQuIgogICAgICAgIDogKGRhdGEuY3VycmVudF9jb21wYW55ID8gYFdvcmtpbmcgb24gJHtkYXRhLmN1cnJlbnRfY29tcGFueX0uIFVwZGF0ZWQgJHtkYXRhLnVwZGF0ZWRfYXR9LmAgOiBgVXBkYXRlZCAke2RhdGEudXBkYXRlZF9hdH0uYCk7CgogICAgICBpZiAoZGF0YS5kb25lKSB7CiAgICAgICAgaWYgKGRhdGEuZXJyb3IpIHsKICAgICAgICAgIHN0YXR1c0VsLmNsYXNzTmFtZSA9ICJzdGF0dXMgZXJyb3IiOwogICAgICAgICAgZGV0YWlsRWwudGV4dENvbnRlbnQgPSBkYXRhLmVycm9yOwogICAgICAgIH0gZWxzZSBpZiAoZGF0YS5ub19yZXN1bHRzIHx8ICEoZGF0YS5yYXdfcm93cyA+IDApKSB7CiAgICAgICAgICBzdGF0dXNFbC50ZXh0Q29udGVudCA9ICJObyBqb2JzIGZvdW5kIjsKICAgICAgICAgIGRldGFpbEVsLnRleHRDb250ZW50ID0gKGRhdGEuc2Nhbl9zdHJhdGVneV9sYWJlbCB8fCAiIikudG9Mb3dlckNhc2UoKS5pbmNsdWRlcygidXJsIikKICAgICAgICAgICAgPyBgTm8gbWF0Y2hpbmcgam9icyB3ZXJlIGZvdW5kIGluIHRoZSBzYXZlZCBVUkwgYmF0Y2guIFJlc29sdmVkIHRhcmdldHM6ICR7ZGF0YS5yZXNvbHZlZF91cmxfY291bnQgfHwgMH0uIE1hbnVhbCByZXZpZXcgaXRlbXM6ICR7ZGF0YS51bnN1cHBvcnRlZF9jb3VudCB8fCAwfS5gCiAgICAgICAgICAgIDogIlRyeSBicm9hZGVyIGtleXdvcmRzIG9yIGZld2VyIGNvbXBhbnkgZmlsdGVycy4iOwogICAgICAgICAgaWYgKGRhdGEuZmlsZXMudW5zdXBwb3J0ZWRfcmVwb3J0X3hsc3ggfHwgZGF0YS5maWxlcy51bnN1cHBvcnRlZF9yZXBvcnRfY3N2KSB7CiAgICAgICAgICAgIGxldCBsaW5rc0h0bWwgPSBgPGRpdiBjbGFzcz0iYWN0aW9ucyI+YDsKICAgICAgICAgICAgaWYgKGRhdGEuZmlsZXMudW5zdXBwb3J0ZWRfcmVwb3J0X3hsc3gpIHsKICAgICAgICAgICAgICBsaW5rc0h0bWwgKz0gYDxhIGNsYXNzPSJidG4gYnRuLWdob3N0IiBocmVmPSIvZG93bmxvYWQvJHtkYXRhLmZpbGVzLnVuc3VwcG9ydGVkX3JlcG9ydF94bHN4fSI+RG93bmxvYWQgbWFudWFsIHJldmlldyBsaXN0PC9hPmA7CiAgICAgICAgICAgIH0KICAgICAgICAgICAgbGlua3NIdG1sICs9IGA8L2Rpdj5gOwogICAgICAgICAgICBkb3dubG9hZHNFbC5pbm5lckhUTUwgPSBsaW5rc0h0bWw7CiAgICAgICAgICB9CiAgICAgICAgfSBlbHNlIHsKICAgICAgICAgIHN0YXR1c0VsLmNsYXNzTmFtZSA9ICJzdGF0dXMgZG9uZSI7CiAgICAgICAgICBsZXQgbGlua3NIdG1sID0gYDxkaXYgY2xhc3M9ImFjdGlvbnMiPmA7CiAgICAgICAgICBpZiAoZGF0YS5maWxlcy5tYXN0ZXJfcXVhbGl0eV94bHN4KSB7CiAgICAgICAgICAgIGxpbmtzSHRtbCArPSBgPGEgY2xhc3M9ImJ0biIgaHJlZj0iL2Rvd25sb2FkLyR7ZGF0YS5maWxlcy5tYXN0ZXJfcXVhbGl0eV94bHN4fSI+RG93bmxvYWQgcHJlZmVycmVkIGpvYnM8L2E+YDsKICAgICAgICAgIH0KICAgICAgICAgIGlmIChkYXRhLmZpbGVzLm1hc3Rlcl9yYXdfeGxzeCkgewogICAgICAgICAgICBsaW5rc0h0bWwgKz0gYDxhIGNsYXNzPSJidG4gYnRuLWdob3N0IiBocmVmPSIvZG93bmxvYWQvJHtkYXRhLmZpbGVzLm1hc3Rlcl9yYXdfeGxzeH0iPkRvd25sb2FkIGFsbCBmb3VuZCBqb2JzPC9hPmA7CiAgICAgICAgICB9CiAgICAgICAgICBpZiAoZGF0YS5maWxlcy5mZWVkX2pzb24pIHsKICAgICAgICAgICAgbGlua3NIdG1sICs9IGA8YSBjbGFzcz0iYnRuIGJ0bi1naG9zdCIgaHJlZj0iL2Rvd25sb2FkLyR7ZGF0YS5maWxlcy5mZWVkX2pzb259Ij5Eb3dubG9hZCBjYXJlZXItc2l0ZSBmZWVkPC9hPmA7CiAgICAgICAgICB9CiAgICAgICAgICBpZiAoZGF0YS5maWxlcy5hdGxhc19qc29uKSB7CiAgICAgICAgICAgIGxpbmtzSHRtbCArPSBgPGEgY2xhc3M9ImJ0biBidG4tZ2hvc3QiIGhyZWY9Ii9kb3dubG9hZC8ke2RhdGEuZmlsZXMuYXRsYXNfanNvbn0iPkRvd25sb2FkIGF0bGFzIG1hcDwvYT5gOwogICAgICAgICAgfQogICAgICAgICAgaWYgKGRhdGEuZmlsZXMuY29tcGlsZXJfc3VtbWFyeV9qc29uKSB7CiAgICAgICAgICAgIGxpbmtzSHRtbCArPSBgPGEgY2xhc3M9ImJ0biBidG4tZ2hvc3QiIGhyZWY9Ii9kb3dubG9hZC8ke2RhdGEuZmlsZXMuY29tcGlsZXJfc3VtbWFyeV9qc29ufSI+RG93bmxvYWQgY29tcGlsZXIgc3VtbWFyeTwvYT5gOwogICAgICAgICAgfQogICAgICAgICAgaWYgKGRhdGEuZmlsZXMudW5zdXBwb3J0ZWRfcmVwb3J0X3hsc3gpIHsKICAgICAgICAgICAgbGlua3NIdG1sICs9IGA8YSBjbGFzcz0iYnRuIGJ0bi1naG9zdCIgaHJlZj0iL2Rvd25sb2FkLyR7ZGF0YS5maWxlcy51bnN1cHBvcnRlZF9yZXBvcnRfeGxzeH0iPkRvd25sb2FkIG1hbnVhbCByZXZpZXcgbGlzdDwvYT5gOwogICAgICAgICAgfQogICAgICAgICAgbGlua3NIdG1sICs9IGA8YSBjbGFzcz0ibGluay1idG4iIGhyZWY9Ii9hdXRvLWFwcGx5Ij5PcGVuIGFwcGxpZXI8L2E+YDsKICAgICAgICAgIGxpbmtzSHRtbCArPSBgPC9kaXY+YDsKICAgICAgICAgIGRvd25sb2Fkc0VsLmlubmVySFRNTCA9IGxpbmtzSHRtbDsKICAgICAgICB9CiAgICAgICAgcmV0dXJuOwogICAgICB9CgogICAgICBzZXRUaW1lb3V0KHBvbGwsIDIwMDApOwogICAgfQoKICAgIHBvbGwoKTsKICA8L3NjcmlwdD4KeyUgZW5kYmxvY2sgJX0K","job_compiler.html":"PCFET0NUWVBFIGh0bWw+DQo8aHRtbCBsYW5nPSJlbiI+DQo8aGVhZD4NCiAgICA8bWV0YSBjaGFyc2V0PSJVVEYtOCI+DQogICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwgaW5pdGlhbC1zY2FsZT0xLjAiPg0KICAgIDx0aXRsZT5Kb2IgU2Nhbm5lciAmIENvbXBpbGVyIC0gQ2FyZWVyIFN1aXRlPC90aXRsZT4NCiAgICA8bGluayBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2Jvb3RzdHJhcEA1LjMuMC9kaXN0L2Nzcy9ib290c3RyYXAubWluLmNzcyIgcmVsPSJzdHlsZXNoZWV0Ij4NCiAgICA8c3R5bGU+DQogICAgICAgIGJvZHkgeyBiYWNrZ3JvdW5kLWNvbG9yOiAjZjhmOWZhOyB9DQogICAgICAgIC5jb250YWluZXIgeyBtYXgtd2lkdGg6IDkwMHB4OyBtYXJnaW4tdG9wOiAzMHB4OyBtYXJnaW4tYm90dG9tOiA1MHB4OyB9DQogICAgICAgIC5jYXJkIHsgYm9yZGVyOiBub25lOyBib3JkZXItcmFkaXVzOiAxMnB4OyBib3gtc2hhZG93OiAwIDRweCAxMnB4IHJnYmEoMCwwLDAsMC4wNSk7IG1hcmdpbi1ib3R0b206IDI0cHg7IH0NCiAgICAgICAgLmNhcmQtaGVhZGVyIHsgYmFja2dyb3VuZC1jb2xvcjogI2ZmZjsgYm9yZGVyLWJvdHRvbTogMXB4IHNvbGlkICNlZGYwZjI7IGZvbnQtd2VpZ2h0OiA2MDA7IHBhZGRpbmc6IDFyZW0gMS41cmVtOyBib3JkZXItcmFkaXVzOiAxMnB4IDEycHggMCAwICFpbXBvcnRhbnQ7IH0NCiAgICAgICAgLmF0cy1jaGVja2JveCB7IG1hcmdpbi1yaWdodDogMTJweDsgbWFyZ2luLWJvdHRvbTogOHB4OyBkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IH0NCiAgICA8L3N0eWxlPg0KPC9oZWFkPg0KPGJvZHk+DQoNCjxuYXYgY2xhc3M9Im5hdmJhciBuYXZiYXItZXhwYW5kLWxnIG5hdmJhci1kYXJrIGJnLWRhcmsgbWItNCI+DQogICAgPGRpdiBjbGFzcz0iY29udGFpbmVyLWZsdWlkIj4NCiAgICAgICAgPGEgY2xhc3M9Im5hdmJhci1icmFuZCIgaHJlZj0iLyI+Q2FyZWVyIFN1aXRlPC9hPg0KICAgICAgICA8ZGl2IGNsYXNzPSJjb2xsYXBzZSBuYXZiYXItY29sbGFwc2UiPg0KICAgICAgICAgICAgPHVsIGNsYXNzPSJuYXZiYXItbmF2IG1zLWF1dG8iPg0KICAgICAgICAgICAgICAgIDxsaSBjbGFzcz0ibmF2LWl0ZW0iPjxhIGNsYXNzPSJuYXYtbGluayIgaHJlZj0iLyI+RGFzaGJvYXJkPC9hPjwvbGk+DQogICAgICAgICAgICAgICAgPGxpIGNsYXNzPSJuYXYtaXRlbSI+PGEgY2xhc3M9Im5hdi1saW5rIiBocmVmPSIvc2NhbiI+TGlua2VkSW4gU2NyYXBlcjwvYT48L2xpPg0KICAgICAgICAgICAgICAgIDxsaSBjbGFzcz0ibmF2LWl0ZW0iPjxhIGNsYXNzPSJuYXYtbGluayIgaHJlZj0iL2F1dG8tYXBwbHkiPkF1dG8gQXBwbHk8L2E+PC9saT4NCiAgICAgICAgICAgICAgICA8bGkgY2xhc3M9Im5hdi1pdGVtIj48YSBjbGFzcz0ibmF2LWxpbmsgYWN0aXZlIiBocmVmPSIvam9iLWNvbXBpbGVyIj5Kb2IgQ29tcGlsZXI8L2E+PC9saT4NCiAgICAgICAgICAgIDwvdWw+DQogICAgICAgIDwvZGl2Pg0KICAgIDwvZGl2Pg0KPC9uYXY+DQoNCjxkaXYgY2xhc3M9ImNvbnRhaW5lciI+DQogICAgPGRpdiBjbGFzcz0iZC1mbGV4IGFsaWduLWl0ZW1zLWNlbnRlciBtYi00Ij4NCiAgICAgICAgPGgyIGNsYXNzPSJtLTAiPkpvYiBTY2FubmVyICYgQ29tcGlsZXI8L2gyPg0KICAgICAgICA8c3BhbiBjbGFzcz0iYmFkZ2UgYmctcHJpbWFyeSBtcy0zIj5BdGxhcyAmIEZlZWQgQWdncmVnYXRvcjwvc3Bhbj4NCiAgICA8L2Rpdj4NCiAgICA8cCBjbGFzcz0idGV4dC1tdXRlZCBtYi00Ij5TY2FuIG11bHRpcGxlIHN1cHBvcnRlZCBBVFMgcGxhdGZvcm1zIChHcmVlbmhvdXNlLCBMZXZlciwgV29ya2RheSwgZXRjLiksIGV4dHJhY3Qgam9icywgYW5kIGNvbXBpbGUgdGhlbSBpbnRvIHN0cnVjdHVyZWQgSlNPTiBmZWVkcyBhbmQgQXRsYXMgZGF0YSBtYXBwaW5nIHNldHMuPC9wPg0KDQogICAgeyUgaWYgZXJyb3IgJX0NCiAgICA8ZGl2IGNsYXNzPSJhbGVydCBhbGVydC1kYW5nZXIiPnt7IGVycm9yIH19PC9kaXY+DQogICAgeyUgZW5kaWYgJX0NCg0KICAgIDxmb3JtIGFjdGlvbj0iL2pvYi1jb21waWxlci9zdGFydCIgbWV0aG9kPSJQT1NUIj4NCiAgICAgICAgPGRpdiBjbGFzcz0iY2FyZCI+DQogICAgICAgICAgICA8ZGl2IGNsYXNzPSJjYXJkLWhlYWRlciI+MS4gU2VhcmNoIEZpbHRlcnM8L2Rpdj4NCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImNhcmQtYm9keSI+DQogICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ibWItMyI+DQogICAgICAgICAgICAgICAgICAgIDxsYWJlbCBjbGFzcz0iZm9ybS1sYWJlbCB0ZXh0LW11dGVkIGZ3LXNlbWlib2xkIj5UYXJnZXQgUm9sZXMgLyBRdWVyaWVzPC9sYWJlbD4NCiAgICAgICAgICAgICAgICAgICAgPGlucHV0IHR5cGU9InRleHQiIG5hbWU9InF1ZXJ5IiBjbGFzcz0iZm9ybS1jb250cm9sIiBwbGFjZWhvbGRlcj0iZS5nLiBJbnRlcm4sIFNvZnR3YXJlIEVuZ2luZWVyIE5ldyBHcmFkLCBEYXRhIEFuYWx5c3QiIHJlcXVpcmVkPg0KICAgICAgICAgICAgICAgIDwvZGl2Pg0KICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9InJvdyI+DQogICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImNvbC1tZC02IG1iLTMiPg0KICAgICAgICAgICAgICAgICAgICAgICAgPGxhYmVsIGNsYXNzPSJmb3JtLWxhYmVsIHRleHQtbXV0ZWQgZnctc2VtaWJvbGQiPlRhcmdldCBDb21wYW5pZXMgKENvbW1hIHNlcGFyYXRlZCk8L2xhYmVsPg0KICAgICAgICAgICAgICAgICAgICAgICAgPHRleHRhcmVhIG5hbWU9ImNvbXBhbmllcyIgY2xhc3M9ImZvcm0tY29udHJvbCIgcm93cz0iMyIgcGxhY2Vob2xkZXI9ImUuZy4gU3RyaXBlLCBDb2luYmFzZSwgU2NhbGUgQUkiPjwvdGV4dGFyZWE+DQogICAgICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb3JtLXRleHQiPkxlYXZlIGJsYW5rIHRvIGRvIGEgd2lkZSBnZW5lcmljIHNlYXJjaC48L2Rpdj4NCiAgICAgICAgICAgICAgICAgICAgPC9kaXY+DQogICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImNvbC1tZC02IG1iLTMiPg0KICAgICAgICAgICAgICAgICAgICAgICAgPGxhYmVsIGNsYXNzPSJmb3JtLWxhYmVsIHRleHQtbXV0ZWQgZnctc2VtaWJvbGQiPlRhcmdldCBMb2NhdGlvbnMgKENvbW1hIHNlcGFyYXRlZCk8L2xhYmVsPg0KICAgICAgICAgICAgICAgICAgICAgICAgPHRleHRhcmVhIG5hbWU9ImxvY2F0aW9ucyIgY2xhc3M9ImZvcm0tY29udHJvbCIgcm93cz0iMyIgcGxhY2Vob2xkZXI9ImUuZy4gUmVtb3RlLCBTYW4gRnJhbmNpc2NvLCBOZXcgWW9yayI+PC90ZXh0YXJlYT4NCiAgICAgICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvcm0tdGV4dCI+Q29tcGlsZXIgd2lsbCBncm91cCBvdXRwdXRzIGdlb2dyYXBoaWNhbGx5IGJhc2VkIG9uIHRoZXNlLjwvZGl2Pg0KICAgICAgICAgICAgICAgICAgICA8L2Rpdj4NCiAgICAgICAgICAgICAgICA8L2Rpdj4NCiAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJtYi0wIj4NCiAgICAgICAgICAgICAgICAgICAgPGxhYmVsIGNsYXNzPSJmb3JtLWxhYmVsIHRleHQtbXV0ZWQgZnctc2VtaWJvbGQiPktleXdvcmRzPC9sYWJlbD4NCiAgICAgICAgICAgICAgICAgICAgPGlucHV0IHR5cGU9InRleHQiIG5hbWU9ImtleXdvcmRzIiBjbGFzcz0iZm9ybS1jb250cm9sIiBwbGFjZWhvbGRlcj0iZS5nLiBQeXRob24sIFJlYWN0LCBQcm9kdWN0IE1hbmFnZW1lbnQiPg0KICAgICAgICAgICAgICAgIDwvZGl2Pg0KICAgICAgICAgICAgPC9kaXY+DQogICAgICAgIDwvZGl2Pg0KDQogICAgICAgIDxkaXYgY2xhc3M9ImNhcmQiPgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJjYXJkLWhlYWRlciI+Mi4gRGF0YSBTb3VyY2VzPC9kaXY+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImNhcmQtYm9keSBwYi0yIj4KICAgICAgICAgICAgICAgIDxwIGNsYXNzPSJ0ZXh0LW11dGVkIHNtYWxsIG1iLTMiPkNvbWJpbmUgbmF0aXZlIEFUUyBzY2FubmluZyB3aXRoIHRoZSBwdWJsaWMgQVRTIGZlZWQgaW5zcGlyZWQgYnkgdGhlIEFUUyBTY3JhcGVycyByZXBvLiBLZWVwIGF0IGxlYXN0IG9uZSBzb3VyY2Ugc2VsZWN0ZWQuPC9wPgogICAgICAgICAgICAgICAgPGRpdj4KICAgICAgICAgICAgICAgICAgICB7JSBmb3Iga2V5LCBsYWJlbCBpbiBjb21waWxlcl9zb3VyY2VzLml0ZW1zKCkgJX0KICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb3JtLWNoZWNrIGF0cy1jaGVja2JveCI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxpbnB1dCBjbGFzcz0iZm9ybS1jaGVjay1pbnB1dCIgdHlwZT0iY2hlY2tib3giIG5hbWU9ImRhdGFfc291cmNlcyIgdmFsdWU9Int7IGtleSB9fSIgaWQ9InNvdXJjZV97eyBrZXkgfX0iIHslIGlmIGtleSA9PSAiaW50ZXJuYWwiICV9Y2hlY2tlZHslIGVuZGlmICV9PgogICAgICAgICAgICAgICAgICAgICAgICA8bGFiZWwgY2xhc3M9ImZvcm0tY2hlY2stbGFiZWwiIGZvcj0ic291cmNlX3t7IGtleSB9fSI+e3sgbGFiZWwgfX08L2xhYmVsPgogICAgICAgICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgIDwvZGl2PgoKICAgICAgICA8ZGl2IGNsYXNzPSJjYXJkIj4KICAgICAgICAgICAgPGRpdiBjbGFzcz0iY2FyZC1oZWFkZXIiPjMuIEFUUyBQbGF0Zm9ybSBUYXJnZXRzPC9kaXY+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImNhcmQtYm9keSBwYi0yIj4KICAgICAgICAgICAgICAgIDxwIGNsYXNzPSJ0ZXh0LW11dGVkIHNtYWxsIG1iLTMiPlNlbGVjdCB0aGUgQVRTIHBsYXRmb3JtcyB0byBuYXRpdmVseSBzY3JhcGUuIExlYXZpbmcgYWxsIHVuY2hlY2tlZCBkZWZhdWx0cyB0byBzY2FubmluZyBhbGwgYXZhaWxhYmxlIHBsYXRmb3Jtcy48L3A+CiAgICAgICAgICAgICAgICA8ZGl2PgogICAgICAgICAgICAgICAgICAgIHslIGZvciBwbGF0Zm9ybSBpbiBhdHNfcGxhdGZvcm1zICV9CiAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0iZm9ybS1jaGVjayBhdHMtY2hlY2tib3giPgogICAgICAgICAgICAgICAgICAgICAgICA8aW5wdXQgY2xhc3M9ImZvcm0tY2hlY2staW5wdXQiIHR5cGU9ImNoZWNrYm94IiBuYW1lPSJzb3VyY2VzIiB2YWx1ZT0ie3sgcGxhdGZvcm0gfX0iIGlkPSJhdHNfe3sgcGxhdGZvcm0gfX0iPgogICAgICAgICAgICAgICAgICAgICAgICA8bGFiZWwgY2xhc3M9ImZvcm0tY2hlY2stbGFiZWwiIGZvcj0iYXRzX3t7IHBsYXRmb3JtIH19Ij57eyBwbGF0Zm9ybSB9fTwvbGFiZWw+CiAgICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImNhcmQiPgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJjYXJkLWhlYWRlciI+NC4gT3V0cHV0IEZlZWRzPC9kaXY+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImNhcmQtYm9keSBwYi0yIj4KICAgICAgICAgICAgICAgIDxwIGNsYXNzPSJ0ZXh0LW11dGVkIHNtYWxsIG1iLTMiPkdlbmVyYXRlIG91dHB1dHMgaW5zcGlyZWQgYnkgSW50ZXJuQXRsYXMgYW5kIHRoZSBjYXJlZXItc2l0ZSBmZWVkIHNjaGVtYS48L3A+CiAgICAgICAgICAgICAgICA8ZGl2PgogICAgICAgICAgICAgICAgICAgIHslIGZvciBrZXksIGxhYmVsIGluIGNvbXBpbGVyX2V4cG9ydHMuaXRlbXMoKSAlfQogICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvcm0tY2hlY2sgYXRzLWNoZWNrYm94Ij4KICAgICAgICAgICAgICAgICAgICAgICAgPGlucHV0IGNsYXNzPSJmb3JtLWNoZWNrLWlucHV0IiB0eXBlPSJjaGVja2JveCIgbmFtZT0iZXhwb3J0cyIgdmFsdWU9Int7IGtleSB9fSIgaWQ9ImV4cG9ydF97eyBrZXkgfX0iIGNoZWNrZWQ+CiAgICAgICAgICAgICAgICAgICAgICAgIDxsYWJlbCBjbGFzcz0iZm9ybS1jaGVjay1sYWJlbCIgZm9yPSJleHBvcnRfe3sga2V5IH19Ij57eyBsYWJlbCB9fTwvbGFiZWw+CiAgICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImNhcmQiPgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJjYXJkLWhlYWRlciI+NS4gQ29tcGlsZXIgTGltaXRzPC9kaXY+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImNhcmQtYm9keSI+CiAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJyb3ciPgogICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImNvbC1tZC02IG1iLTMiPgogICAgICAgICAgICAgICAgICAgICAgICA8bGFiZWwgY2xhc3M9ImZvcm0tbGFiZWwgdGV4dC1tdXRlZCBmdy1zZW1pYm9sZCI+TGltaXQgcGVyIFNvdXJjZS9Db21wYW55PC9sYWJlbD4KICAgICAgICAgICAgICAgICAgICAgICAgPGlucHV0IHR5cGU9Im51bWJlciIgbmFtZT0ibGltaXRfcGVyX3NvdXJjZSIgY2xhc3M9ImZvcm0tY29udHJvbCIgdmFsdWU9IjEwMCIgbWluPSIxMCIgbWF4PSIxMDAwIj4KICAgICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0iZm9ybS10ZXh0Ij5NYXhpbXVtIGpvYnMgdG8gcHVsbCBwZXIgaW5kaXZpZHVhbCBjb21wYW55IHBhZ2UuPC9kaXY+CiAgICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0iY29sLW1kLTYgbWItMyI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxsYWJlbCBjbGFzcz0iZm9ybS1sYWJlbCB0ZXh0LW11dGVkIGZ3LXNlbWlib2xkIj5NYXggU2VhcmNoIFBhZ2VzPC9sYWJlbD4KICAgICAgICAgICAgICAgICAgICAgICAgPGlucHV0IHR5cGU9Im51bWJlciIgbmFtZT0ibWF4X3BhZ2VzIiBjbGFzcz0iZm9ybS1jb250cm9sIiB2YWx1ZT0iNSIgbWluPSIxIiBtYXg9IjUwIj4KICAgICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0iZm9ybS10ZXh0Ij5NYXhpbXVtIHBhZ2luYXRpb24gZGVwdGggZm9yIHNlYXJjaCBxdWVyaWVzLjwvZGl2PgogICAgICAgICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgIDwvZGl2PgoNCiAgICAgICAgPGRpdiBjbGFzcz0iZC1mbGV4IGp1c3RpZnktY29udGVudC1lbmQgZ2FwLTIgbWItNSI+DQogICAgICAgICAgICA8YnV0dG9uIHR5cGU9InN1Ym1pdCIgY2xhc3M9ImJ0biBidG4tcHJpbWFyeSBweC00IGZ3LWJvbGQiPkNvbXBpbGUgSm9icyAmIEdlbmVyYXRlIEZlZWQ8L2J1dHRvbj4NCiAgICAgICAgPC9kaXY+DQogICAgPC9mb3JtPg0KPC9kaXY+DQoNCjxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2Jvb3RzdHJhcEA1LjMuMC9kaXN0L2pzL2Jvb3RzdHJhcC5idW5kbGUubWluLmpzIj48L3NjcmlwdD4NCjwvYm9keT4NCjwvaHRtbD4K","linkedin_posts.html":"77u/eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBoZWFkICV9CiAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJ7eyB1cmxfZm9yKCdzdGF0aWMnLCBmaWxlbmFtZT0nbGlua2VkaW4uY3NzJykgfX0iIC8+CnslIGVuZGJsb2NrICV9CnslIGJsb2NrIGNvbnRlbnQgJX0KICA8ZGl2IGNsYXNzPSJsaS1zaGVsbCBsaS1wYWdlIj4KICAgIDxoZWFkZXIgY2xhc3M9ImxpLWhlcm8iPgogICAgICA8ZGl2PgogICAgICAgIDxkaXYgY2xhc3M9ImxpLWtpY2tlciI+TGlua2VkSW4gQUkgUG9zdHM8L2Rpdj4KICAgICAgICA8aDE+R2VuZXJhdGUgTGlua2VkSW4gUG9zdHM8L2gxPgogICAgICAgIDxwIGNsYXNzPSJsaS1zdWJ0aXRsZSI+Q3JlYXRlIGEgcG9saXNoZWQgTGlua2VkSW4gcG9zdCBpbiBzZWNvbmRzIHdpdGggR2VtaW5pLjwvcD4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImxpLWhlcm8tbWV0YSI+CiAgICAgICAgPHNwYW4gY2xhc3M9ImxpLXBpbGwge3sgJ29uJyBpZiBnZW1pbmlfZW5hYmxlZCBlbHNlICdvZmYnIH19Ij4KICAgICAgICAgIEdlbWluaSB7eyAnY29ubmVjdGVkJyBpZiBnZW1pbmlfZW5hYmxlZCBlbHNlICdub3QgY29ubmVjdGVkJyB9fQogICAgICAgIDwvc3Bhbj4KICAgICAgPC9kaXY+CiAgICA8L2hlYWRlcj4KCiAgICB7JSBpZiBlcnJvciAlfQogICAgICA8ZGl2IGNsYXNzPSJsaS1hbGVydCI+e3sgZXJyb3IgfX08L2Rpdj4KICAgIHslIGVuZGlmICV9CgogICAgPGRpdiBjbGFzcz0ibGktZ3JpZCI+CiAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQiPgogICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgICA8aDM+UG9zdCBpbnB1dHM8L2gzPgogICAgICAgIDwvZGl2PgogICAgICAgIDxmb3JtIG1ldGhvZD0icG9zdCIgY2xhc3M9ImxpLWZvcm0iPgogICAgICAgICAgPGxhYmVsIGZvcj0idG9waWMiPlRvcGljIG9yIGhvb2s8L2xhYmVsPgogICAgICAgICAgPHRleHRhcmVhIGlkPSJ0b3BpYyIgbmFtZT0idG9waWMiIHJvd3M9IjQiIHBsYWNlaG9sZGVyPSJlLmcuLCAzIGxlc3NvbnMgZnJvbSBsZWFkaW5nIGEgcHJvZHVjdCBsYXVuY2ggdGhhdCBkb3VibGVkIGFkb3B0aW9uIiByZXF1aXJlZD48L3RleHRhcmVhPgoKICAgICAgICAgIDxsYWJlbCBmb3I9ImF1ZGllbmNlIj5BdWRpZW5jZTwvbGFiZWw+CiAgICAgICAgICA8aW5wdXQgaWQ9ImF1ZGllbmNlIiBuYW1lPSJhdWRpZW5jZSIgdHlwZT0idGV4dCIgcGxhY2Vob2xkZXI9ImUuZy4sIFNhYVMgZm91bmRlcnMsIHByb2R1Y3QgbWFuYWdlcnMiIC8+CgogICAgICAgICAgPGxhYmVsIGZvcj0idG9uZSI+VG9uZTwvbGFiZWw+CiAgICAgICAgICA8aW5wdXQgaWQ9InRvbmUiIG5hbWU9InRvbmUiIHR5cGU9InRleHQiIHBsYWNlaG9sZGVyPSJlLmcuLCBjb25maWRlbnQsIHByYWN0aWNhbCwgc2xpZ2h0bHkgYm9sZCIgLz4KCiAgICAgICAgICA8bGFiZWwgZm9yPSJsZW5ndGgiPkxlbmd0aDwvbGFiZWw+CiAgICAgICAgICA8aW5wdXQgaWQ9Imxlbmd0aCIgbmFtZT0ibGVuZ3RoIiB0eXBlPSJ0ZXh0IiBwbGFjZWhvbGRlcj0iZS5nLiwgMTIwLTE4MCB3b3JkcyIgLz4KCiAgICAgICAgICA8bGFiZWwgZm9yPSJrZXl3b3JkcyI+S2V5d29yZHMgdG8gaW5jbHVkZTwvbGFiZWw+CiAgICAgICAgICA8aW5wdXQgaWQ9ImtleXdvcmRzIiBuYW1lPSJrZXl3b3JkcyIgdHlwZT0idGV4dCIgcGxhY2Vob2xkZXI9ImUuZy4sIEdUTSwgcmV0ZW50aW9uLCBQTEciIC8+CgogICAgICAgICAgPGxhYmVsIGZvcj0iY3RhIj5DYWxsIHRvIGFjdGlvbjwvbGFiZWw+CiAgICAgICAgICA8aW5wdXQgaWQ9ImN0YSIgbmFtZT0iY3RhIiB0eXBlPSJ0ZXh0IiBwbGFjZWhvbGRlcj0iZS5nLiwgQXNrIHJlYWRlcnMgdG8gc2hhcmUgdGhlaXIgYXBwcm9hY2giIC8+CgogICAgICAgICAgPGxhYmVsPgogICAgICAgICAgICA8aW5wdXQgdHlwZT0iY2hlY2tib3giIG5hbWU9InVzZV9lbW9qaXMiIC8+IFVzZSBlbW9qaXMKICAgICAgICAgIDwvbGFiZWw+CgogICAgICAgICAgPGJ1dHRvbiBjbGFzcz0ibGktYnRuIiB0eXBlPSJzdWJtaXQiPkdlbmVyYXRlIHBvc3Q8L2J1dHRvbj4KICAgICAgICA8L2Zvcm0+CiAgICAgIDwvZGl2PgoKICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZCI+CiAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICAgIDxoMz5HZW5lcmF0ZWQgcG9zdDwvaDM+CiAgICAgICAgICA8YnV0dG9uIGNsYXNzPSJsaS1jb3B5IiB0eXBlPSJidXR0b24iIGRhdGEtY29weS10YXJnZXQ9ImxpLXBvc3Qtb3V0cHV0Ij5Db3B5PC9idXR0b24+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBpZD0ibGktcG9zdC1vdXRwdXQiIGNsYXNzPSJsaS1jb3B5LWJsb2NrIj57eyBvdXRwdXQgb3IgJ1lvdXIgcG9zdCB3aWxsIGFwcGVhciBoZXJlLicgfX08L2Rpdj4KICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+VGlwOiBSZWdlbmVyYXRlIHdpdGggYSBzaGFycGVyIGhvb2sgb3Igc3BlY2lmaWMgb3V0Y29tZSBmb3IgaGlnaGVyIGVuZ2FnZW1lbnQuPC9wPgogICAgICA8L2Rpdj4KICAgIDwvZGl2PgogIDwvZGl2Pgp7JSBlbmRibG9jayAlfQp7JSBibG9jayBzY3JpcHRzICV9CiAgPHNjcmlwdCBzcmM9Int7IHVybF9mb3IoJ3N0YXRpYycsIGZpbGVuYW1lPSdsaW5rZWRpbi5qcycpIH19Ij48L3NjcmlwdD4KeyUgZW5kYmxvY2sgJX0NCg==","linkedin_review.html":"77u/eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBoZWFkICV9CiAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJ7eyB1cmxfZm9yKCdzdGF0aWMnLCBmaWxlbmFtZT0nbGlua2VkaW4uY3NzJykgfX0iIC8+CnslIGVuZGJsb2NrICV9CnslIGJsb2NrIHNjcmlwdHMgJX0KICA8c2NyaXB0IHNyYz0ie3sgdXJsX2Zvcignc3RhdGljJywgZmlsZW5hbWU9J2xpbmtlZGluLmpzJykgfX0iPjwvc2NyaXB0Pgp7JSBlbmRibG9jayAlfQp7JSBibG9jayBjb250ZW50ICV9CiAgPGRpdiBjbGFzcz0ibGktc2hlbGwgbGktcGFnZSI+CiAgICA8aGVhZGVyIGNsYXNzPSJsaS1oZXJvIj4KICAgICAgPGRpdj4KICAgICAgICA8ZGl2IGNsYXNzPSJsaS1raWNrZXIiPkdlbWluaSBMaW5rZWRJbiBBbmFseXplcjwvZGl2PgogICAgICAgIDxoMT5MaW5rZWRJbiBQcm9maWxlIEFuYWx5emVyPC9oMT4KICAgICAgICA8cCBjbGFzcz0ibGktc3VidGl0bGUiPlNjYW4gYSBwcm9maWxlIGluIHNlY29uZHMuIFBhc3RlIHRleHQsIHVwbG9hZCBhIFBERiBvciBET0NYIGV4cG9ydCwgb3IgdXNlIGEgTGlua2VkSW4gVVJMLjwvcD4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImxpLWhlcm8tbWV0YSI+CiAgICAgICAgPHNwYW4gY2xhc3M9ImxpLXBpbGwge3sgJ29uJyBpZiBnZW1pbmlfZW5hYmxlZCBlbHNlICdvZmYnIH19Ij4KICAgICAgICAgIEdlbWluaSB7eyAnY29ubmVjdGVkJyBpZiBnZW1pbmlfZW5hYmxlZCBlbHNlICdub3QgY29ubmVjdGVkJyB9fQogICAgICAgIDwvc3Bhbj4KICAgICAgPC9kaXY+CiAgICA8L2hlYWRlcj4KCiAgICB7JSBpZiBlcnJvciAlfQogICAgICA8ZGl2IGNsYXNzPSJsaS1hbGVydCI+e3sgZXJyb3IgfX08L2Rpdj4KICAgIHslIGVuZGlmICV9CgogICAgPGRpdiBjbGFzcz0ibGktZ3JpZCI+CiAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQiPgogICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgICA8aDM+UnVuIGEgbmV3IHNjYW48L2gzPgogICAgICAgICAgPHNwYW4gY2xhc3M9ImxpLXRhZyI+djIgcmVidWlsZDwvc3Bhbj4KICAgICAgICA8L2Rpdj4KICAgICAgICA8Zm9ybSBtZXRob2Q9InBvc3QiIGVuY3R5cGU9Im11bHRpcGFydC9mb3JtLWRhdGEiIGNsYXNzPSJsaS1mb3JtIj4KICAgICAgICAgIDxsYWJlbCBmb3I9InByb2ZpbGVfdXJsIj5MaW5rZWRJbiBVUkw8L2xhYmVsPgogICAgICAgICAgPGlucHV0IGlkPSJwcm9maWxlX3VybCIgbmFtZT0icHJvZmlsZV91cmwiIHR5cGU9InRleHQiIHBsYWNlaG9sZGVyPSJodHRwczovL3d3dy5saW5rZWRpbi5jb20vaW4vdXNlcm5hbWUiIC8+CgogICAgICAgICAgPGxhYmVsIGZvcj0icHJvZmlsZV90ZXh0Ij5QYXN0ZSBwcm9maWxlIHRleHQ8L2xhYmVsPgogICAgICAgICAgPHRleHRhcmVhIGlkPSJwcm9maWxlX3RleHQiIG5hbWU9InByb2ZpbGVfdGV4dCIgcm93cz0iNiIgcGxhY2Vob2xkZXI9IlBhc3RlIHlvdXIgQWJvdXQsIEV4cGVyaWVuY2UsIFNraWxscywgYW5kIEVkdWNhdGlvbiBzZWN0aW9ucyBoZXJlIj48L3RleHRhcmVhPgoKICAgICAgICAgIDxsYWJlbCBmb3I9InByb2ZpbGVfZmlsZSI+VXBsb2FkIFBERiBvciBET0NYIGV4cG9ydDwvbGFiZWw+CiAgICAgICAgICA8aW5wdXQgaWQ9InByb2ZpbGVfZmlsZSIgbmFtZT0icHJvZmlsZV9maWxlIiB0eXBlPSJmaWxlIiAvPgoKICAgICAgICAgIDxidXR0b24gY2xhc3M9ImxpLWJ0biIgdHlwZT0ic3VibWl0Ij5BbmFseXplIHByb2ZpbGU8L2J1dHRvbj4KICAgICAgICAgIDxwIGNsYXNzPSJsaS1ub3RlIj5Qcml2YXRlIHByb2ZpbGVzIHJlcXVpcmUgTGlua2VkSW4gY3JlZGVudGlhbHMgaW4gYC5lbnZgIHRvIGZldGNoIGNvbnRlbnQuPC9wPgogICAgICAgIDwvZm9ybT4KICAgICAgPC9kaXY+CgogICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkIj4KICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkLWhlYWQiPgogICAgICAgICAgPGgzPldoYXQgeW91IGdldDwvaDM+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPHVsIGNsYXNzPSJsaS1saXN0Ij4KICAgICAgICAgIDxsaT5Qcm9maWxlIHNjb3JlIGFuZCBzZWN0aW9uIGRpYWdub3N0aWNzPC9saT4KICAgICAgICAgIDxsaT5Ub3AgaXNzdWVzIGFuZCBxdWljayB3aW5zPC9saT4KICAgICAgICAgIDxsaT5LZXl3b3JkIGdhcHMgYW5kIHJvbGUgYWxpZ25tZW50PC9saT4KICAgICAgICAgIDxsaT5BSSByZXdyaXRlIGZvciBoZWFkbGluZSwgQWJvdXQsIGFuZCBleHBlcmllbmNlIGJ1bGxldHM8L2xpPgogICAgICAgICAgPGxpPkFjdGlvbiBwbGFuIHdpdGggbmV4dCBzdGVwczwvbGk+CiAgICAgICAgPC91bD4KICAgICAgICA8ZGl2IGNsYXNzPSJsaS1kaXZpZGVyIj48L2Rpdj4KICAgICAgICA8ZGl2IGNsYXNzPSJsaS1taW5pLWdyaWQiPgogICAgICAgICAgPGRpdj4KICAgICAgICAgICAgPHAgY2xhc3M9ImxpLW1pbmktdGl0bGUiPkJlc3QgaW5wdXQ8L3A+CiAgICAgICAgICAgIDxwIGNsYXNzPSJsaS1taW5pLWJvZHkiPkV4cG9ydGVkIFBERiBvciBwYXN0ZWQgcHJvZmlsZSB0ZXh0IGdpdmVzIHRoZSByaWNoZXN0IHJlc3VsdHMuPC9wPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2PgogICAgICAgICAgICA8cCBjbGFzcz0ibGktbWluaS10aXRsZSI+RmFzdCBtb2RlPC9wPgogICAgICAgICAgICA8cCBjbGFzcz0ibGktbWluaS1ib2R5Ij5Vc2UgYSBwdWJsaWMgVVJMIGZvciBxdWljayBzY2FucyBhbmQgYmFzZWxpbmUgaW5zaWdodHMuPC9wPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CiAgICAgIDwvZGl2PgogICAgPC9kaXY+CgogICAgeyUgc2V0IHRyZW5kID0gdHJlbmRfaGlzdG9yeSBpZiB0cmVuZF9oaXN0b3J5IGlzIGRlZmluZWQgZWxzZSBoaXN0b3J5ICV9CiAgICB7JSBpZiB0cmVuZCBhbmQgdHJlbmR8bGVuZ3RoICV9CiAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQgbGktY2hhcnQiPgogICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgICA8aDM+U2NvcmUgdHJlbmQ8L2gzPgogICAgICAgICAgPHNwYW4gY2xhc3M9ImxpLXRhZyI+UGFzdCB2cyBub3cgdnMgcG90ZW50aWFsPC9zcGFuPgogICAgICAgIDwvZGl2PgogICAgICAgIDxjYW52YXMgaWQ9ImxpU2NvcmVUcmVuZCIgaGVpZ2h0PSIxNDAiIGRhdGEtaGlzdG9yeT0ne3sgdHJlbmQgfCB0b2pzb24gfX0nPjwvY2FudmFzPgogICAgICAgIDxkaXYgY2xhc3M9ImxpLWxlZ2VuZCI+CiAgICAgICAgICA8c3Bhbj48aSBjbGFzcz0ibGktZG90IGxpLWRvdC1wYXN0Ij48L2k+UGFzdDwvc3Bhbj4KICAgICAgICAgIDxzcGFuPjxpIGNsYXNzPSJsaS1kb3QgbGktZG90LW5vdyI+PC9pPkN1cnJlbnQ8L3NwYW4+CiAgICAgICAgICA8c3Bhbj48aSBjbGFzcz0ibGktZG90IGxpLWRvdC1wb3RlbnRpYWwiPjwvaT5Qb3RlbnRpYWw8L3NwYW4+CiAgICAgICAgPC9kaXY+CiAgICAgIDwvZGl2PgogICAgeyUgZW5kaWYgJX0KCiAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkIj4KICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICA8aDM+UmVjZW50IHNjYW5zPC9oMz4KICAgICAgICA8ZGl2IGNsYXNzPSJwYWdlciI+CiAgICAgICAgICB7JSBpZiB2aWV3X2FsbCAlfQogICAgICAgICAgICA8YSBjbGFzcz0iYnRuIGJ0bi1naG9zdCIgaHJlZj0iL2xpbmtlZGluLXJldmlldz9wYWdlPTEiPlBhZ2luYXRlPC9hPgogICAgICAgICAgeyUgZWxzZSAlfQogICAgICAgICAgICA8YSBjbGFzcz0iYnRuIGJ0bi1naG9zdCIgaHJlZj0iL2xpbmtlZGluLXJldmlldz92aWV3PWFsbCI+RXhwYW5kIGFsbDwvYT4KICAgICAgICAgICAgeyUgaWYgcGFnZSA+IDEgJX0KICAgICAgICAgICAgICA8YSBjbGFzcz0iYnRuIGJ0bi1naG9zdCIgaHJlZj0iL2xpbmtlZGluLXJldmlldz9wYWdlPXt7IHBhZ2UgLSAxIH19Ij5QcmV2PC9hPgogICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgICB7JSBpZiBwYWdlIDwgdG90YWxfcGFnZXMgJX0KICAgICAgICAgICAgICA8YSBjbGFzcz0iYnRuIGJ0bi1naG9zdCIgaHJlZj0iL2xpbmtlZGluLXJldmlldz9wYWdlPXt7IHBhZ2UgKyAxIH19Ij5OZXh0PC9hPgogICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgICA8c3BhbiBjbGFzcz0ibGktbm90ZSI+UGFnZSB7eyBwYWdlIH19IC8ge3sgdG90YWxfcGFnZXMgfX08L3NwYW4+CiAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgIDwvZGl2PgogICAgICA8L2Rpdj4KICAgICAgeyUgaWYgaGlzdG9yeSBhbmQgaGlzdG9yeXxsZW5ndGggJX0KICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+U2hvd2luZyB7eyBwYWdlX2NvdW50IH19IG9mIHt7IHRvdGFsX2NvdW50IH19IHNjYW5zLjwvcD4KICAgICAgICA8ZGl2IGNsYXNzPSJsaS10YWJsZSI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS10YWJsZS1oZWFkIj4KICAgICAgICAgICAgPHNwYW4+VGltZXN0YW1wPC9zcGFuPgogICAgICAgICAgICA8c3Bhbj5TY29yZTwvc3Bhbj4KICAgICAgICAgICAgPHNwYW4+SXNzdWVzPC9zcGFuPgogICAgICAgICAgICA8c3Bhbj48L3NwYW4+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIHslIGZvciBpdGVtIGluIGhpc3RvcnkgJX0KICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktdGFibGUtcm93Ij4KICAgICAgICAgICAgICA8c3Bhbj57eyBpdGVtLnRpbWVzdGFtcCB9fTwvc3Bhbj4KICAgICAgICAgICAgICA8c3BhbiBjbGFzcz0ibGktbW9ubyI+e3sgaXRlbS5vdmVyYWxsX3Njb3JlIH19PC9zcGFuPgogICAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJsaS1tb25vIj57eyBpdGVtLmlzc3Vlc19jb3VudCB9fTwvc3Bhbj4KICAgICAgICAgICAgICA8YSBjbGFzcz0ibGktbGluayIgaHJlZj0iL2xpbmtlZGluLXJldmlldy97eyBpdGVtLmlkIH19Ij5WaWV3PC9hPgogICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgIDwvZGl2PgogICAgICB7JSBlbHNlICV9CiAgICAgICAgPHAgY2xhc3M9ImxpLW5vdGUiPk5vIHNjYW5zIHlldC48L3A+CiAgICAgIHslIGVuZGlmICV9CiAgICA8L2Rpdj4KICA8L2Rpdj4KeyUgZW5kYmxvY2sgJX0NCg==","linkedin_review_detail.html":"77u/eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBoZWFkICV9CiAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJ7eyB1cmxfZm9yKCdzdGF0aWMnLCBmaWxlbmFtZT0nbGlua2VkaW4uY3NzJykgfX0iIC8+CnslIGVuZGJsb2NrICV9CnslIGJsb2NrIGNvbnRlbnQgJX0KICB7JSBzZXQgYWkgPSByZXZpZXcuYWkgb3Ige30gJX0KICB7JSBzZXQgc3RhdHMgPSByZXZpZXcuc3RhdHMgb3Ige30gJX0KICB7JSBzZXQgYnJlYWtkb3duID0gcmV2aWV3LmJyZWFrZG93biBvciB7fSAlfQogIHslIHNldCBrZXl3b3JkcyA9IGFpLmdldCgna2V5d29yZF9hbmFseXNpcycpIG9yIHJldmlldy5nZXQoJ2FpX2tleXdvcmRzJykgb3Ige30gJX0KICB7JSBzZXQgZm9jdXNfaXRlbXMgPSBhaS5nZXQoJ2ZvY3VzX2FyZWFzJykgb3IgcmV2aWV3LmdldCgnYWlfZm9jdXNfYXJlYXMnKSBvciBbXSAlfQogIHslIHNldCBhY3Rpb25fcGxhbiA9IGFpLmdldCgnYWN0aW9uX3BsYW4nKSBvciBbXSAlfQogIHslIHNldCBoZWFkbGluZSA9IGFpLmdldCgnaGVhZGxpbmUnKSBvciB7fSAlfQogIHslIHNldCBhYm91dCA9IGFpLmdldCgnYWJvdXQnKSBvciB7fSAlfQogIHslIHNldCBleHBlcmllbmNlX2J1bGxldHMgPSBhaS5nZXQoJ2V4cGVyaWVuY2VfYnVsbGV0cycpIG9yIFtdICV9CiAgeyUgc2V0IHN1bW1hcnkgPSBhaS5nZXQoJ3N1bW1hcnknKSBvciAnJyAlfQogIHslIHNldCB0b3Bfa2V5d29yZHMgPSBrZXl3b3Jkcy5nZXQoJ3RvcF9rZXl3b3JkcycpIG9yIHJldmlldy5nZXQoJ2tleXdvcmRfdG9wJykgb3IgW10gJX0KICB7JSBzZXQgbWlzc2luZ19rZXl3b3JkcyA9IGtleXdvcmRzLmdldCgnbWlzc2luZ19rZXl3b3JkcycpIG9yIFtdICV9CiAgeyUgc2V0IHJvbGVfa2V5d29yZHMgPSBrZXl3b3Jkcy5nZXQoJ3JvbGVfa2V5d29yZHMnKSBvciBbXSAlfQogIHslIHNldCBhbmFseXRpY3MgPSByZXZpZXcucG9zdF9hbmFseXRpY3Mgb3IgcmV2aWV3LmdldCgncG9zdF9hbmFseXRpY3MnKSBvciB7fSAlfQoKICA8ZGl2IGNsYXNzPSJsaS1zaGVsbCBsaS1kZXRhaWwiIGRhdGEtcmV2aWV3LWlkPSJ7eyByZXZpZXcuaWQgfX0iPgogICAgPGhlYWRlciBjbGFzcz0ibGktaGVybyI+CiAgICAgIDxkaXY+CiAgICAgICAgPGRpdiBjbGFzcz0ibGkta2lja2VyIj5MaW5rZWRJbiBQcm9maWxlIEludGVsbGlnZW5jZTwvZGl2PgogICAgICAgIDxoMT5Qcm9maWxlIEludGVsbGlnZW5jZTwvaDE+CiAgICAgICAgPHAgY2xhc3M9ImxpLXN1YnRpdGxlIj5TY2FuIGNyZWF0ZWQge3sgcmV2aWV3LnRpbWVzdGFtcCBvciAnJyB9fSAtIFNvdXJjZSB7eyByZXZpZXcuc291cmNlIG9yICdmaWxlJyB9fTwvcD4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImxpLXNjb3JlIiBzdHlsZT0iLS1zY29yZToge3sgcmV2aWV3Lm92ZXJhbGxfc2NvcmUgb3IgMCB9fTsiPgogICAgICAgIDxkaXYgY2xhc3M9ImxpLXNjb3JlLWlubmVyIj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXNjb3JlLW51bSI+e3sgcmV2aWV3Lm92ZXJhbGxfc2NvcmUgb3IgMCB9fTwvZGl2PgogICAgICAgICAgPGRpdiBjbGFzcz0ibGktc2NvcmUtbGFiZWwiPlByb2ZpbGUgc2NvcmU8L2Rpdj4KICAgICAgICA8L2Rpdj4KICAgICAgPC9kaXY+CiAgICA8L2hlYWRlcj4KCiAgICB7JSBpZiBzdW1tYXJ5ICV9CiAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQgbGktaGlnaGxpZ2h0Ij4KICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkLWhlYWQiPgogICAgICAgICAgPGgzPkV4ZWN1dGl2ZSBzdW1tYXJ5PC9oMz4KICAgICAgICA8L2Rpdj4KICAgICAgICA8cCBjbGFzcz0ibGktbGVhZCI+e3sgc3VtbWFyeSB8IGNsZWFuX2J1bGxldHMgfX08L3A+CiAgICAgIDwvZGl2PgogICAgeyUgZW5kaWYgJX0KCiAgICA8ZGl2IGNsYXNzPSJsaS1ncmlkIj4KICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZCI+CiAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICAgIDxoMz5TbmFwc2hvdDwvaDM+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0ibGktc3RhdC1ncmlkIj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXN0YXQiPgogICAgICAgICAgICA8c3Bhbj5Xb3Jkczwvc3Bhbj4KICAgICAgICAgICAgPHN0cm9uZz57eyBzdGF0cy53b3JkX2NvdW50IG9yIDAgfX08L3N0cm9uZz4KICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPGRpdiBjbGFzcz0ibGktc3RhdCI+CiAgICAgICAgICAgIDxzcGFuPlNlY3Rpb25zPC9zcGFuPgogICAgICAgICAgICA8c3Ryb25nPnt7IHN0YXRzLnNlY3Rpb25zX3ByZXNlbnQgb3IgMCB9fTwvc3Ryb25nPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1zdGF0Ij4KICAgICAgICAgICAgPHNwYW4+U2tpbGxzPC9zcGFuPgogICAgICAgICAgICA8c3Ryb25nPnt7IHN0YXRzLnNraWxsc19jb3VudCBvciAwIH19PC9zdHJvbmc+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXN0YXQiPgogICAgICAgICAgICA8c3Bhbj5NZXRyaWNzIHVzZWQ8L3NwYW4+CiAgICAgICAgICAgIDxzdHJvbmc+e3sgJ1llcycgaWYgc3RhdHMuaGFzX251bWJlcnMgZWxzZSAnTm8nIH19PC9zdHJvbmc+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICA8L2Rpdj4KICAgICAgPC9kaXY+CgogICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkIj4KICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkLWhlYWQiPgogICAgICAgICAgPGgzPlRvcCBpc3N1ZXM8L2gzPgogICAgICAgIDwvZGl2PgogICAgICAgIHslIGlmIHJldmlldy5pc3N1ZXMgJX0KICAgICAgICAgIDx1bCBjbGFzcz0ibGktbGlzdCI+CiAgICAgICAgICAgIHslIGZvciBpc3N1ZSBpbiByZXZpZXcuaXNzdWVzWzo1XSAlfQogICAgICAgICAgICAgIDxsaT57eyBpc3N1ZSB9fTwvbGk+CiAgICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgICAgPC91bD4KICAgICAgICB7JSBlbHNlICV9CiAgICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+Tm8gaXNzdWVzIGZvdW5kLiBTdHJvbmcgYmFzZWxpbmUuPC9wPgogICAgICAgIHslIGVuZGlmICV9CiAgICAgIDwvZGl2PgoKICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZCI+CiAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICAgIDxoMz5TdHJlbmd0aHM8L2gzPgogICAgICAgIDwvZGl2PgogICAgICAgIHslIGlmIHJldmlldy5zdHJlbmd0aHMgJX0KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXRhZy1ncm91cCI+CiAgICAgICAgICAgIHslIGZvciBpdGVtIGluIHJldmlldy5zdHJlbmd0aHMgJX0KICAgICAgICAgICAgICA8c3BhbiBjbGFzcz0ibGktdGFnIj57eyBpdGVtIH19PC9zcGFuPgogICAgICAgICAgICB7JSBlbmRmb3IgJX0KICAgICAgICAgIDwvZGl2PgogICAgICAgIHslIGVsc2UgJX0KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXRhZy1ncm91cCI+CiAgICAgICAgICAgIHslIGZvciBpdGVtIGluIHRvcF9rZXl3b3Jkc1s6Nl0gJX0KICAgICAgICAgICAgICA8c3BhbiBjbGFzcz0ibGktdGFnIj57eyBpdGVtIH19PC9zcGFuPgogICAgICAgICAgICB7JSBlbmRmb3IgJX0KICAgICAgICAgIDwvZGl2PgogICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgPHAgY2xhc3M9ImxpLW5vdGUiPlJlaW5mb3JjZSBzdHJlbmd0aHMgaW4gaGVhZGxpbmUgYW5kIEFib3V0LjwvcD4KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KCiAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkIj4KICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICA8aDM+U2VjdGlvbiBzY29yZXM8L2gzPgogICAgICA8L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0ibGktYmFycyI+CiAgICAgICAgeyUgZm9yIGxhYmVsLCB2YWx1ZSBpbiBicmVha2Rvd24uaXRlbXMoKSAlfQogICAgICAgICAgPGRpdiBjbGFzcz0ibGktYmFyIj4KICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktYmFyLWxhYmVsIj57eyBsYWJlbCB9fTwvZGl2PgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1iYXItdHJhY2siPjxzcGFuIHN0eWxlPSItLXZhbDoge3sgdmFsdWUgfX07Ij48L3NwYW4+PC9kaXY+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWJhci12YWwiPnt7IHZhbHVlIH19PC9kaXY+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICB7JSBlbmRmb3IgJX0KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KCiAgICA8ZGl2IGNsYXNzPSJsaS10YWJzIj4KICAgICAgPGRpdiBjbGFzcz0ibGktdGFiLWJ1dHRvbnMiPgogICAgICAgIDxidXR0b24gdHlwZT0iYnV0dG9uIiBjbGFzcz0ibGktdGFiLWJ0biBhY3RpdmUiIGRhdGEtbGktdGFiPSJyZXdyaXRlIj5BSSByZXdyaXRlPC9idXR0b24+CiAgICAgICAgPGJ1dHRvbiB0eXBlPSJidXR0b24iIGNsYXNzPSJsaS10YWItYnRuIiBkYXRhLWxpLXRhYj0ia2V5d29yZHMiPktleXdvcmRzPC9idXR0b24+CiAgICAgICAgPGJ1dHRvbiB0eXBlPSJidXR0b24iIGNsYXNzPSJsaS10YWItYnRuIiBkYXRhLWxpLXRhYj0iYWN0aW9uIj5BY3Rpb24gcGxhbjwvYnV0dG9uPgogICAgICAgIDxidXR0b24gdHlwZT0iYnV0dG9uIiBjbGFzcz0ibGktdGFiLWJ0biIgZGF0YS1saS10YWI9ImZvY3VzIj5Gb2N1cyBhcmVhczwvYnV0dG9uPgogICAgICA8L2Rpdj4KCiAgICAgIDxkaXYgY2xhc3M9ImxpLXRhYi1wYW5lbHMiPgogICAgICAgIDxkaXYgY2xhc3M9ImxpLXRhYi1wYW5lbCBhY3RpdmUiIGRhdGEtbGktcGFuZWw9InJld3JpdGUiPgogICAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZCI+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgICAgICAgPGgzPkhlYWRsaW5lIHJld3JpdGU8L2gzPgogICAgICAgICAgICAgIDxidXR0b24gY2xhc3M9ImxpLWNvcHkiIHR5cGU9ImJ1dHRvbiIgZGF0YS1jb3B5LXRhcmdldD0iaGVhZGxpbmUtc3VnZ2VzdGVkIj5Db3B5PC9idXR0b24+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jb21wYXJlIj4KICAgICAgICAgICAgICA8ZGl2PgogICAgICAgICAgICAgICAgPHNwYW4gY2xhc3M9ImxpLW11dGVkIj5DdXJyZW50PC9zcGFuPgogICAgICAgICAgICAgICAgPHA+e3sgaGVhZGxpbmUuZ2V0KCdvcmlnaW5hbCcpIG9yIHJldmlldy5oZWFkbGluZSBvciAnTm90IGRldGVjdGVkJyB9fTwvcD4KICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICA8ZGl2PgogICAgICAgICAgICAgICAgPHNwYW4gY2xhc3M9ImxpLW11dGVkIj5TdWdnZXN0ZWQ8L3NwYW4+CiAgICAgICAgICAgICAgICA8cCBpZD0iaGVhZGxpbmUtc3VnZ2VzdGVkIj57eyBoZWFkbGluZS5nZXQoJ3N1Z2dlc3RlZCcpIG9yIHJldmlldy5oZWFkbGluZSBvciAnJyB9fTwvcD4KICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8L2Rpdj4KCiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkIj4KICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICAgICAgICA8aDM+QWJvdXQgcmV3cml0ZTwvaDM+CiAgICAgICAgICAgICAgPGJ1dHRvbiBjbGFzcz0ibGktY29weSIgdHlwZT0iYnV0dG9uIiBkYXRhLWNvcHktdGFyZ2V0PSJhYm91dC1zdWdnZXN0ZWQiPkNvcHk8L2J1dHRvbj4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIDxkaXYgaWQ9ImFib3V0LXN1Z2dlc3RlZCIgY2xhc3M9ImxpLWNvcHktYmxvY2siPnt7IGFib3V0LmdldCgnc3VnZ2VzdGVkJykgb3IgJycgfX08L2Rpdj4KICAgICAgICAgIDwvZGl2PgoKICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQiPgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkLWhlYWQiPgogICAgICAgICAgICAgIDxoMz5FeHBlcmllbmNlIGJ1bGxldHM8L2gzPgogICAgICAgICAgICAgIDxidXR0b24gY2xhc3M9ImxpLWNvcHkiIHR5cGU9ImJ1dHRvbiIgZGF0YS1jb3B5LXRhcmdldD0iZXhwZXJpZW5jZS1zdWdnZXN0ZWQiPkNvcHk8L2J1dHRvbj4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIDxkaXYgaWQ9ImV4cGVyaWVuY2Utc3VnZ2VzdGVkIiBjbGFzcz0ibGktY29weS1ibG9jayI+CiAgICAgICAgICAgICAgeyUgaWYgZXhwZXJpZW5jZV9idWxsZXRzICV9CiAgICAgICAgICAgICAgICA8dWwgY2xhc3M9ImxpLWxpc3QiPgogICAgICAgICAgICAgICAgICB7JSBmb3IgaXRlbSBpbiBleHBlcmllbmNlX2J1bGxldHMgJX0KICAgICAgICAgICAgICAgICAgICB7JSBpZiBpdGVtIGlzIG1hcHBpbmcgJX0KICAgICAgICAgICAgICAgICAgICAgIDxsaT57eyBpdGVtLmdldCgnc3VnZ2VzdGVkJykgb3IgaXRlbS5nZXQoJ29yaWdpbmFsJykgfX08L2xpPgogICAgICAgICAgICAgICAgICAgIHslIGVsc2UgJX0KICAgICAgICAgICAgICAgICAgICAgIDxsaT57eyBpdGVtIH19PC9saT4KICAgICAgICAgICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgICAgICAgICB7JSBlbmRmb3IgJX0KICAgICAgICAgICAgICAgIDwvdWw+CiAgICAgICAgICAgICAgeyUgZWxzZSAlfQogICAgICAgICAgICAgICAgPHAgY2xhc3M9ImxpLW5vdGUiPk5vIGJ1bGxldCBzdWdnZXN0aW9ucyBnZW5lcmF0ZWQuPC9wPgogICAgICAgICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImxpLXRhYi1wYW5lbCIgZGF0YS1saS1wYW5lbD0ia2V5d29yZHMiPgogICAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZCI+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgICAgICAgPGgzPlRvcCBrZXl3b3JkczwvaDM+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS10YWctZ3JvdXAiPgogICAgICAgICAgICAgIHslIGZvciBrdyBpbiB0b3Bfa2V5d29yZHMgJX0KICAgICAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJsaS10YWciPnt7IGt3IH19PC9zcGFuPgogICAgICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZCI+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgICAgICAgPGgzPk1pc3Npbmcga2V5d29yZHM8L2gzPgogICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgeyUgaWYgbWlzc2luZ19rZXl3b3JkcyAlfQogICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXRhZy1ncm91cCI+CiAgICAgICAgICAgICAgICB7JSBmb3Iga3cgaW4gbWlzc2luZ19rZXl3b3JkcyAlfQogICAgICAgICAgICAgICAgICA8c3BhbiBjbGFzcz0ibGktdGFnIGxpLXRhZy13YXJuIj57eyBrdyB9fTwvc3Bhbj4KICAgICAgICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICB7JSBlbHNlICV9CiAgICAgICAgICAgICAgPHAgY2xhc3M9ImxpLW5vdGUiPk5vIG1pc3Npbmcga2V5d29yZHMgZGV0ZWN0ZWQuPC9wPgogICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkIj4KICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICAgICAgICA8aDM+Um9sZSBrZXl3b3JkczwvaDM+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICB7JSBpZiByb2xlX2tleXdvcmRzICV9CiAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktdGFnLWdyb3VwIj4KICAgICAgICAgICAgICAgIHslIGZvciBrdyBpbiByb2xlX2tleXdvcmRzICV9CiAgICAgICAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJsaS10YWcgbGktdGFnLWFjY2VudCI+e3sga3cgfX08L3NwYW4+CiAgICAgICAgICAgICAgICB7JSBlbmRmb3IgJX0KICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgeyUgZWxzZSAlfQogICAgICAgICAgICAgIDxwIGNsYXNzPSJsaS1ub3RlIj5Sb2xlIGtleXdvcmRzIHdpbGwgYXBwZWFyIGFmdGVyIHRoZSBuZXh0IHNjYW4uPC9wPgogICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImxpLXRhYi1wYW5lbCIgZGF0YS1saS1wYW5lbD0iYWN0aW9uIj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQiPgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkLWhlYWQiPgogICAgICAgICAgICAgIDxoMz5BY3Rpb24gcGxhbjwvaDM+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICB7JSBpZiBhY3Rpb25fcGxhbiAlfQogICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXRpbWVsaW5lIj4KICAgICAgICAgICAgICAgIHslIGZvciBzdGVwIGluIGFjdGlvbl9wbGFuICV9CiAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXRpbWVsaW5lLWl0ZW0iPgogICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXRpbWUiPnt7IHN0ZXAudGltZWZyYW1lIG9yIHN0ZXAuZ2V0KCd0aW1lZnJhbWUnKSB9fTwvZGl2PgogICAgICAgICAgICAgICAgICAgIDxkaXY+CiAgICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS10aW1lbGluZS10aXRsZSI+e3sgc3RlcC5nb2FsIG9yIHN0ZXAuZ2V0KCdnb2FsJykgfX08L2Rpdj4KICAgICAgICAgICAgICAgICAgICAgIHslIGlmIHN0ZXAuYWN0aW9ucyBvciBzdGVwLmdldCgnYWN0aW9ucycpICV9CiAgICAgICAgICAgICAgICAgICAgICAgIDx1bCBjbGFzcz0ibGktbGlzdCI+CiAgICAgICAgICAgICAgICAgICAgICAgICAgeyUgZm9yIGFjdGlvbiBpbiBzdGVwLmFjdGlvbnMgb3Igc3RlcC5nZXQoJ2FjdGlvbnMnKSAlfQogICAgICAgICAgICAgICAgICAgICAgICAgICAgPGxpPnt7IGFjdGlvbiB9fTwvbGk+CiAgICAgICAgICAgICAgICAgICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgICAgICAgICAgICAgICAgIDwvdWw+CiAgICAgICAgICAgICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgICAgICAgICAgICAgeyUgaWYgc3RlcC5kZWxpdmVyYWJsZSBvciBzdGVwLmdldCgnZGVsaXZlcmFibGUnKSAlfQogICAgICAgICAgICAgICAgICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+RGVsaXZlcmFibGU6IHt7IHN0ZXAuZGVsaXZlcmFibGUgb3Igc3RlcC5nZXQoJ2RlbGl2ZXJhYmxlJykgfX08L3A+CiAgICAgICAgICAgICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICB7JSBlbHNlICV9CiAgICAgICAgICAgICAgPHAgY2xhc3M9ImxpLW5vdGUiPkFjdGlvbiBwbGFuIHdpbGwgYXBwZWFyIGFmdGVyIHRoZSBuZXh0IHNjYW4uPC9wPgogICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImxpLXRhYi1wYW5lbCIgZGF0YS1saS1wYW5lbD0iZm9jdXMiPgogICAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZCI+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgICAgICAgPGgzPkZvY3VzIGFyZWFzPC9oMz4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIHslIGlmIGZvY3VzX2l0ZW1zICV9CiAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktZm9jdXMtbGlzdCI+CiAgICAgICAgICAgICAgICB7JSBmb3IgaXRlbSBpbiBmb2N1c19pdGVtcyAlfQogICAgICAgICAgICAgICAgICB7JSBzZXQgc2VjdGlvbl9sYWJlbCA9IGl0ZW0uZ2V0KCdzZWN0aW9uJykgb3IgaXRlbS5nZXQoJ2NhdGVnb3J5Jykgb3IgJ0FyZWEnICV9CiAgICAgICAgICAgICAgICAgIHslIHNldCBwcmlvcml0eSA9IGl0ZW0uZ2V0KCdwcmlvcml0eScpIG9yICdNZWRpdW0nICV9CiAgICAgICAgICAgICAgICAgIHslIHNldCByZWFzb24gPSBpdGVtLmdldCgncmVhc29uJykgb3IgaXRlbS5nZXQoJ25vdGUnKSBvciAnJyAlfQogICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1mb2N1cy1pdGVtIj4KICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1mb2N1cy10aXRsZSI+e3sgc2VjdGlvbl9sYWJlbCB9fTwvZGl2PgogICAgICAgICAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJsaS1waWxsIGxpLXBpbGwte3sgcHJpb3JpdHkgfCBsb3dlciB9fSI+e3sgcHJpb3JpdHkgfX08L3NwYW4+CiAgICAgICAgICAgICAgICAgICAgeyUgaWYgcmVhc29uICV9CiAgICAgICAgICAgICAgICAgICAgICA8cD57eyByZWFzb24gfX08L3A+CiAgICAgICAgICAgICAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgICAgICAgICAgICAgICB7JSBpZiBpdGVtLmdldCgnYWN0aW9ucycpICV9CiAgICAgICAgICAgICAgICAgICAgICA8dWwgY2xhc3M9ImxpLWxpc3QiPgogICAgICAgICAgICAgICAgICAgICAgICB7JSBmb3IgYWN0aW9uIGluIGl0ZW0uZ2V0KCdhY3Rpb25zJykgJX0KICAgICAgICAgICAgICAgICAgICAgICAgICA8bGk+e3sgYWN0aW9uIH19PC9saT4KICAgICAgICAgICAgICAgICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgICAgICAgICAgICAgICA8L3VsPgogICAgICAgICAgICAgICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIHslIGVsc2UgJX0KICAgICAgICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+Tm8gZm9jdXMgYXJlYXMgZmxhZ2dlZC48L3A+CiAgICAgICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgICA8L2Rpdj4KICAgICAgICA8L2Rpdj4KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KCiAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkIj4KICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICA8aDM+TGlua2VkSW4gcG9zdCBhbmFseXRpY3M8L2gzPgogICAgICA8L2Rpdj4KICAgICAgPGZvcm0gbWV0aG9kPSJwb3N0IiBhY3Rpb249Ii9saW5rZWRpbi1yZXZpZXcve3sgcmV2aWV3LmlkIH19L3Bvc3RzLWFuYWx5dGljcyIgZW5jdHlwZT0ibXVsdGlwYXJ0L2Zvcm0tZGF0YSIgY2xhc3M9ImxpLWZvcm0iPgogICAgICAgIDxsYWJlbCBmb3I9InBvc3RzX2ZpbGUiPlVwbG9hZCBwb3N0IGFuYWx5dGljcyAoQ1NWL1hMU1gpPC9sYWJlbD4KICAgICAgICA8aW5wdXQgaWQ9InBvc3RzX2ZpbGUiIG5hbWU9InBvc3RzX2ZpbGUiIHR5cGU9ImZpbGUiIC8+CgogICAgICAgIDxsYWJlbCBmb3I9InBvc3RzX3RleHQiPk9yIHBhc3RlIGFuYWx5dGljcyBKU09OIG9yIHBvc3QgdGV4dCAob25lIHBvc3QgcGVyIGxpbmUpPC9sYWJlbD4KICAgICAgICA8dGV4dGFyZWEgaWQ9InBvc3RzX3RleHQiIG5hbWU9InBvc3RzX3RleHQiIHJvd3M9IjUiIHBsYWNlaG9sZGVyPSdbeyJkYXRlIjoiMjAyNi0wMy0wMSIsImNvbnRlbnQiOiIuLi4iLCJsaWtlcyI6MjAsImNvbW1lbnRzIjozLCJzaGFyZXMiOjEsImltcHJlc3Npb25zIjo4MDB9XSc+PC90ZXh0YXJlYT4KCiAgICAgICAgPGxhYmVsPgogICAgICAgICAgPGlucHV0IHR5cGU9ImNoZWNrYm94IiBuYW1lPSJ1c2VfYWkiIC8+IFVzZSBHZW1pbmkgaW5zaWdodHMKICAgICAgICA8L2xhYmVsPgoKICAgICAgICA8YnV0dG9uIGNsYXNzPSJsaS1idG4iIHR5cGU9InN1Ym1pdCI+QW5hbHl6ZSBwb3N0czwvYnV0dG9uPgogICAgICA8L2Zvcm0+CiAgICAgIHslIGlmIGFuYWx5dGljc19lcnJvciAlfQogICAgICAgIDxkaXYgY2xhc3M9ImxpLWFsZXJ0Ij57eyBhbmFseXRpY3NfZXJyb3IgfX08L2Rpdj4KICAgICAgeyUgZW5kaWYgJX0KCiAgICAgIHslIGlmIGFuYWx5dGljcy50b3RhbF9wb3N0cyAlfQogICAgICAgIDxkaXYgY2xhc3M9ImxpLWRpdmlkZXIiPjwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9ImxpLXN0YXQtZ3JpZCI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1zdGF0Ij4KICAgICAgICAgICAgPHNwYW4+VG90YWwgcG9zdHM8L3NwYW4+CiAgICAgICAgICAgIDxzdHJvbmc+e3sgYW5hbHl0aWNzLnRvdGFsX3Bvc3RzIH19PC9zdHJvbmc+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXN0YXQiPgogICAgICAgICAgICA8c3Bhbj5BdmcgZW5nYWdlbWVudDwvc3Bhbj4KICAgICAgICAgICAgPHN0cm9uZz57eyBhbmFseXRpY3MuYXZnX2VuZ2FnZW1lbnQgfX08L3N0cm9uZz4KICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPGRpdiBjbGFzcz0ibGktc3RhdCI+CiAgICAgICAgICAgIDxzcGFuPkltcHJlc3Npb25zIGF2YWlsYWJsZTwvc3Bhbj4KICAgICAgICAgICAgPHN0cm9uZz57eyAnWWVzJyBpZiBhbmFseXRpY3MuaGFzX2ltcHJlc3Npb25zIGVsc2UgJ05vJyB9fTwvc3Ryb25nPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImxpLWdyaWQiPgogICAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZCI+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgICAgICAgPGgzPldoYXQgd29ya2VkPC9oMz4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIHslIGlmIGFuYWx5dGljcy53aGF0X3dvcmtlZCAlfQogICAgICAgICAgICAgIDx1bCBjbGFzcz0ibGktbGlzdCI+CiAgICAgICAgICAgICAgICB7JSBmb3IgaXRlbSBpbiBhbmFseXRpY3Mud2hhdF93b3JrZWQgJX0KICAgICAgICAgICAgICAgICAgPGxpPnt7IGl0ZW0gfX08L2xpPgogICAgICAgICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgICAgICAgPC91bD4KICAgICAgICAgICAgeyUgZWxzZSAlfQogICAgICAgICAgICAgIDxwIGNsYXNzPSJsaS1ub3RlIj5Ob3QgZW5vdWdoIHNpZ25hbCB5ZXQuPC9wPgogICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkIj4KICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICAgICAgICA8aDM+V2hhdCBkaWRu4oCZdCB3b3JrPC9oMz4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgIHslIGlmIGFuYWx5dGljcy53aGF0X2RpZG50ICV9CiAgICAgICAgICAgICAgPHVsIGNsYXNzPSJsaS1saXN0Ij4KICAgICAgICAgICAgICAgIHslIGZvciBpdGVtIGluIGFuYWx5dGljcy53aGF0X2RpZG50ICV9CiAgICAgICAgICAgICAgICAgIDxsaT57eyBpdGVtIH19PC9saT4KICAgICAgICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgICAgICAgIDwvdWw+CiAgICAgICAgICAgIHslIGVsc2UgJX0KICAgICAgICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+Tm90IGVub3VnaCBzaWduYWwgeWV0LjwvcD4KICAgICAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgICAgIDwvZGl2PgogICAgICAgIDwvZGl2PgoKICAgICAgICA8ZGl2IGNsYXNzPSJsaS1ncmlkIj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQiPgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkLWhlYWQiPgogICAgICAgICAgICAgIDxoMz5Ub3AgcG9zdHM8L2gzPgogICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgeyUgaWYgYW5hbHl0aWNzLnRvcF9wb3N0cyAlfQogICAgICAgICAgICAgIDx1bCBjbGFzcz0ibGktbGlzdCI+CiAgICAgICAgICAgICAgICB7JSBmb3IgcG9zdCBpbiBhbmFseXRpY3MudG9wX3Bvc3RzICV9CiAgICAgICAgICAgICAgICAgIDxsaT4KICAgICAgICAgICAgICAgICAgICB7eyBwb3N0LmNvbnRlbnRbOjE2MF0gfX17JSBpZiBwb3N0LmNvbnRlbnR8bGVuZ3RoID4gMTYwICV9Li4ueyUgZW5kaWYgJX0KICAgICAgICAgICAgICAgICAgICA8c3BhbiBjbGFzcz0ibGktbm90ZSI+wrcge3sgcG9zdC5saWtlcyB9fSBsaWtlcyDCtyB7eyBwb3N0LmNvbW1lbnRzIH19IGNvbW1lbnRzIMK3IHt7IHBvc3Quc2hhcmVzIH19IHNoYXJlczwvc3Bhbj4KICAgICAgICAgICAgICAgICAgPC9saT4KICAgICAgICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgICAgICAgIDwvdWw+CiAgICAgICAgICAgIHslIGVsc2UgJX0KICAgICAgICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+Tm8gdG9wIHBvc3RzIHlldC48L3A+CiAgICAgICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQiPgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkLWhlYWQiPgogICAgICAgICAgICAgIDxoMz5Mb3ctcGVyZm9ybWluZyBwb3N0czwvaDM+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICB7JSBpZiBhbmFseXRpY3MuYm90dG9tX3Bvc3RzICV9CiAgICAgICAgICAgICAgPHVsIGNsYXNzPSJsaS1saXN0Ij4KICAgICAgICAgICAgICAgIHslIGZvciBwb3N0IGluIGFuYWx5dGljcy5ib3R0b21fcG9zdHMgJX0KICAgICAgICAgICAgICAgICAgPGxpPgogICAgICAgICAgICAgICAgICAgIHt7IHBvc3QuY29udGVudFs6MTYwXSB9fXslIGlmIHBvc3QuY29udGVudHxsZW5ndGggPiAxNjAgJX0uLi57JSBlbmRpZiAlfQogICAgICAgICAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJsaS1ub3RlIj7CtyB7eyBwb3N0Lmxpa2VzIH19IGxpa2VzIMK3IHt7IHBvc3QuY29tbWVudHMgfX0gY29tbWVudHMgwrcge3sgcG9zdC5zaGFyZXMgfX0gc2hhcmVzPC9zcGFuPgogICAgICAgICAgICAgICAgICA8L2xpPgogICAgICAgICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgICAgICAgPC91bD4KICAgICAgICAgICAgeyUgZWxzZSAlfQogICAgICAgICAgICAgIDxwIGNsYXNzPSJsaS1ub3RlIj5ObyBsb3ctcGVyZm9ybWluZyBwb3N0cyB5ZXQuPC9wPgogICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIHslIGlmIGFuYWx5dGljcy5haV9pbnNpZ2h0cyAlfQogICAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZCI+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgICAgICAgPGgzPkFJIGluc2lnaHRzPC9oMz4KICAgICAgICAgICAgICA8YnV0dG9uIGNsYXNzPSJsaS1jb3B5IiB0eXBlPSJidXR0b24iIGRhdGEtY29weS10YXJnZXQ9ImxpLWFpLWluc2lnaHRzIj5Db3B5PC9idXR0b24+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICA8ZGl2IGlkPSJsaS1haS1pbnNpZ2h0cyIgY2xhc3M9ImxpLWNvcHktYmxvY2siPnt7IGFuYWx5dGljcy5haV9pbnNpZ2h0cyB9fTwvZGl2PgogICAgICAgICAgPC9kaXY+CiAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgeyUgZW5kaWYgJX0KICAgIDwvZGl2PgoKICAgIDxkZXRhaWxzIGNsYXNzPSJsaS1jYXJkIGxpLXJhdyI+CiAgICAgIDxzdW1tYXJ5PlZpZXcgZXh0cmFjdGVkIHByb2ZpbGUgdGV4dDwvc3VtbWFyeT4KICAgICAgPHByZT57eyByZXZpZXcudGV4dCBvciAnJyB9fTwvcHJlPgogICAgPC9kZXRhaWxzPgogIDwvZGl2Pgp7JSBlbmRibG9jayAlfQp7JSBibG9jayBzY3JpcHRzICV9CiAgPHNjcmlwdCBzcmM9Int7IHVybF9mb3IoJ3N0YXRpYycsIGZpbGVuYW1lPSdsaW5rZWRpbi5qcycpIH19Ij48L3NjcmlwdD4KeyUgZW5kYmxvY2sgJX0NCg==","resume_review.html":"eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBoZWFkICV9CiAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJ7eyB1cmxfZm9yKCdzdGF0aWMnLCBmaWxlbmFtZT0nbGlua2VkaW4uY3NzJykgfX0iIC8+CnslIGVuZGJsb2NrICV9CnslIGJsb2NrIGNvbnRlbnQgJX0KICB7JSBzZXQgbGF0ZXN0ID0gbGF0ZXN0X2Z1bGwgaWYgbGF0ZXN0X2Z1bGwgaXMgZGVmaW5lZCBhbmQgbGF0ZXN0X2Z1bGwgZWxzZSAoaGlzdG9yeVswXSBpZiBoaXN0b3J5IGFuZCBoaXN0b3J5fGxlbmd0aCBlbHNlIE5vbmUpICV9CiAgeyUgc2V0IHByZXZpb3VzID0gaGlzdG9yeVsxXSBpZiBoaXN0b3J5IGFuZCBoaXN0b3J5fGxlbmd0aCA+IDEgZWxzZSBOb25lICV9CiAgeyUgc2V0IGRlbHRhID0gKGxhdGVzdC5vdmVyYWxsX3Njb3JlIHwgaW50KSAtIChwcmV2aW91cy5vdmVyYWxsX3Njb3JlIHwgaW50KSBpZiBsYXRlc3QgYW5kIHByZXZpb3VzIGVsc2UgTm9uZSAlfQogIHslIHNldCBsYXRlc3Rfcm9sZSA9IGxhdGVzdC5wcmVkaWN0ZWRfcm9sZV9mYW1pbHkgaWYgbGF0ZXN0IGFuZCBsYXRlc3QucHJlZGljdGVkX3JvbGVfZmFtaWx5IGlzIGRlZmluZWQgZWxzZSAnJyAlfQogIHslIHNldCBsYXRlc3RfbGV2ZWwgPSBsYXRlc3QuY2FuZGlkYXRlX2xldmVsIGlmIGxhdGVzdCBhbmQgbGF0ZXN0LmNhbmRpZGF0ZV9sZXZlbCBpcyBkZWZpbmVkIGVsc2UgJycgJX0KICB7JSBzZXQgbGF0ZXN0X2F0cyA9IGxhdGVzdC5hdHNfcmVhZGluZXNzX3Njb3JlIGlmIGxhdGVzdCBhbmQgbGF0ZXN0LmF0c19yZWFkaW5lc3Nfc2NvcmUgaXMgZGVmaW5lZCBlbHNlIChsYXRlc3Qub3ZlcmFsbF9zY29yZSBpZiBsYXRlc3QgZWxzZSAwKSAlfQogIHslIHNldCBsYXRlc3RfbWlzc2luZyA9IGxhdGVzdC5taXNzaW5nX3NraWxscyBpZiBsYXRlc3QgYW5kIGxhdGVzdC5taXNzaW5nX3NraWxscyBpcyBkZWZpbmVkIGFuZCBsYXRlc3QubWlzc2luZ19za2lsbHMgZWxzZSBbXSAlfQogIHslIHNldCBsYXRlc3RfY291cnNlcyA9IGxhdGVzdC5yZWNvbW1lbmRlZF9jb3Vyc2VzIGlmIGxhdGVzdCBhbmQgbGF0ZXN0LnJlY29tbWVuZGVkX2NvdXJzZXMgaXMgZGVmaW5lZCBhbmQgbGF0ZXN0LnJlY29tbWVuZGVkX2NvdXJzZXMgZWxzZSBbXSAlfQogIHslIHNldCB0b3BfZml4ZXMgPSB0b3BfZml4ZXMgaWYgdG9wX2ZpeGVzIGlzIGRlZmluZWQgZWxzZSBbXSAlfQogIHslIHNldCBzZWN0aW9uX2NhcmRzID0gc2VjdGlvbl9jYXJkcyBpZiBzZWN0aW9uX2NhcmRzIGlzIGRlZmluZWQgZWxzZSBbXSAlfQogIHslIHNldCBhdHNfc25hcHNob3QgPSBhdHNfc25hcHNob3QgaWYgYXRzX3NuYXBzaG90IGlzIGRlZmluZWQgZWxzZSB7fSAlfQoKICA8ZGl2IGNsYXNzPSJsaS1zaGVsbCBsaS1wYWdlIGxpLXJlc3VtZSI+CiAgICA8aGVhZGVyIGNsYXNzPSJsaS1oZXJvIj4KICAgICAgPGRpdj4KICAgICAgICA8ZGl2IGNsYXNzPSJsaS1raWNrZXIiPlJlc3VtZSBJbnRlbGxpZ2VuY2U8L2Rpdj4KICAgICAgICA8aDE+UmVzdW1lIFJldmlldyBEYXNoYm9hcmQ8L2gxPgogICAgICAgIDxwIGNsYXNzPSJsaS1zdWJ0aXRsZSI+VXBsb2FkIG9yIHBhc3RlIHlvdXIgcmVzdW1lIGZvciBBSS1wb3dlcmVkIGFuYWx5c2lzIHdpdGggc3Ryb25nZXIgc2VjdGlvbiB1bmRlcnN0YW5kaW5nIGFuZCBjbGVhbmVyIFBERiBwYXJzaW5nLjwvcD4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImxpLWhlcm8tbWV0YSI+CiAgICAgICAgPHNwYW4gY2xhc3M9ImxpLXBpbGwge3sgJ29uJyBpZiBnZW1pbmlfZW5hYmxlZCBlbHNlICdvZmYnIH19Ij4KICAgICAgICAgIHt7IChhaV9wcm92aWRlcl9sYWJlbCB+ICcgY29ubmVjdGVkJykgaWYgZ2VtaW5pX2VuYWJsZWQgZWxzZSAnQUkgbm90IGNvbm5lY3RlZCcgfX0KICAgICAgICA8L3NwYW4+CiAgICAgICAgeyUgaWYgbGF0ZXN0ICV9CiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1zY29yZSIgc3R5bGU9Ii0tc2NvcmU6IHt7IGxhdGVzdC5vdmVyYWxsX3Njb3JlIG9yIDAgfX07Ij4KICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktc2NvcmUtaW5uZXIiPgogICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXNjb3JlLW51bSI+e3sgbGF0ZXN0Lm92ZXJhbGxfc2NvcmUgb3IgMCB9fTwvZGl2PgogICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXNjb3JlLWxhYmVsIj5MYXRlc3Qgc2NvcmU8L2Rpdj4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICB7JSBlbmRpZiAlfQogICAgICA8L2Rpdj4KICAgIDwvaGVhZGVyPgoKICAgIHslIGlmIGVycm9yICV9CiAgICAgIDxkaXYgY2xhc3M9ImxpLWFsZXJ0Ij57eyBlcnJvciB9fTwvZGl2PgogICAgeyUgZW5kaWYgJX0KCiAgICA8ZGl2IGNsYXNzPSJsaS1ncmlkIGxpLWRhc2hib2FyZCI+CiAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQgbGktb3V0Y29tZSI+CiAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICAgIDxoMz5PdXRjb21lIGRhc2hib2FyZDwvaDM+CiAgICAgICAgICA8c3BhbiBjbGFzcz0ibGktdGFnIj5EZWZhdWx0IHZpZXc8L3NwYW4+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0ibGktb3V0Y29tZS1yb3ciPgogICAgICAgICAgPGRpdiBjbGFzcz0ibGktb3V0Y29tZS1zY29yZSI+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXNjb3JlIiBzdHlsZT0iLS1zY29yZToge3sgbGF0ZXN0Lm92ZXJhbGxfc2NvcmUgb3IgMCB9fTsiPgogICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXNjb3JlLWlubmVyIj4KICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXNjb3JlLW51bSI+e3sgbGF0ZXN0Lm92ZXJhbGxfc2NvcmUgb3IgMCB9fTwvZGl2PgogICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktc2NvcmUtbGFiZWwiPlJlc3VtZSBzY29yZTwvZGl2PgogICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktb3V0Y29tZS1tZXRhIj4KICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1vdXRjb21lLWtwaSI+CiAgICAgICAgICAgICAgICA8c3Bhbj5BVFMgcmVhZHk8L3NwYW4+CiAgICAgICAgICAgICAgICA8c3Ryb25nPnt7IGxhdGVzdF9hdHMgb3IgMCB9fSU8L3N0cm9uZz4KICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1vdXRjb21lLWtwaSI+CiAgICAgICAgICAgICAgICA8c3Bhbj5MZXZlbCBmaXQ8L3NwYW4+CiAgICAgICAgICAgICAgICA8c3Ryb25nPnt7IGxhdGVzdF9sZXZlbCBvciAnTm90IGluZmVycmVkJyB9fTwvc3Ryb25nPgogICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICAgIHslIGlmIGRlbHRhIGlzIG5vdCBub25lICV9CiAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1vdXRjb21lLWtwaSI+CiAgICAgICAgICAgICAgICAgIDxzcGFuPkNoYW5nZTwvc3Bhbj4KICAgICAgICAgICAgICAgICAgPHN0cm9uZz57eyAnKycgaWYgZGVsdGEgPj0gMCBlbHNlICcnIH19e3sgZGVsdGEgfX08L3N0cm9uZz4KICAgICAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1vdXRjb21lLWFjdGlvbnMiPgogICAgICAgICAgICA8bGFiZWwgZm9yPSJ0YXJnZXRfcm9sZSIgY2xhc3M9ImxpLW11dGVkIj5UYXJnZXQgcm9sZTwvbGFiZWw+CiAgICAgICAgICAgIDxzZWxlY3QgaWQ9InRhcmdldF9yb2xlIiBjbGFzcz0ibGktc2VsZWN0Ij4KICAgICAgICAgICAgICA8b3B0aW9uIHZhbHVlPSJwbSIge3sgJ3NlbGVjdGVkJyBpZiBsYXRlc3Rfcm9sZSA9PSAnUHJvZHVjdCBNYW5hZ2VtZW50JyBlbHNlICcnIH19PlByb2R1Y3QgTWFuYWdlcjwvb3B0aW9uPgogICAgICAgICAgICAgIDxvcHRpb24gdmFsdWU9Im1hcmtldGluZyIge3sgJ3NlbGVjdGVkJyBpZiBsYXRlc3Rfcm9sZSA9PSAnTWFya2V0aW5nIC8gR3Jvd3RoJyBlbHNlICcnIH19Pk1hcmtldGluZzwvb3B0aW9uPgogICAgICAgICAgICAgIDxvcHRpb24gdmFsdWU9ImFuYWx5dGljcyIge3sgJ3NlbGVjdGVkJyBpZiBsYXRlc3Rfcm9sZSA9PSAnRGF0YSAvIEFuYWx5dGljcycgZWxzZSAnJyB9fT5BbmFseXN0PC9vcHRpb24+CiAgICAgICAgICAgICAgPG9wdGlvbiB2YWx1ZT0iZW5naW5lZXJpbmciIHt7ICdzZWxlY3RlZCcgaWYgbGF0ZXN0X3JvbGUgPT0gJ1NvZnR3YXJlIEVuZ2luZWVyaW5nJyBlbHNlICcnIH19PlNvZnR3YXJlPC9vcHRpb24+CiAgICAgICAgICAgICAgPG9wdGlvbiB2YWx1ZT0iZGVzaWduIiB7eyAnc2VsZWN0ZWQnIGlmIGxhdGVzdF9yb2xlID09ICdEZXNpZ24gLyBVWCcgZWxzZSAnJyB9fT5EZXNpZ248L29wdGlvbj4KICAgICAgICAgICAgICA8b3B0aW9uIHZhbHVlPSJvcHMiIHt7ICdzZWxlY3RlZCcgaWYgbGF0ZXN0X3JvbGUgPT0gJ09wZXJhdGlvbnMgLyBQcm9ncmFtIE1hbmFnZW1lbnQnIGVsc2UgJycgfX0+T3BlcmF0aW9uczwvb3B0aW9uPgogICAgICAgICAgICA8L3NlbGVjdD4KICAgICAgICAgICAgPHAgY2xhc3M9ImxpLW5vdGUiPlNlbGVjdCBhIHRhcmdldCByb2xlIHRvIHN0ZWVyIGZ1dHVyZSByZWNvbW1lbmRhdGlvbnMuPC9wPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CgogICAgICAgIDxkaXYgY2xhc3M9ImxpLWRpdmlkZXIiPjwvZGl2PgoKICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkLWhlYWQiPgogICAgICAgICAgPGgzPkZpeCB0aGVzZSAzIHRoaW5ncyBmaXJzdDwvaDM+CiAgICAgICAgICA8YnV0dG9uIGNsYXNzPSJsaS1idG4gbGktYnRuLXNlY29uZGFyeSIgdHlwZT0iYnV0dG9uIiBpZD0iZml4QWxsQnRuIiBkYXRhLWxhdGVzdC1pZD0ie3sgbGF0ZXN0LmlkIGlmIGxhdGVzdCBlbHNlICcnIH19IiB7JSBpZiBub3QgbGF0ZXN0ICV9ZGlzYWJsZWR7JSBlbmRpZiAlfT5GaXggQWxsIGluIDEgQ2xpY2s8L2J1dHRvbj4KICAgICAgICA8L2Rpdj4KICAgICAgICB7JSBpZiB0b3BfZml4ZXMgJX0KICAgICAgICAgIDxvbCBjbGFzcz0ibGktZml4LWxpc3QiPgogICAgICAgICAgICB7JSBmb3IgaXRlbSBpbiB0b3BfZml4ZXMgJX0KICAgICAgICAgICAgICA8bGk+e3sgaXRlbSB9fTwvbGk+CiAgICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgICAgPC9vbD4KICAgICAgICB7JSBlbHNlICV9CiAgICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+UnVuIGEgcmV2aWV3IHRvIHNlZSBwcmlvcml0aXplZCBmaXhlcy48L3A+CiAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgPC9kaXY+CgogICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkIGxpLXVwbG9hZCI+CiAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICAgIDxoMz5VcGxvYWQgcmVzdW1lPC9oMz4KICAgICAgICAgIDxzcGFuIGNsYXNzPSJsaS10YWciPkFJIHJldmlldzwvc3Bhbj4KICAgICAgICA8L2Rpdj4KICAgICAgICA8Zm9ybSBtZXRob2Q9InBvc3QiIGVuY3R5cGU9Im11bHRpcGFydC9mb3JtLWRhdGEiIGNsYXNzPSJsaS1mb3JtIj4KICAgICAgICAgIDxsYWJlbCBmb3I9InJlc3VtZV90ZXh0Ij5QYXN0ZSByZXN1bWUgdGV4dDwvbGFiZWw+CiAgICAgICAgICA8dGV4dGFyZWEgaWQ9InJlc3VtZV90ZXh0IiBuYW1lPSJyZXN1bWVfdGV4dCIgcm93cz0iOCIgcGxhY2Vob2xkZXI9IlBhc3RlIHJlc3VtZSB0ZXh0IGhlcmUuLi4iPjwvdGV4dGFyZWE+CiAgICAgICAgICA8bGFiZWwgZm9yPSJyZXN1bWVfZmlsZSI+T3IgdXBsb2FkIGEgZmlsZSAoLnR4dCwgLnBkZiwgLmRvY3gpPC9sYWJlbD4KICAgICAgICAgIDxpbnB1dCBpZD0icmVzdW1lX2ZpbGUiIG5hbWU9InJlc3VtZV9maWxlIiB0eXBlPSJmaWxlIiAvPgogICAgICAgICAgPGJ1dHRvbiBjbGFzcz0ibGktYnRuIiB0eXBlPSJzdWJtaXQiPkFuYWx5emUgUmVzdW1lPC9idXR0b24+CiAgICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+VXBsb2FkIHRvIGdlbmVyYXRlIHNjb3JlcywgZml4ZXMsIGFuZCByZWNvbW1lbmRhdGlvbnMuPC9wPgogICAgICAgIDwvZm9ybT4KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KCiAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkIGxpLXNlY3Rpb24tY2FyZHMiPgogICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkLWhlYWQiPgogICAgICAgIDxoMz5TZWN0aW9uIHNjb3JlczwvaDM+CiAgICAgICAgeyUgaWYgbGF0ZXN0ICV9CiAgICAgICAgICA8YSBjbGFzcz0ibGktbGluayIgaHJlZj0iL3Jlc3VtZS1yZXZpZXcve3sgbGF0ZXN0LmlkIH19P2Zyb209ZGFzaGJvYXJkIj5WaWV3IGRldGFpbGVkIHJldmlldzwvYT4KICAgICAgICB7JSBlbmRpZiAlfQogICAgICA8L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0ibGktc2VjdGlvbi1ncmlkIj4KICAgICAgICB7JSBmb3IgY2FyZCBpbiBzZWN0aW9uX2NhcmRzICV9CiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1zZWN0aW9uLWNhcmQtY29tcGFjdCI+CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXNlY3Rpb24tY2FyZC10aXRsZSI+e3sgY2FyZC5sYWJlbCB9fTwvZGl2PgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1zZWN0aW9uLWNhcmQtc2NvcmUiPnt7IGNhcmQuc2NvcmUgfX0vMTA8L2Rpdj4KICAgICAgICAgICAgPHNwYW4gY2xhc3M9ImxpLWJhZGdlIHt7ICdsaS1iYWRnZS1nb29kJyBpZiBjYXJkLnN0YXR1cyA9PSAnZ29vZCcgZWxzZSAoJ2xpLWJhZGdlLXdhcm4nIGlmIGNhcmQuc3RhdHVzID09ICd3YXJuJyBlbHNlICdsaS1iYWRnZS1iYWQnKSB9fSI+CiAgICAgICAgICAgICAge3sgJ0dvb2QnIGlmIGNhcmQuc3RhdHVzID09ICdnb29kJyBlbHNlICgnSW1wcm92ZScgaWYgY2FyZC5zdGF0dXMgPT0gJ3dhcm4nIGVsc2UgJ0NyaXRpY2FsJykgfX0KICAgICAgICAgICAgPC9zcGFuPgogICAgICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+e3sgY2FyZC5pbnNpZ2h0IH19PC9wPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgeyUgZWxzZSAlfQogICAgICAgICAgPHAgY2xhc3M9ImxpLW5vdGUiPk5vIHNlY3Rpb24gc2NvcmVzIGF2YWlsYWJsZSB5ZXQuPC9wPgogICAgICAgIHslIGVuZGZvciAlfQogICAgICA8L2Rpdj4KICAgICAgeyUgaWYgbGF0ZXN0ICV9CiAgICAgICAgPGRpdiBjbGFzcz0ibGktZGFzaGJvYXJkLWN0YSI+CiAgICAgICAgICA8YSBjbGFzcz0ibGktYnRuIiBocmVmPSIvcmVzdW1lLXJldmlldy97eyBsYXRlc3QuaWQgfX0iPlZpZXcgRGV0YWlsZWQgUmV2aWV3PC9hPgogICAgICAgIDwvZGl2PgogICAgICB7JSBlbmRpZiAlfQogICAgPC9kaXY+CgogICAgeyUgaWYgYXRzX3NuYXBzaG90ICV9CiAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQgbGktYXRzIj4KICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkLWhlYWQiPgogICAgICAgICAgPGgzPkFUUyBzaW11bGF0aW9uPC9oMz4KICAgICAgICAgIDxzcGFuIGNsYXNzPSJsaS10YWciPlJlY3J1aXRlciB2aWV3PC9zcGFuPgogICAgICAgIDwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9ImxpLXN0YXQtZ3JpZCI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1zdGF0Ij4KICAgICAgICAgICAgPHNwYW4+TmFtZTwvc3Bhbj4KICAgICAgICAgICAgPHN0cm9uZz57eyBhdHNfc25hcHNob3QubmFtZSBvciAnTm90IGRldGVjdGVkJyB9fTwvc3Ryb25nPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1zdGF0Ij4KICAgICAgICAgICAgPHNwYW4+RW1haWw8L3NwYW4+CiAgICAgICAgICAgIDxzdHJvbmc+e3sgJ0RldGVjdGVkJyBpZiBhdHNfc25hcHNob3QuZW1haWxfZm91bmQgZWxzZSAnTWlzc2luZycgfX08L3N0cm9uZz4KICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPGRpdiBjbGFzcz0ibGktc3RhdCI+CiAgICAgICAgICAgIDxzcGFuPlBob25lPC9zcGFuPgogICAgICAgICAgICA8c3Ryb25nPnt7ICdEZXRlY3RlZCcgaWYgYXRzX3NuYXBzaG90LnBob25lX2ZvdW5kIGVsc2UgJ01pc3NpbmcnIH19PC9zdHJvbmc+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXN0YXQiPgogICAgICAgICAgICA8c3Bhbj5Ta2lsbHMgZGV0ZWN0ZWQ8L3NwYW4+CiAgICAgICAgICAgIDxzdHJvbmc+e3sgYXRzX3NuYXBzaG90LnNraWxsc19kZXRlY3RlZCBvciAwIH19L3t7IGF0c19zbmFwc2hvdC5za2lsbHNfdGFyZ2V0IG9yIDAgfX08L3N0cm9uZz4KICAgICAgICAgIDwvZGl2PgogICAgICAgIDwvZGl2PgogICAgICA8L2Rpdj4KICAgIHslIGVuZGlmICV9CgogICAgeyUgc2V0IHRyZW5kID0gdHJlbmRfaGlzdG9yeSBpZiB0cmVuZF9oaXN0b3J5IGlzIGRlZmluZWQgZWxzZSBoaXN0b3J5ICV9CiAgICB7JSBpZiB0cmVuZCBhbmQgdHJlbmR8bGVuZ3RoICV9CiAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQgbGktY2hhcnQgbGktcHJvZ3Jlc3MiPgogICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgICA8aDM+UHJvZ3Jlc3M8L2gzPgogICAgICAgICAgPHNwYW4gY2xhc3M9ImxpLXRhZyI+U2NvcmUgb3ZlciB0aW1lPC9zcGFuPgogICAgICAgIDwvZGl2PgogICAgICAgIDxjYW52YXMgaWQ9InJlc3VtZVNjb3JlVHJlbmQiIGhlaWdodD0iMTQwIiBkYXRhLWhpc3Rvcnk9J3t7IHRyZW5kIHwgdG9qc29uIH19Jz48L2NhbnZhcz4KICAgICAgPC9kaXY+CiAgICB7JSBlbmRpZiAlfQoKICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQgbGktaGlzdG9yeSI+CiAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgPGgzPlBhc3QgcmV2aWV3czwvaDM+CiAgICAgICAgPGRpdiBjbGFzcz0icGFnZXIiPgogICAgICAgICAgeyUgaWYgdmlld19hbGwgJX0KICAgICAgICAgICAgPGEgY2xhc3M9ImJ0biBidG4tZ2hvc3QiIGhyZWY9Ii9yZXN1bWUtcmV2aWV3P3BhZ2U9MSI+UGFnaW5hdGU8L2E+CiAgICAgICAgICB7JSBlbHNlICV9CiAgICAgICAgICAgIDxhIGNsYXNzPSJidG4gYnRuLWdob3N0IiBocmVmPSIvcmVzdW1lLXJldmlldz92aWV3PWFsbCI+RXhwYW5kIGFsbDwvYT4KICAgICAgICAgICAgeyUgaWYgcGFnZSA+IDEgJX0KICAgICAgICAgICAgICA8YSBjbGFzcz0iYnRuIGJ0bi1naG9zdCIgaHJlZj0iL3Jlc3VtZS1yZXZpZXc/cGFnZT17eyBwYWdlIC0gMSB9fSI+UHJldjwvYT4KICAgICAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgICAgICAgeyUgaWYgcGFnZSA8IHRvdGFsX3BhZ2VzICV9CiAgICAgICAgICAgICAgPGEgY2xhc3M9ImJ0biBidG4tZ2hvc3QiIGhyZWY9Ii9yZXN1bWUtcmV2aWV3P3BhZ2U9e3sgcGFnZSArIDEgfX0iPk5leHQ8L2E+CiAgICAgICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJsaS1ub3RlIj5QYWdlIHt7IHBhZ2UgfX0gLyB7eyB0b3RhbF9wYWdlcyB9fTwvc3Bhbj4KICAgICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgPC9kaXY+CiAgICAgIDwvZGl2PgogICAgICB7JSBpZiBoaXN0b3J5IGFuZCBoaXN0b3J5fGxlbmd0aCAlfQogICAgICAgIDxwIGNsYXNzPSJsaS1ub3RlIj5TaG93aW5nIHt7IHBhZ2VfY291bnQgfX0gb2Yge3sgdG90YWxfY291bnQgfX0gcmV2aWV3cy48L3A+CiAgICAgICAgPGRpdiBjbGFzcz0ibGktdGFibGUiPgogICAgICAgICAgPGRpdiBjbGFzcz0ibGktdGFibGUtaGVhZCI+CiAgICAgICAgICAgIDxzcGFuPlRpbWVzdGFtcDwvc3Bhbj4KICAgICAgICAgICAgPHNwYW4+U2NvcmU8L3NwYW4+CiAgICAgICAgICAgIDxzcGFuPklzc3Vlczwvc3Bhbj4KICAgICAgICAgICAgPHNwYW4+PC9zcGFuPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICB7JSBmb3IgaXRlbSBpbiBoaXN0b3J5ICV9CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXRhYmxlLXJvdyI+CiAgICAgICAgICAgICAgPHNwYW4+e3sgaXRlbS50aW1lc3RhbXAgfX08L3NwYW4+CiAgICAgICAgICAgICAgPHNwYW4gY2xhc3M9ImxpLW1vbm8iPnt7IGl0ZW0ub3ZlcmFsbF9zY29yZSB9fTwvc3Bhbj4KICAgICAgICAgICAgICA8c3BhbiBjbGFzcz0ibGktbW9ubyI+e3sgaXRlbS5pc3N1ZXNfY291bnQgfX08L3NwYW4+CiAgICAgICAgICAgICAgPGEgY2xhc3M9ImxpLWxpbmsiIGhyZWY9Ii9yZXN1bWUtcmV2aWV3L3t7IGl0ZW0uaWQgfX0iPlZpZXc8L2E+CiAgICAgICAgICAgIDwvZGl2PgogICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgPC9kaXY+CiAgICAgIHslIGVsc2UgJX0KICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+Tm8gcmV2aWV3cyB5ZXQuPC9wPgogICAgICB7JSBlbmRpZiAlfQogICAgPC9kaXY+CiAgPC9kaXY+CnslIGVuZGJsb2NrICV9CnslIGJsb2NrIHNjcmlwdHMgJX0KICA8c2NyaXB0IHNyYz0ie3sgdXJsX2Zvcignc3RhdGljJywgZmlsZW5hbWU9J2xpbmtlZGluLmpzJykgfX0iPjwvc2NyaXB0Pgp7JSBlbmRibG9jayAlfQo=","resume_review_detail.html":"eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBoZWFkICV9CiAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJ7eyB1cmxfZm9yKCdzdGF0aWMnLCBmaWxlbmFtZT0nbGlua2VkaW4uY3NzJykgfX0iIC8+CnslIGVuZGJsb2NrICV9CnslIGJsb2NrIGNvbnRlbnQgJX0KICB7JSBzZXQgYnJlYWtkb3duID0gcmV2aWV3LmJyZWFrZG93biBvciB7fSAlfQogIHslIHNldCBpc3N1ZXMgPSByZXZpZXcuaXNzdWVzIG9yIFtdICV9CiAgeyUgc2V0IGxpbmVfcmV2aWV3cyA9IHJldmlldy5saW5lX3Jldmlld3Mgb3IgW10gJX0KICB7JSBzZXQgaW1wcm92ZWRfYnVsbGV0cyA9IHJldmlldy5pbXByb3ZlZF9idWxsZXRzIG9yIFtdICV9CiAgeyUgc2V0IHNlY3Rpb25fcmVwb3J0ID0gc2VjdGlvbl9yZXBvcnQgb3IgW10gJX0KICB7JSBzZXQgYW5hbHlzaXNfZW5naW5lID0gcmV2aWV3LmFuYWx5c2lzX2VuZ2luZSBvciAncnVsZV9iYXNlZCcgJX0KICB7JSBzZXQgZml4X2FsbCA9IGZpeF9hbGwgaWYgZml4X2FsbCBpcyBkZWZpbmVkIGVsc2UgZmFsc2UgJX0KICB7JSBzZXQgcmVjcnVpdGVyX3ZpZXcgPSByZWNydWl0ZXJfdmlldyBpZiByZWNydWl0ZXJfdmlldyBpcyBkZWZpbmVkIGVsc2UgW10gJX0KICB7JSBzZXQgYXRzX3NuYXBzaG90ID0gYXRzX3NuYXBzaG90IGlmIGF0c19zbmFwc2hvdCBpcyBkZWZpbmVkIGVsc2Uge30gJX0KICB7JSBzZXQgYXRzX3JlYWRpbmVzc19zY29yZSA9IHJldmlldy5hdHNfcmVhZGluZXNzX3Njb3JlIGlmIHJldmlldy5hdHNfcmVhZGluZXNzX3Njb3JlIGlzIGRlZmluZWQgZWxzZSByZXZpZXcub3ZlcmFsbF9zY29yZSAlfQogIHslIHNldCBwcmVkaWN0ZWRfcm9sZV9mYW1pbHkgPSByZXZpZXcucHJlZGljdGVkX3JvbGVfZmFtaWx5IGlmIHJldmlldy5wcmVkaWN0ZWRfcm9sZV9mYW1pbHkgaXMgZGVmaW5lZCBlbHNlICcnICV9CiAgeyUgc2V0IGNhbmRpZGF0ZV9sZXZlbCA9IHJldmlldy5jYW5kaWRhdGVfbGV2ZWwgaWYgcmV2aWV3LmNhbmRpZGF0ZV9sZXZlbCBpcyBkZWZpbmVkIGVsc2UgJycgJX0KICB7JSBzZXQgeWVhcnNfZXhwZXJpZW5jZSA9IHJldmlldy5lc3RpbWF0ZWRfeWVhcnNfZXhwZXJpZW5jZSBpZiByZXZpZXcuZXN0aW1hdGVkX3llYXJzX2V4cGVyaWVuY2UgaXMgZGVmaW5lZCBlbHNlIDAgJX0KICB7JSBzZXQgc2tpbGxzX2xpc3QgPSByZXZpZXcuc2tpbGxzX2xpc3QgaWYgcmV2aWV3LnNraWxsc19saXN0IGlzIGRlZmluZWQgYW5kIHJldmlldy5za2lsbHNfbGlzdCBlbHNlIFtdICV9CiAgeyUgc2V0IG1pc3Npbmdfc2tpbGxzID0gcmV2aWV3Lm1pc3Npbmdfc2tpbGxzIGlmIHJldmlldy5taXNzaW5nX3NraWxscyBpcyBkZWZpbmVkIGFuZCByZXZpZXcubWlzc2luZ19za2lsbHMgZWxzZSBbXSAlfQogIHslIHNldCByZWNvbW1lbmRlZF9za2lsbHMgPSByZXZpZXcucmVjb21tZW5kZWRfc2tpbGxzIGlmIHJldmlldy5yZWNvbW1lbmRlZF9za2lsbHMgaXMgZGVmaW5lZCBhbmQgcmV2aWV3LnJlY29tbWVuZGVkX3NraWxscyBlbHNlIFtdICV9CiAgeyUgc2V0IHN0cmVuZ3RocyA9IHJldmlldy5zdHJlbmd0aHMgaWYgcmV2aWV3LnN0cmVuZ3RocyBpcyBkZWZpbmVkIGFuZCByZXZpZXcuc3RyZW5ndGhzIGVsc2UgW10gJX0KICB7JSBzZXQgbGVhcm5pbmdfcmVjb21tZW5kYXRpb25zID0gcmV2aWV3LmxlYXJuaW5nX3JlY29tbWVuZGF0aW9ucyBpZiByZXZpZXcubGVhcm5pbmdfcmVjb21tZW5kYXRpb25zIGlzIGRlZmluZWQgYW5kIHJldmlldy5sZWFybmluZ19yZWNvbW1lbmRhdGlvbnMgZWxzZSBbXSAlfQogIHslIHNldCB0YXJnZXRfcm9sZV9oaW50cyA9IHJldmlldy50YXJnZXRfcm9sZV9oaW50cyBpZiByZXZpZXcudGFyZ2V0X3JvbGVfaGludHMgaXMgZGVmaW5lZCBhbmQgcmV2aWV3LnRhcmdldF9yb2xlX2hpbnRzIGVsc2UgW10gJX0KICB7JSBzZXQgcmVzdW1lX2NoZWNrbGlzdCA9IHJldmlldy5yZXN1bWVfY2hlY2tsaXN0IGlmIHJldmlldy5yZXN1bWVfY2hlY2tsaXN0IGlzIGRlZmluZWQgYW5kIHJldmlldy5yZXN1bWVfY2hlY2tsaXN0IGVsc2UgW10gJX0KICB7JSBzZXQgcmVjb21tZW5kZWRfY291cnNlcyA9IHJldmlldy5yZWNvbW1lbmRlZF9jb3Vyc2VzIGlmIHJldmlldy5yZWNvbW1lbmRlZF9jb3Vyc2VzIGlzIGRlZmluZWQgYW5kIHJldmlldy5yZWNvbW1lbmRlZF9jb3Vyc2VzIGVsc2UgW10gJX0KICB7JSBzZXQgcmVzdW1lX3Jlc291cmNlcyA9IHJldmlldy5yZXN1bWVfcmVzb3VyY2VzIGlmIHJldmlldy5yZXN1bWVfcmVzb3VyY2VzIGlzIGRlZmluZWQgYW5kIHJldmlldy5yZXN1bWVfcmVzb3VyY2VzIGVsc2UgW10gJX0KICB7JSBzZXQgaW50ZXJ2aWV3X3Jlc291cmNlcyA9IHJldmlldy5pbnRlcnZpZXdfcmVzb3VyY2VzIGlmIHJldmlldy5pbnRlcnZpZXdfcmVzb3VyY2VzIGlzIGRlZmluZWQgYW5kIHJldmlldy5pbnRlcnZpZXdfcmVzb3VyY2VzIGVsc2UgW10gJX0KCiAgPGRpdiBjbGFzcz0ibGktc2hlbGwgbGktZGV0YWlsIGxpLXJlc3VtZSI+CiAgICA8aGVhZGVyIGNsYXNzPSJsaS1oZXJvIj4KICAgICAgPGRpdj4KICAgICAgICA8ZGl2IGNsYXNzPSJsaS1raWNrZXIiPlJlc3VtZSBJbnRlbGxpZ2VuY2U8L2Rpdj4KICAgICAgICA8aDE+RGV0YWlsZWQgUmVzdW1lIFJldmlldzwvaDE+CiAgICAgICAgPHAgY2xhc3M9ImxpLXN1YnRpdGxlIj5SZXZpZXcgY3JlYXRlZCB7eyByZXZpZXcudGltZXN0YW1wIG9yICcnIH19IHdpdGggQUktbGVkIHNlY3Rpb24gcGFyc2luZywgc2NvcmUgYnJlYWtkb3duLCBpc3N1ZXMsIGFuZCByZXdyaXRlIGd1aWRhbmNlLjwvcD4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImxpLWhlcm8tbWV0YSI+CiAgICAgICAgPHNwYW4gY2xhc3M9ImxpLXBpbGwge3sgJ29uJyBpZiBnZW1pbmlfZW5hYmxlZCBlbHNlICdvZmYnIH19Ij4KICAgICAgICAgIHt7ICdHZW1pbmkgYW5hbHlzaXMnIGlmIGFuYWx5c2lzX2VuZ2luZSA9PSAnZ2VtaW5pJyBlbHNlICgnT2xsYW1hIGFuYWx5c2lzJyBpZiBhbmFseXNpc19lbmdpbmUgPT0gJ29sbGFtYScgZWxzZSAnUnVsZSBmYWxsYmFjaycpIH19CiAgICAgICAgPC9zcGFuPgogICAgICAgIDxkaXYgY2xhc3M9ImxpLXNjb3JlIiBzdHlsZT0iLS1zY29yZToge3sgcmV2aWV3Lm92ZXJhbGxfc2NvcmUgb3IgMCB9fTsiPgogICAgICAgICAgPGRpdiBjbGFzcz0ibGktc2NvcmUtaW5uZXIiPgogICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1zY29yZS1udW0iPnt7IHJldmlldy5vdmVyYWxsX3Njb3JlIG9yIDAgfX08L2Rpdj4KICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktc2NvcmUtbGFiZWwiPlJlc3VtZSBzY29yZTwvZGl2PgogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CiAgICAgIDwvZGl2PgogICAgPC9oZWFkZXI+CgogICAgeyUgaWYgcmV2aWV3LmFuYWx5c2lzX25vdGljZSAlfQogICAgICA8ZGl2IGNsYXNzPSJsaS1hbGVydCI+e3sgcmV2aWV3LmFuYWx5c2lzX25vdGljZSB9fTwvZGl2PgogICAgeyUgZW5kaWYgJX0KCiAgICA8ZGl2IGNsYXNzPSJsaS1ncmlkIj4KICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZCI+CiAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICAgIDxoMz5TbmFwc2hvdDwvaDM+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0ibGktc3RhdC1ncmlkIj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXN0YXQiPgogICAgICAgICAgICA8c3Bhbj5PdmVyYWxsIHNjb3JlPC9zcGFuPgogICAgICAgICAgICA8c3Ryb25nPnt7IHJldmlldy5vdmVyYWxsX3Njb3JlIG9yIDAgfX08L3N0cm9uZz4KICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPGRpdiBjbGFzcz0ibGktc3RhdCI+CiAgICAgICAgICAgIDxzcGFuPkFUUyByZWFkaW5lc3M8L3NwYW4+CiAgICAgICAgICAgIDxzdHJvbmc+e3sgYXRzX3JlYWRpbmVzc19zY29yZSBvciAwIH19PC9zdHJvbmc+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXN0YXQiPgogICAgICAgICAgICA8c3Bhbj5Jc3N1ZXM8L3NwYW4+CiAgICAgICAgICAgIDxzdHJvbmc+e3sgaXNzdWVzfGxlbmd0aCB9fTwvc3Ryb25nPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1zdGF0Ij4KICAgICAgICAgICAgPHNwYW4+RmxhZ2dlZCBsaW5lczwvc3Bhbj4KICAgICAgICAgICAgPHN0cm9uZz57eyBsaW5lX3Jldmlld3N8bGVuZ3RoIH19PC9zdHJvbmc+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXN0YXQiPgogICAgICAgICAgICA8c3Bhbj5CdWxsZXQgcmV3cml0ZXM8L3NwYW4+CiAgICAgICAgICAgIDxzdHJvbmc+e3sgaW1wcm92ZWRfYnVsbGV0c3xsZW5ndGggfX08L3N0cm9uZz4KICAgICAgICAgIDwvZGl2PgogICAgICAgIDwvZGl2PgogICAgICA8L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZCI+CiAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICAgIDxoMz5Sb2xlIGZpdDwvaDM+CiAgICAgICAgPC9kaXY+CiAgICAgICAgPGRpdiBjbGFzcz0ibGktc3RhdC1ncmlkIj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXN0YXQiPgogICAgICAgICAgICA8c3Bhbj5QcmVkaWN0ZWQgZmFtaWx5PC9zcGFuPgogICAgICAgICAgICA8c3Ryb25nPnt7IHByZWRpY3RlZF9yb2xlX2ZhbWlseSBvciAnTm90IGluZmVycmVkIHlldCcgfX08L3N0cm9uZz4KICAgICAgICAgIDwvZGl2PgogICAgICAgICAgPGRpdiBjbGFzcz0ibGktc3RhdCI+CiAgICAgICAgICAgIDxzcGFuPkNhbmRpZGF0ZSBsZXZlbDwvc3Bhbj4KICAgICAgICAgICAgPHN0cm9uZz57eyBjYW5kaWRhdGVfbGV2ZWwgb3IgJ05vdCBpbmZlcnJlZCB5ZXQnIH19PC9zdHJvbmc+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXN0YXQiPgogICAgICAgICAgICA8c3Bhbj5ZZWFycyBleHBlcmllbmNlPC9zcGFuPgogICAgICAgICAgICA8c3Ryb25nPnt7IHllYXJzX2V4cGVyaWVuY2Ugb3IgMCB9fTwvc3Ryb25nPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1zdGF0Ij4KICAgICAgICAgICAgPHNwYW4+VGFyZ2V0IHJvbGUgaGludHM8L3NwYW4+CiAgICAgICAgICAgIDxzdHJvbmc+e3sgdGFyZ2V0X3JvbGVfaGludHN8bGVuZ3RoIH19PC9zdHJvbmc+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICA8L2Rpdj4KICAgICAgICB7JSBpZiB0YXJnZXRfcm9sZV9oaW50cyAlfQogICAgICAgICAgPHVsIGNsYXNzPSJsaS1saXN0IiBzdHlsZT0ibWFyZ2luLXRvcDogMTJweDsiPgogICAgICAgICAgICB7JSBmb3Igcm9sZSBpbiB0YXJnZXRfcm9sZV9oaW50c1s6NV0gJX0KICAgICAgICAgICAgICA8bGk+e3sgcm9sZSB9fTwvbGk+CiAgICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgICAgPC91bD4KICAgICAgICB7JSBlbmRpZiAlfQogICAgICA8L2Rpdj4KCiAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQiPgogICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgICA8aDM+VG9wIGlzc3VlczwvaDM+CiAgICAgICAgPC9kaXY+CiAgICAgICAgeyUgaWYgaXNzdWVzICV9CiAgICAgICAgICA8dWwgY2xhc3M9ImxpLWxpc3QiPgogICAgICAgICAgICB7JSBmb3IgaXNzdWUgaW4gaXNzdWVzWzo2XSAlfQogICAgICAgICAgICAgIDxsaT57eyBpc3N1ZSB9fTwvbGk+CiAgICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgICAgPC91bD4KICAgICAgICB7JSBlbHNlICV9CiAgICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+Tm8gbWFqb3IgaXNzdWVzIGRldGVjdGVkLjwvcD4KICAgICAgICB7JSBlbmRpZiAlfQogICAgICA8L2Rpdj4KICAgIDwvZGl2PgoKICAgIDxkaXYgY2xhc3M9ImxpLWdyaWQiPgogICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkIj4KICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkLWhlYWQiPgogICAgICAgICAgPGgzPlNraWxscyBnYXAgYW5hbHlzaXM8L2gzPgogICAgICAgIDwvZGl2PgogICAgICAgIDxkaXYgY2xhc3M9ImxpLXN0YXQtZ3JpZCI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1zdGF0Ij4KICAgICAgICAgICAgPHNwYW4+RGV0ZWN0ZWQgc2tpbGxzPC9zcGFuPgogICAgICAgICAgICA8c3Ryb25nPnt7IHNraWxsc19saXN0fGxlbmd0aCB9fTwvc3Ryb25nPgogICAgICAgICAgPC9kaXY+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1zdGF0Ij4KICAgICAgICAgICAgPHNwYW4+TWlzc2luZyBza2lsbHM8L3NwYW4+CiAgICAgICAgICAgIDxzdHJvbmc+e3sgbWlzc2luZ19za2lsbHN8bGVuZ3RoIH19PC9zdHJvbmc+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXN0YXQiPgogICAgICAgICAgICA8c3Bhbj5SZWNvbW1lbmRlZDwvc3Bhbj4KICAgICAgICAgICAgPHN0cm9uZz57eyByZWNvbW1lbmRlZF9za2lsbHN8bGVuZ3RoIH19PC9zdHJvbmc+CiAgICAgICAgICA8L2Rpdj4KICAgICAgICA8L2Rpdj4KICAgICAgICB7JSBpZiBza2lsbHNfbGlzdCAlfQogICAgICAgICAgPHAgY2xhc3M9ImxpLW5vdGUiIHN0eWxlPSJtYXJnaW4tdG9wOiAxMnB4OyI+RGV0ZWN0ZWQ6IHt7IHNraWxsc19saXN0WzoxMl18am9pbignLCAnKSB9fTwvcD4KICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgIHslIGlmIG1pc3Npbmdfc2tpbGxzICV9CiAgICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+TWlzc2luZzoge3sgbWlzc2luZ19za2lsbHNbOjEwXXxqb2luKCcsICcpIH19PC9wPgogICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgeyUgaWYgbm90IHNraWxsc19saXN0IGFuZCBub3QgbWlzc2luZ19za2lsbHMgJX0KICAgICAgICAgIDxwIGNsYXNzPSJsaS1ub3RlIj5ObyBza2lsbHMgZ2FwIGRhdGEgYXZhaWxhYmxlIGluIHRoaXMgcmV2aWV3IHlldC48L3A+CiAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQiPgogICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgICA8aDM+U3RyZW5ndGhzIGFuZCBuZXh0IGFjdGlvbnM8L2gzPgogICAgICAgIDwvZGl2PgogICAgICAgIHslIGlmIHN0cmVuZ3RocyAlfQogICAgICAgICAgPHNwYW4gY2xhc3M9ImxpLW11dGVkIj5TdHJlbmd0aHM8L3NwYW4+CiAgICAgICAgICA8dWwgY2xhc3M9ImxpLWxpc3QiPgogICAgICAgICAgICB7JSBmb3IgaXRlbSBpbiBzdHJlbmd0aHNbOjVdICV9CiAgICAgICAgICAgICAgPGxpPnt7IGl0ZW0gfX08L2xpPgogICAgICAgICAgICB7JSBlbmRmb3IgJX0KICAgICAgICAgIDwvdWw+CiAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgICB7JSBpZiBsZWFybmluZ19yZWNvbW1lbmRhdGlvbnMgJX0KICAgICAgICAgIDxzcGFuIGNsYXNzPSJsaS1tdXRlZCI+TGVhcm5pbmcgcGxhbjwvc3Bhbj4KICAgICAgICAgIDx1bCBjbGFzcz0ibGktbGlzdCI+CiAgICAgICAgICAgIHslIGZvciBpdGVtIGluIGxlYXJuaW5nX3JlY29tbWVuZGF0aW9uc1s6NV0gJX0KICAgICAgICAgICAgICA8bGk+e3sgaXRlbSB9fTwvbGk+CiAgICAgICAgICAgIHslIGVuZGZvciAlfQogICAgICAgICAgPC91bD4KICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgIHslIGlmIG5vdCBzdHJlbmd0aHMgYW5kIG5vdCBsZWFybmluZ19yZWNvbW1lbmRhdGlvbnMgJX0KICAgICAgICAgIDxwIGNsYXNzPSJsaS1ub3RlIj5ObyBhZGRpdGlvbmFsIHN0cmVuZ3RocyBvciBsZWFybmluZyBwbGFuIGl0ZW1zIHdlcmUgZ2VuZXJhdGVkLjwvcD4KICAgICAgICB7JSBlbmRpZiAlfQogICAgICA8L2Rpdj4KICAgIDwvZGl2PgoKICAgIDxkaXYgY2xhc3M9ImxpLWdyaWQiPgogICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkIj4KICAgICAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkLWhlYWQiPgogICAgICAgICAgPGgzPlJlY29tbWVuZGVkIGNvdXJzZXM8L2gzPgogICAgICAgICAgPHNwYW4gY2xhc3M9ImxpLXRhZyI+Um9sZS1hbGlnbmVkPC9zcGFuPgogICAgICAgIDwvZGl2PgogICAgICAgIHslIGlmIHJlY29tbWVuZGVkX2NvdXJzZXMgJX0KICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWZvY3VzLWxpc3QiPgogICAgICAgICAgICB7JSBmb3IgaXRlbSBpbiByZWNvbW1lbmRlZF9jb3Vyc2VzWzo1XSAlfQogICAgICAgICAgICAgIHslIHNldCBjb3Vyc2VfdGl0bGUgPSBpdGVtLnRpdGxlIGlmIGl0ZW0udGl0bGUgaXMgZGVmaW5lZCBlbHNlIGl0ZW0gJX0KICAgICAgICAgICAgICB7JSBzZXQgY291cnNlX3VybCA9IGl0ZW0udXJsIGlmIGl0ZW0udXJsIGlzIGRlZmluZWQgZWxzZSAnJyAlfQogICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWZvY3VzLWl0ZW0iPgogICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktZm9jdXMtdGl0bGUiPnt7IGNvdXJzZV90aXRsZSB9fTwvZGl2PgogICAgICAgICAgICAgICAgeyUgaWYgY291cnNlX3VybCAlfQogICAgICAgICAgICAgICAgICA8YSBjbGFzcz0ibGktbGluayIgaHJlZj0ie3sgY291cnNlX3VybCB9fSIgdGFyZ2V0PSJfYmxhbmsiIHJlbD0ibm9vcGVuZXIgbm9yZWZlcnJlciI+e3sgY291cnNlX3VybCB9fTwvYT4KICAgICAgICAgICAgICAgIHslIGVsc2UgJX0KICAgICAgICAgICAgICAgICAgPHAgY2xhc3M9ImxpLW5vdGUiPk5vIFVSTCBhdmFpbGFibGUuPC9wPgogICAgICAgICAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgICA8L2Rpdj4KICAgICAgICB7JSBlbHNlICV9CiAgICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+Tm8gY291cnNlIHJlY29tbWVuZGF0aW9ucyBhdmFpbGFibGUgZm9yIHRoaXMgcmV2aWV3IHlldC48L3A+CiAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQiPgogICAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgICA8aDM+TGVhcm5pbmcgcmVzb3VyY2VzPC9oMz4KICAgICAgICA8L2Rpdj4KICAgICAgICB7JSBpZiByZXN1bWVfcmVzb3VyY2VzICV9CiAgICAgICAgICA8c3BhbiBjbGFzcz0ibGktbXV0ZWQiPlJlc3VtZSB3cml0aW5nIHZpZGVvczwvc3Bhbj4KICAgICAgICAgIDx1bCBjbGFzcz0ibGktbGlzdCI+CiAgICAgICAgICAgIHslIGZvciB1cmwgaW4gcmVzdW1lX3Jlc291cmNlc1s6NF0gJX0KICAgICAgICAgICAgICA8bGk+PGEgY2xhc3M9ImxpLWxpbmsiIGhyZWY9Int7IHVybCB9fSIgdGFyZ2V0PSJfYmxhbmsiIHJlbD0ibm9vcGVuZXIgbm9yZWZlcnJlciI+UmVzdW1lIHZpZGVvIHt7IGxvb3AuaW5kZXggfX08L2E+PC9saT4KICAgICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgICA8L3VsPgogICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgeyUgaWYgaW50ZXJ2aWV3X3Jlc291cmNlcyAlfQogICAgICAgICAgPHNwYW4gY2xhc3M9ImxpLW11dGVkIj5JbnRlcnZpZXcgcHJlcGFyYXRpb24gdmlkZW9zPC9zcGFuPgogICAgICAgICAgPHVsIGNsYXNzPSJsaS1saXN0Ij4KICAgICAgICAgICAgeyUgZm9yIHVybCBpbiBpbnRlcnZpZXdfcmVzb3VyY2VzWzo0XSAlfQogICAgICAgICAgICAgIDxsaT48YSBjbGFzcz0ibGktbGluayIgaHJlZj0ie3sgdXJsIH19IiB0YXJnZXQ9Il9ibGFuayIgcmVsPSJub29wZW5lciBub3JlZmVycmVyIj5JbnRlcnZpZXcgdmlkZW8ge3sgbG9vcC5pbmRleCB9fTwvYT48L2xpPgogICAgICAgICAgICB7JSBlbmRmb3IgJX0KICAgICAgICAgIDwvdWw+CiAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgICB7JSBpZiBub3QgcmVzdW1lX3Jlc291cmNlcyBhbmQgbm90IGludGVydmlld19yZXNvdXJjZXMgJX0KICAgICAgICAgIDxwIGNsYXNzPSJsaS1ub3RlIj5ObyBsZWFybmluZyByZXNvdXJjZXMgYXZhaWxhYmxlIGluIHRoaXMgcmV2aWV3IHlldC48L3A+CiAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KCiAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkIj4KICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICA8aDM+QVRTIGNoZWNrbGlzdDwvaDM+CiAgICAgIDwvZGl2PgogICAgICB7JSBpZiByZXN1bWVfY2hlY2tsaXN0ICV9CiAgICAgICAgPGRpdiBjbGFzcz0ibGktZm9jdXMtbGlzdCI+CiAgICAgICAgICB7JSBmb3IgaXRlbSBpbiByZXN1bWVfY2hlY2tsaXN0ICV9CiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWZvY3VzLWl0ZW0iPgogICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWZvY3VzLXRpdGxlIj57eyBpdGVtLmxhYmVsIH19PC9kaXY+CiAgICAgICAgICAgICAgPHAgY2xhc3M9ImxpLW5vdGUiPnt7IGl0ZW0uZGV0YWlsIH19PC9wPgogICAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJsaS10YWcge3sgJ2xpLXRhZy1hY2NlbnQnIGlmIGl0ZW0uc3RhdHVzID09ICdnb29kJyBlbHNlICdsaS10YWctd2FybicgfX0iPgogICAgICAgICAgICAgICAge3sgJ0dvb2QnIGlmIGl0ZW0uc3RhdHVzID09ICdnb29kJyBlbHNlICdOZWVkcyB3b3JrJyB9fQogICAgICAgICAgICAgIDwvc3Bhbj4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICB7JSBlbmRmb3IgJX0KICAgICAgICA8L2Rpdj4KICAgICAgeyUgZWxzZSAlfQogICAgICAgIDxwIGNsYXNzPSJsaS1ub3RlIj5ObyBBVFMgY2hlY2tsaXN0IGF2YWlsYWJsZSBpbiB0aGlzIHJldmlldyB5ZXQuPC9wPgogICAgICB7JSBlbmRpZiAlfQogICAgPC9kaXY+CgogICAgPGRpdiBjbGFzcz0ibGktY2FyZCI+CiAgICAgIDxkaXYgY2xhc3M9ImxpLWNhcmQtaGVhZCI+CiAgICAgICAgPGgzPlNjb3JlIGJyZWFrZG93bjwvaDM+CiAgICAgIDwvZGl2PgogICAgICB7JSBpZiBicmVha2Rvd24gJX0KICAgICAgICA8ZGl2IGNsYXNzPSJsaS1iYXJzIj4KICAgICAgICAgIHslIGZvciBrZXksIHZhbCBpbiBicmVha2Rvd24uaXRlbXMoKSAlfQogICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1iYXIiPgogICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWJhci1sYWJlbCI+e3sga2V5IH19PC9kaXY+CiAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktYmFyLXRyYWNrIj48c3BhbiBzdHlsZT0iLS12YWw6IHt7IHZhbCB9fTsiPjwvc3Bhbj48L2Rpdj4KICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1iYXItdmFsIj57eyB2YWwgfX08L2Rpdj4KICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICB7JSBlbmRmb3IgJX0KICAgICAgICA8L2Rpdj4KICAgICAgeyUgZWxzZSAlfQogICAgICAgIDxwIGNsYXNzPSJsaS1ub3RlIj5ObyBjYXRlZ29yeSBzY29yZXMgYXZhaWxhYmxlIHlldC48L3A+CiAgICAgIHslIGVuZGlmICV9CiAgICA8L2Rpdj4KCiAgICA8ZGl2IGNsYXNzPSJsaS1jYXJkIj4KICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICA8aDM+U2VjdGlvbi13aXNlIHJldmlldzwvaDM+CiAgICAgICAgPHNwYW4gY2xhc3M9ImxpLXRhZyI+e3sgc2VjdGlvbl9yZXBvcnR8bGVuZ3RoIH19IHNlY3Rpb25zPC9zcGFuPgogICAgICA8L2Rpdj4KICAgICAgeyUgaWYgc2VjdGlvbl9yZXBvcnQgJX0KICAgICAgICA8ZGl2IGNsYXNzPSJsaS1zZWN0aW9uLXN0YWNrIj4KICAgICAgICAgIHslIGZvciBzZWN0aW9uIGluIHNlY3Rpb25fcmVwb3J0ICV9CiAgICAgICAgICAgIDxzZWN0aW9uIGNsYXNzPSJsaS1mb2N1cy1pdGVtIGxpLXNlY3Rpb24tY2FyZCI+CiAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktY2FyZC1oZWFkIj4KICAgICAgICAgICAgICAgIDxoMz57eyBzZWN0aW9uLmxhYmVsIH19PC9oMz4KICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXRhZy1ncm91cCI+CiAgICAgICAgICAgICAgICAgIHslIGlmIHNlY3Rpb24ucmVjb21tZW5kYXRpb25zICV9CiAgICAgICAgICAgICAgICAgICAgPHNwYW4gY2xhc3M9ImxpLXRhZyI+e3sgc2VjdGlvbi5yZWNvbW1lbmRhdGlvbnN8bGVuZ3RoIH19IGFjdGlvbnM8L3NwYW4+CiAgICAgICAgICAgICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgICAgICAgICAgIHslIGlmIHNlY3Rpb24ubGluZV9yZXZpZXdzICV9CiAgICAgICAgICAgICAgICAgICAgPHNwYW4gY2xhc3M9ImxpLXRhZyBsaS10YWctd2FybiI+e3sgc2VjdGlvbi5saW5lX3Jldmlld3N8bGVuZ3RoIH19IGRpYWdub3N0aWNzPC9zcGFuPgogICAgICAgICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgICAgICAgICB7JSBpZiBzZWN0aW9uLmltcHJvdmVkX2J1bGxldHMgJX0KICAgICAgICAgICAgICAgICAgICA8c3BhbiBjbGFzcz0ibGktdGFnIGxpLXRhZy1hY2NlbnQiPnt7IHNlY3Rpb24uaW1wcm92ZWRfYnVsbGV0c3xsZW5ndGggfX0gcmV3cml0ZXM8L3NwYW4+CiAgICAgICAgICAgICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICA8L2Rpdj4KCiAgICAgICAgICAgICAgeyUgaWYgc2VjdGlvbi5yYXdfdGV4dCAlfQogICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktc2VjdGlvbi1ibG9jayI+CiAgICAgICAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJsaS1tdXRlZCI+RGV0ZWN0ZWQgY29udGVudDwvc3Bhbj4KICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktY29weS1ibG9jayI+e3sgc2VjdGlvbi5yYXdfdGV4dCB8IHJlcGxhY2UoJ8Oi4oKs4oCdJywgJy0nKSB9fTwvZGl2PgogICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgeyUgZW5kaWYgJX0KCiAgICAgICAgICAgICAgeyUgaWYgc2VjdGlvbi5yZWNvbW1lbmRhdGlvbnMgJX0KICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXNlY3Rpb24tYmxvY2siPgogICAgICAgICAgICAgICAgICA8c3BhbiBjbGFzcz0ibGktbXV0ZWQiPlJlY29tbWVuZGVkIGZpeGVzPC9zcGFuPgogICAgICAgICAgICAgICAgICA8dWwgY2xhc3M9ImxpLWxpc3QiPgogICAgICAgICAgICAgICAgICAgIHslIGZvciBpdGVtIGluIHNlY3Rpb24ucmVjb21tZW5kYXRpb25zICV9CiAgICAgICAgICAgICAgICAgICAgICA8bGk+e3sgaXRlbSB9fTwvbGk+CiAgICAgICAgICAgICAgICAgICAgeyUgZW5kZm9yICV9CiAgICAgICAgICAgICAgICAgIDwvdWw+CiAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICB7JSBlbmRpZiAlfQoKICAgICAgICAgICAgICB7JSBpZiBzZWN0aW9uLmxpbmVfcmV2aWV3cyAlfQogICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktc2VjdGlvbi1ibG9jayI+CiAgICAgICAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJsaS1tdXRlZCI+RGlhZ25vc3RpY3M8L3NwYW4+CiAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWZvY3VzLWxpc3QiPgogICAgICAgICAgICAgICAgICAgIHslIGZvciBpdGVtIGluIHNlY3Rpb24ubGluZV9yZXZpZXdzICV9CiAgICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPSJsaS1mb2N1cy1pdGVtIj4KICAgICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktZm9jdXMtdGl0bGUiPnt7IGl0ZW0ubGluZSB8IHJlcGxhY2UoJ8Oi4oKs4oCdJywgJy0nKSB9fTwvZGl2PgogICAgICAgICAgICAgICAgICAgICAgICA8cCBjbGFzcz0ibGktbm90ZSI+UmVhc29uOiB7eyBpdGVtLnJlYXNvbiB9fTwvcD4KICAgICAgICAgICAgICAgICAgICAgICAgeyUgaWYgaXRlbS5zdWdnZXN0aW9uICV9CiAgICAgICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktY29weS1ibG9jayI+e3sgaXRlbS5zdWdnZXN0aW9uIHwgcmVwbGFjZSgnw6LigqzigJ0nLCAnLScpIH19PC9kaXY+CiAgICAgICAgICAgICAgICAgICAgICAgIHslIGVuZGlmICV9CiAgICAgICAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICAgICAgICB7JSBlbmRmb3IgJX0KICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICB7JSBlbmRpZiAlfQoKICAgICAgICAgICAgICB7JSBpZiBzZWN0aW9uLmltcHJvdmVkX2J1bGxldHMgJX0KICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLXNlY3Rpb24tYmxvY2siPgogICAgICAgICAgICAgICAgICA8c3BhbiBjbGFzcz0ibGktbXV0ZWQiPlJld3JpdGUgc3VnZ2VzdGlvbnM8L3NwYW4+CiAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWZvY3VzLWxpc3QiPgogICAgICAgICAgICAgICAgICAgIHslIGZvciBpdGVtIGluIHNlY3Rpb24uaW1wcm92ZWRfYnVsbGV0cyAlfQogICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktZm9jdXMtaXRlbSI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxzcGFuIGNsYXNzPSJsaS1tdXRlZCI+T3JpZ2luYWw8L3NwYW4+CiAgICAgICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9ImxpLWNvcHktYmxvY2siPnt7IGl0ZW0ub3JpZ2luYWwgfCByZXBsYWNlKCfDouKCrOKAnScsICctJykgfX08L2Rpdj4KICAgICAgICAgICAgICAgICAgICAgICAgPHNwYW4gY2xhc3M9ImxpLW11dGVkIiBzdHlsZT0ibWFyZ2luLXRvcDogOHB4OyI+U3VnZ2VzdGlvbjwvc3Bhbj4KICAgICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz0ibGktY29weS1ibG9jayI+e3sgaXRlbS5zdWdnZXN0aW9uIHwgcmVwbGFjZSgnw6LigqzigJ0nLCAnLScpIH19PC9kaXY+CiAgICAgICAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICAgICAgICB7JSBlbmRmb3IgJX0KICAgICAgICAgICAgICAgICAgPC9kaXY+CiAgICAgICAgICAgICAgICA8L2Rpdj4KICAgICAgICAgICAgICB7JSBlbmRpZiAlfQogICAgICAgICAgICA8L3NlY3Rpb24+CiAgICAgICAgICB7JSBlbmRmb3IgJX0KICAgICAgICA8L2Rpdj4KICAgICAgeyUgZWxzZSAlfQogICAgICAgIDxwIGNsYXNzPSJsaS1ub3RlIj5ObyBzZWN0aW9uLXdpc2UgaW5zaWdodHMgYXZhaWxhYmxlIHlldC48L3A+CiAgICAgIHslIGVuZGlmICV9CiAgICA8L2Rpdj4KCiAgICA8ZGl2IGNsYXNzPSJhY3Rpb25zIGxpLXByaW50LWhpZGUiPgogICAgICA8YnV0dG9uIGNsYXNzPSJidG4gYnRuLWdob3N0IiB0eXBlPSJidXR0b24iIG9uY2xpY2s9IndpbmRvdy5wcmludCgpIj5QcmludCAvIFNhdmUgUERGPC9idXR0b24+CiAgICAgIDxhIGNsYXNzPSJsaW5rLWJ0biIgaHJlZj0iL3Jlc3VtZS1yZXZpZXciPkJhY2sgdG8gUmV2aWV3czwvYT4KICAgIDwvZGl2PgogIDwvZGl2Pgp7JSBlbmRibG9jayAlfQo=","scan_email.html":"eyUgZXh0ZW5kcyAiYmFzZS5odG1sIiAlfQp7JSBibG9jayBjb250ZW50ICV9CiAgPGRpdiBjbGFzcz0icGFnZSI+CiAgICA8aGVhZGVyIGNsYXNzPSJoZWFkZXIiPgogICAgICA8ZGl2IGNsYXNzPSJpY29uLWJhZGdlIj4KICAgICAgICA8c3ZnIHdpZHRoPSIyNiIgaGVpZ2h0PSIyNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj4KICAgICAgICAgIDxwYXRoIGQ9Ik00IDZoMTZ2MTJINFY2eiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICAgIDxwYXRoIGQ9Ik00IDdsOCA2IDgtNiIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIxLjYiLz4KICAgICAgICA8L3N2Zz4KICAgICAgPC9kaXY+CiAgICAgIDxkaXY+CiAgICAgICAgPGgxPlNlbmQgU2NhbiBPdmVyIEVtYWlsPC9oMT4KICAgICAgICA8cCBjbGFzcz0ic3VidGl0bGUiPkRlbGl2ZXIgdGhlIG1hc3RlciBxdWFsaXR5IGZpbGUgdG8geW91ciBpbmJveC48L3A+CiAgICAgIDwvZGl2PgogICAgPC9oZWFkZXI+CgogICAgPGRpdiBjbGFzcz0iY2FyZCI+CiAgICAgIHslIGlmIGVycm9yICV9CiAgICAgICAgPGRpdiBjbGFzcz0ic3RhdHVzIGVycm9yIj57eyBlcnJvciB9fTwvZGl2PgogICAgICB7JSBlbmRpZiAlfQogICAgICB7JSBpZiBzdWNjZXNzICV9CiAgICAgICAgPGRpdiBjbGFzcz0ic3RhdHVzIGRvbmUiPkVtYWlsIHNlbnQgc3VjY2Vzc2Z1bGx5LjwvZGl2PgogICAgICB7JSBlbmRpZiAlfQoKICAgICAgPHAgY2xhc3M9Im5vdGUiPkZpbGU6IDxzdHJvbmc+e3sgZmlsZV9uYW1lIH19PC9zdHJvbmc+eyUgaWYgbGFiZWwgJX0gfCB7eyBsYWJlbCB9fXslIGVuZGlmICV9PC9wPgogICAgICA8Zm9ybSBtZXRob2Q9InBvc3QiIGNsYXNzPSJzdGFnZ2VyIj4KICAgICAgICA8ZGl2IGNsYXNzPSJmaWVsZCI+CiAgICAgICAgICA8bGFiZWwgZm9yPSJ0b19lbWFpbCI+UmVjaXBpZW50IEVtYWlsPC9sYWJlbD4KICAgICAgICAgIDxpbnB1dCBpZD0idG9fZW1haWwiIG5hbWU9InRvX2VtYWlsIiB0eXBlPSJ0ZXh0IiBwbGFjZWhvbGRlcj0icmVjaXBpZW50QGVtYWlsLmNvbSIgcmVxdWlyZWQgLz4KICAgICAgICA8L2Rpdj4KICAgICAgICA8ZGl2IGNsYXNzPSJhY3Rpb25zIj4KICAgICAgICAgIDxidXR0b24gY2xhc3M9ImJ0biIgdHlwZT0ic3VibWl0Ij5TZW5kIEVtYWlsPC9idXR0b24+CiAgICAgICAgICB7JSBpZiBiYWNrX2hyZWYgJX0KICAgICAgICAgICAgPGEgY2xhc3M9ImxpbmstYnRuIiBocmVmPSJ7eyBiYWNrX2hyZWYgfX0iPnt7IGJhY2tfbGFiZWwgb3IgIkJhY2siIH19PC9hPgogICAgICAgICAgeyUgZWxpZiBqb2JfaWQgJX0KICAgICAgICAgICAgPGEgY2xhc3M9ImxpbmstYnRuIiBocmVmPSIvam9iL3t7IGpvYl9pZCB9fSI+QmFjayB0byBTY2FuPC9hPgogICAgICAgICAgeyUgZWxzZSAlfQogICAgICAgICAgICA8YSBjbGFzcz0ibGluay1idG4iIGhyZWY9Ii9zY2FuIj5CYWNrIHRvIHNjYW5zPC9hPgogICAgICAgICAgeyUgZW5kaWYgJX0KICAgICAgICA8L2Rpdj4KICAgICAgPC9mb3JtPgogICAgPC9kaXY+CiAgPC9kaXY+CnslIGVuZGJsb2NrICV9Cg=="}
EMBEDDED_STATIC_B64 = {"app.css":{"b64":"QGltcG9ydCB1cmwoImh0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9RnJhdW5jZXM6d2dodEA1MDA7NzAwJmZhbWlseT1NYW5yb3BlOndnaHRANDAwOzYwMCZkaXNwbGF5PXN3YXAiKTsKCjpyb290IHsKICAtLWJnLTE6ICMwNTA3MGU7CiAgLS1iZy0yOiAjMGIxMjIwOwogIC0tY2FyZDogIzBmMWEyYjsKICAtLWNhcmQtMjogIzEzMjQzYTsKICAtLWNhcmQtMzogIzBiMTQyNDsKICAtLWluazogI2U2ZWRmNzsKICAtLW11dGVkOiAjYTJiMGMwOwogIC0tYWNjZW50OiAjNDRkN2M1OwogIC0tYWNjZW50LTI6ICNmZjhhNjY7CiAgLS1hY2NlbnQtMzogI2Y1ZDI2YTsKICAtLWJvcmRlcjogcmdiYSgxNDgsIDE2MywgMTg0LCAwLjE4KTsKICAtLWJvcmRlci1zdHJvbmc6IHJnYmEoMTQ4LCAxNjMsIDE4NCwgMC4yOCk7CiAgLS1zaGFkb3c6IDAgMThweCA0MHB4IHJnYmEoMiwgNiwgMjMsIDAuNik7CiAgLS1zaGFkb3ctc3Ryb25nOiAwIDI4cHggNjBweCByZ2JhKDIsIDYsIDIzLCAwLjcpOwogIC0tcmFkaXVzOiAxNnB4Owp9CgoqIHsgYm94LXNpemluZzogYm9yZGVyLWJveDsgfQoKYm9keSB7CiAgbWFyZ2luOiAwOwogIGZvbnQtZmFtaWx5OiAiTWFucm9wZSIsICJTZWdvZSBVSSIsIHNhbnMtc2VyaWY7CiAgY29sb3I6IHZhcigtLWluayk7CiAgbGluZS1oZWlnaHQ6IDEuNTsKICBiYWNrZ3JvdW5kOgogICAgcmFkaWFsLWdyYWRpZW50KDkwMHB4IDUwMHB4IGF0IDE1JSAtMTAlLCByZ2JhKDI0NSwgMjEwLCAxMDYsIDAuMTIpLCB0cmFuc3BhcmVudCA2NSUpLAogICAgcmFkaWFsLWdyYWRpZW50KDcwMHB4IDQ1MHB4IGF0IDkwJSAwJSwgcmdiYSg2OCwgMjE1LCAxOTcsIDAuMTgpLCB0cmFuc3BhcmVudCA1NSUpLAogICAgbGluZWFyLWdyYWRpZW50KDE4MGRlZywgdmFyKC0tYmctMSkgMCUsIHZhcigtLWJnLTIpIDEwMCUpOwogIG1pbi1oZWlnaHQ6IDEwMHZoOwp9Cgpib2R5OjpiZWZvcmUgewogIGNvbnRlbnQ6ICIiOwogIHBvc2l0aW9uOiBmaXhlZDsKICBpbnNldDogMDsKICBiYWNrZ3JvdW5kLWltYWdlOiByYWRpYWwtZ3JhZGllbnQocmdiYSgyNTUsIDI1NSwgMjU1LCAwLjAzNSkgMXB4LCB0cmFuc3BhcmVudCAxcHgpOwogIGJhY2tncm91bmQtc2l6ZTogMjhweCAyOHB4OwogIHBvaW50ZXItZXZlbnRzOiBub25lOwogIG9wYWNpdHk6IDAuMzsKfQoKaDEsIGgyLCBoMywgaDQgewogIGZvbnQtZmFtaWx5OiAiRnJhdW5jZXMiLCAiR2VvcmdpYSIsIHNlcmlmOwogIG1hcmdpbjogMCAwIDEwcHg7CiAgb3ZlcmZsb3ctd3JhcDogYW55d2hlcmU7Cn0KCi5sYXlvdXQgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiAyNjBweCAxZnI7CiAgbWluLWhlaWdodDogMTAwdmg7Cn0KCi5zaWRlYmFyIHsKICBiYWNrZ3JvdW5kOiByZ2JhKDEwLCAxNiwgMjgsIDAuOTUpOwogIGNvbG9yOiAjZTZlZGY1OwogIHBhZGRpbmc6IDI0cHggMThweDsKICBwb3NpdGlvbjogc3RpY2t5OwogIHRvcDogMDsKICBoZWlnaHQ6IDEwMHZoOwogIGJhY2tkcm9wLWZpbHRlcjogYmx1cig4cHgpOwogIGJvcmRlci1yaWdodDogMXB4IHNvbGlkIHJnYmEoMTQ4LCAxNjMsIDE4NCwgMC4xNik7CiAgb3ZlcmZsb3c6IGhpZGRlbjsKfQoKLnNpZGViYXIuY29sbGFwc2VkIHsKICB3aWR0aDogODBweDsKICBwYWRkaW5nOiAyNHB4IDEwcHg7Cn0KCi5zaWRlYmFyLmNvbGxhcHNlZCAuYnJhbmQtdGV4dCwKLnNpZGViYXIuY29sbGFwc2VkIC5uYXYtbGFiZWwgewogIGRpc3BsYXk6IG5vbmU7Cn0KCi5zaWRlYmFyLmNvbGxhcHNlZCAubmF2LWxpbmsgewogIGp1c3RpZnktY29udGVudDogY2VudGVyOwogIHBhZGRpbmc6IDEwcHg7Cn0KCi5zaWRlYmFyLmNvbGxhcHNlZCAudG9nZ2xlIHsKICB3aWR0aDogMTAwJTsKICBmb250LXNpemU6IDA7CiAgcGFkZGluZzogMTBweDsKfQoKLnNpZGViYXIuY29sbGFwc2VkIC50b2dnbGU6OmFmdGVyIHsKICBjb250ZW50OiAiwrsiOwogIGZvbnQtc2l6ZTogMTRweDsKICBjb2xvcjogI2M3ZDJkZjsKfQoKLmJyYW5kIHsKICBkaXNwbGF5OiBmbGV4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAgZ2FwOiAxMnB4OwogIG1hcmdpbi1ib3R0b206IDI0cHg7Cn0KCi5icmFuZC1pY29uIHsKICB3aWR0aDogNDJweDsKICBoZWlnaHQ6IDQycHg7CiAgYm9yZGVyLXJhZGl1czogMTRweDsKICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTM1ZGVnLCB2YXIoLS1hY2NlbnQtMiksICNmM2EyNjEpOwogIGRpc3BsYXk6IGdyaWQ7CiAgcGxhY2UtaXRlbXM6IGNlbnRlcjsKICBmb250LXdlaWdodDogNzAwOwogIGNvbG9yOiAjZmZmOwp9CgouYnJhbmQtdGV4dCBzcGFuIHsKICBkaXNwbGF5OiBibG9jazsKICBmb250LXNpemU6IDEycHg7CiAgY29sb3I6ICNiOGM0ZDI7Cn0KCi5uYXYgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiA4cHg7Cn0KCi5uYXYtbGluayB7CiAgY29sb3I6ICNkNWRlZWE7CiAgdGV4dC1kZWNvcmF0aW9uOiBub25lOwogIHBhZGRpbmc6IDEwcHggMTJweDsKICBib3JkZXItcmFkaXVzOiAxMnB4OwogIGZvbnQtd2VpZ2h0OiA2MDA7CiAgdHJhbnNpdGlvbjogYmFja2dyb3VuZCAwLjJzIGVhc2U7CiAgZGlzcGxheTogZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGdhcDogMTBweDsKfQoKLm5hdi1saW5rOmhvdmVyIHsKICBiYWNrZ3JvdW5kOiByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMTYpOwp9CgoubmF2LWxpbmsuYWN0aXZlIHsKICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTM1ZGVnLCByZ2JhKDY4LCAyMTUsIDE5NywgMC4xNiksIHJnYmEoMjU1LCAxMzgsIDEwMiwgMC4xNCkpOwogIGJvcmRlcjogMXB4IHNvbGlkIHJnYmEoNjgsIDIxNSwgMTk3LCAwLjIyKTsKICBjb2xvcjogI2YyZmJmYTsKfQoKLm5hdi1saW5rLmFjdGl2ZSAubmF2LWljb24gewogIGNvbG9yOiAjYjdmZmYzOwp9CgoubmF2LWljb24gewogIHdpZHRoOiAyMHB4OwogIGhlaWdodDogMjBweDsKICBkaXNwbGF5OiBpbmxpbmUtZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGp1c3RpZnktY29udGVudDogY2VudGVyOwogIGNvbG9yOiAjYzdkMmRmOwogIGZsZXg6IDAgMCBhdXRvOwp9CgoubmF2LWljb24gc3ZnIHsKICB3aWR0aDogMjBweDsKICBoZWlnaHQ6IDIwcHg7Cn0KCi5uYXYtbGFiZWwgewogIHdoaXRlLXNwYWNlOiBub3dyYXA7Cn0KCi50b2dnbGUgewogIG1hcmdpbi10b3A6IDIwcHg7CiAgYmFja2dyb3VuZDogdHJhbnNwYXJlbnQ7CiAgY29sb3I6ICNjN2QyZGY7CiAgYm9yZGVyOiAxcHggc29saWQgcmdiYSgxNDgsIDE2MywgMTg0LCAwLjMpOwogIHBhZGRpbmc6IDhweCAxMHB4OwogIGJvcmRlci1yYWRpdXM6IDEwcHg7CiAgY3Vyc29yOiBwb2ludGVyOwp9CgoubWFpbiB7CiAgcGFkZGluZzogNDBweCAyOHB4IDcycHg7CiAgcG9zaXRpb246IHJlbGF0aXZlOwogIHotaW5kZXg6IDE7CiAgb3ZlcmZsb3cteDogaGlkZGVuOwp9CgoucGFnZSB7CiAgbWF4LXdpZHRoOiAxMTAwcHg7CiAgbWFyZ2luOiAwIGF1dG87CiAgd2lkdGg6IDEwMCU7CiAgcGFkZGluZzogMCA0cHg7Cn0KCi5wYWdlICogewogIG1pbi13aWR0aDogMDsKfQoKLnBhZ2UgcCwKLnBhZ2UgbGksCi5wYWdlIHNwYW4gewogIHdvcmQtYnJlYWs6IGJyZWFrLXdvcmQ7Cn0KCi5oZWFkZXIgewogIGRpc3BsYXk6IGZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBnYXA6IDE2cHg7CiAgY29sb3I6ICNlOWVlZjc7CiAgbWFyZ2luLWJvdHRvbTogMjRweDsKfQoKLnN1YnRpdGxlIHsKICBjb2xvcjogIzlmYjBjMzsKICBtYXJnaW46IDA7Cn0KCi5pY29uLWJhZGdlIHsKICB3aWR0aDogNTRweDsKICBoZWlnaHQ6IDU0cHg7CiAgYm9yZGVyLXJhZGl1czogMTZweDsKICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTM1ZGVnLCB2YXIoLS1hY2NlbnQtMiksICNmM2EyNjEpOwogIGRpc3BsYXk6IGZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsKICBib3gtc2hhZG93OiAwIDEwcHggMjRweCByZ2JhKDIsIDYsIDIzLCAwLjYpOwp9CgouY2FyZCB7CiAgYmFja2dyb3VuZDogdmFyKC0tY2FyZCk7CiAgYm9yZGVyLXJhZGl1czogdmFyKC0tcmFkaXVzKTsKICBwYWRkaW5nOiAxNnB4OwogIGJveC1zaGFkb3c6IHZhcigtLXNoYWRvdyk7CiAgYW5pbWF0aW9uOiBmYWRlVXAgMC43cyBlYXNlIGJvdGg7CiAgYm9yZGVyOiAxcHggc29saWQgdmFyKC0tYm9yZGVyKTsKfQoKLnRhYnMgewogIGRpc3BsYXk6IGZsZXg7CiAgZ2FwOiAxMHB4OwogIGZsZXgtd3JhcDogd3JhcDsKICBtYXJnaW46IDE4cHggMCAxMnB4Owp9CgoudGFiLWJ0biB7CiAgYmFja2dyb3VuZDogdmFyKC0tY2FyZC0yKTsKICBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIGNvbG9yOiB2YXIoLS1pbmspOwogIHBhZGRpbmc6IDhweCAxNHB4OwogIGJvcmRlci1yYWRpdXM6IDk5OXB4OwogIGZvbnQtd2VpZ2h0OiA2MDA7CiAgY3Vyc29yOiBwb2ludGVyOwogIHRyYW5zaXRpb246IGFsbCAwLjJzIGVhc2U7Cn0KCi50YWItYnRuLmFjdGl2ZSB7CiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDEzNWRlZywgcmdiYSg2OCwgMjE1LCAxOTcsIDAuMjUpLCByZ2JhKDI1NSwgMTM4LCAxMDIsIDAuMTgpKTsKICBib3JkZXItY29sb3I6IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjUpOwogIGNvbG9yOiAjZWFmZmY5OwogIGJveC1zaGFkb3c6IDAgMTBweCAyMHB4IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjIpOwp9CgoudGFiLXBhbmVsIHsKICBkaXNwbGF5OiBub25lOwp9CgoudGFiLXBhbmVsLmFjdGl2ZSB7CiAgZGlzcGxheTogYmxvY2s7Cn0KCi5wYWdlLnByZW1pdW0gLmNhcmQgewogIHBvc2l0aW9uOiByZWxhdGl2ZTsKICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTYwZGVnLCByZ2JhKDIwLCAzMiwgNTIsIDAuOTgpLCByZ2JhKDgsIDE0LCAyNCwgMC45NikpOwogIGJveC1zaGFkb3c6CiAgICAwIDI2cHggNjRweCByZ2JhKDIsIDYsIDIzLCAwLjc1KSwKICAgIDAgOHB4IDE4cHggcmdiYSgyLCA2LCAyMywgMC4zNSk7CiAgYm9yZGVyOiAxcHggc29saWQgcmdiYSgxNDgsIDE2MywgMTg0LCAwLjI0KTsKICB0cmFuc2l0aW9uOiB0cmFuc2Zvcm0gMC4ycyBlYXNlLCBib3gtc2hhZG93IDAuMnMgZWFzZTsKICBvdmVyZmxvdzogaGlkZGVuOwp9CgoucGFnZS5wcmVtaXVtIC5jYXJkOjphZnRlciB7CiAgY29udGVudDogIiI7CiAgcG9zaXRpb246IGFic29sdXRlOwogIGluc2V0OiAwOwogIGJvcmRlci1yYWRpdXM6IGluaGVyaXQ7CiAgYm94LXNoYWRvdzoKICAgIGluc2V0IDAgMXB4IDAgcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjA4KSwKICAgIGluc2V0IDAgMCAwIDFweCByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMDYpOwogIHBvaW50ZXItZXZlbnRzOiBub25lOwp9CgoucGFnZS5wcmVtaXVtIC5jYXJkOjpiZWZvcmUgewogIGNvbnRlbnQ6ICIiOwogIHBvc2l0aW9uOiBhYnNvbHV0ZTsKICBpbnNldDogLTFweDsKICBib3JkZXItcmFkaXVzOiBpbmhlcml0OwogIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCgxMzVkZWcsIHJnYmEoNjgsIDIxNSwgMTk3LCAwLjI4KSwgcmdiYSgyNTUsIDEzOCwgMTAyLCAwLjIyKSwgcmdiYSgyNDUsIDIxMCwgMTA2LCAwLjIpKTsKICBvcGFjaXR5OiAwLjM7CiAgZmlsdGVyOiBibHVyKDE2cHgpOwogIHotaW5kZXg6IDA7CiAgcG9pbnRlci1ldmVudHM6IG5vbmU7Cn0KCi5wYWdlLnByZW1pdW0gLmNhcmQgPiAqIHsKICBwb3NpdGlvbjogcmVsYXRpdmU7CiAgei1pbmRleDogMTsKfQoKLnBhZ2UucHJlbWl1bSAuY2FyZDpob3ZlciB7CiAgdHJhbnNmb3JtOiB0cmFuc2xhdGVZKC0ycHgpOwogIGJveC1zaGFkb3c6CiAgICAwIDMycHggNzJweCByZ2JhKDIsIDYsIDIzLCAwLjgpLAogICAgMCAxMnB4IDIycHggcmdiYSgyLCA2LCAyMywgMC41KTsKfQoKLnBhZ2UucHJlbWl1bSAuYmVudG8tY2FyZCB7CiAgdHJhbnNmb3JtLXN0eWxlOiBwcmVzZXJ2ZS0zZDsKfQoKLnBhZ2UucHJlbWl1bSAuYmVudG8tY2FyZDpob3ZlciB7CiAgdHJhbnNmb3JtOiB0cmFuc2xhdGVZKC0ycHgpIHRyYW5zbGF0ZVooMCk7Cn0KCi5jYXJkIHAgewogIG1hcmdpbjogMCAwIDhweDsKfQoKLmNhcmQgcDpsYXN0LWNoaWxkIHsKICBtYXJnaW4tYm90dG9tOiAwOwp9CgouY2FyZCArIC5jYXJkIHsKICBtYXJnaW4tdG9wOiAxMnB4Owp9Cgouc3RhZ2dlciA+ICogewogIG9wYWNpdHk6IDA7CiAgYW5pbWF0aW9uOiBmYWRlVXAgMC43cyBlYXNlIGZvcndhcmRzOwp9Ci5zdGFnZ2VyID4gKjpudGgtY2hpbGQoMSkgeyBhbmltYXRpb24tZGVsYXk6IDAuMDVzOyB9Ci5zdGFnZ2VyID4gKjpudGgtY2hpbGQoMikgeyBhbmltYXRpb24tZGVsYXk6IDAuMTJzOyB9Ci5zdGFnZ2VyID4gKjpudGgtY2hpbGQoMykgeyBhbmltYXRpb24tZGVsYXk6IDAuMThzOyB9Ci5zdGFnZ2VyID4gKjpudGgtY2hpbGQoNCkgeyBhbmltYXRpb24tZGVsYXk6IDAuMjRzOyB9CgouZmllbGQgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiA4cHg7Cn0KCi5ncmlkIHsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogMTZweDsKfQoKLmdyaWQudHdvIHsKICBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IHJlcGVhdChhdXRvLWZpdCwgbWlubWF4KDI0MHB4LCAxZnIpKTsKfQoKLmdyaWQudGhyZWUgewogIGdyaWQtdGVtcGxhdGUtY29sdW1uczogcmVwZWF0KGF1dG8tZml0LCBtaW5tYXgoMjAwcHgsIDFmcikpOwp9CgpsYWJlbCB7CiAgZm9udC13ZWlnaHQ6IDYwMDsKICBmb250LXNpemU6IDE0cHg7Cn0KCmlucHV0W3R5cGU9InRleHQiXSwKaW5wdXRbdHlwZT0ibnVtYmVyIl0sCmlucHV0W3R5cGU9InBhc3N3b3JkIl0sCnRleHRhcmVhIHsKICB3aWR0aDogMTAwJTsKICBwYWRkaW5nOiAxMnB4IDE0cHg7CiAgYm9yZGVyLXJhZGl1czogMTJweDsKICBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIGZvbnQtc2l6ZTogMTVweDsKICBmb250LWZhbWlseTogaW5oZXJpdDsKICBiYWNrZ3JvdW5kOiB2YXIoLS1jYXJkLTMpOwogIGNvbG9yOiB2YXIoLS1pbmspOwp9CgppbnB1dDpmb2N1cywKdGV4dGFyZWE6Zm9jdXMgewogIG91dGxpbmU6IDJweCBzb2xpZCByZ2JhKDY4LCAyMTUsIDE5NywgMC4zNSk7CiAgYm9yZGVyLWNvbG9yOiB2YXIoLS1hY2NlbnQpOwp9Cgoubm90ZSB7CiAgZm9udC1zaXplOiAxM3B4OwogIGNvbG9yOiB2YXIoLS1tdXRlZCk7CiAgbWFyZ2luOiA2cHggMCAwOwp9CgouYWN0aW9ucyB7CiAgZGlzcGxheTogZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGdhcDogMTJweDsKICBmbGV4LXdyYXA6IHdyYXA7CiAgbWFyZ2luLXRvcDogOHB4Owp9CgouZmFiIHsKICBwb3NpdGlvbjogZml4ZWQ7CiAgcmlnaHQ6IDI4cHg7CiAgYm90dG9tOiAyOHB4OwogIHotaW5kZXg6IDUwOwogIGJvcmRlcjogbm9uZTsKICBib3JkZXItcmFkaXVzOiA5OTlweDsKICBwYWRkaW5nOiAxNHB4IDE4cHg7CiAgZm9udC1zaXplOiAxM3B4OwogIGZvbnQtd2VpZ2h0OiA3MDA7CiAgY3Vyc29yOiBwb2ludGVyOwogIGNvbG9yOiAjMGIxMjIwOwogIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCgxMzVkZWcsIHZhcigtLWFjY2VudC0zKSwgdmFyKC0tYWNjZW50KSk7CiAgYm94LXNoYWRvdzogMCAxOHB4IDMycHggcmdiYSgyLCA2LCAyMywgMC41NSk7Cn0KCi5mYWI6aG92ZXIgewogIHRyYW5zZm9ybTogdHJhbnNsYXRlWSgtMnB4KTsKfQoKLmJ0biB7CiAgYm9yZGVyOiBub25lOwogIGJvcmRlci1yYWRpdXM6IDk5OXB4OwogIHBhZGRpbmc6IDEycHggMjBweDsKICBmb250LXNpemU6IDE1cHg7CiAgZm9udC13ZWlnaHQ6IDYwMDsKICBjdXJzb3I6IHBvaW50ZXI7CiAgY29sb3I6ICNmZmY7CiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDEzNWRlZywgdmFyKC0tYWNjZW50KSwgIzFlYTZhMCk7CiAgYm94LXNoYWRvdzogMCAxMnB4IDI0cHggcmdiYSg2OCwgMjE1LCAxOTcsIDAuMjUpOwp9CgouYnRuLXNlY29uZGFyeSB7CiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDEzNWRlZywgdmFyKC0tYWNjZW50LTIpLCAjZjBhMDdhKTsKfQoKLmJ0bi1naG9zdCB7CiAgYmFja2dyb3VuZDogdHJhbnNwYXJlbnQ7CiAgYm9yZGVyOiAxcHggc29saWQgcmdiYSgxNDgsIDE2MywgMTg0LCAwLjM1KTsKICBjb2xvcjogI2Q4ZTJlZjsKICBib3gtc2hhZG93OiBub25lOwp9CgouYnRuOmRpc2FibGVkIHsKICBiYWNrZ3JvdW5kOiAjOWFhN2I0OwogIGN1cnNvcjogbm90LWFsbG93ZWQ7CiAgYm94LXNoYWRvdzogbm9uZTsKfQoKLmxpbmstYnRuIHsKICBkaXNwbGF5OiBpbmxpbmUtZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGdhcDogOHB4OwogIGNvbG9yOiAjMGIxMjIwOwogIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCgxMzVkZWcsIHZhcigtLWFjY2VudC0zKSwgdmFyKC0tYWNjZW50LTIpKTsKICBwYWRkaW5nOiAxMHB4IDE4cHg7CiAgYm9yZGVyLXJhZGl1czogOTk5cHg7CiAgdGV4dC1kZWNvcmF0aW9uOiBub25lOwogIGZvbnQtd2VpZ2h0OiA2MDA7Cn0KCi5zdGF0dXMgewogIHBhZGRpbmc6IDEycHggMTRweDsKICBib3JkZXItcmFkaXVzOiAxMnB4OwogIGZvbnQtc2l6ZTogMTRweDsKICBiYWNrZ3JvdW5kOiByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMTIpOwogIG1hcmdpbjogMTBweCAwOwp9Ci5zdGF0dXMuZG9uZSB7IGJhY2tncm91bmQ6IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjE2KTsgY29sb3I6ICNiN2ZmZjM7IH0KLnN0YXR1cy5lcnJvciB7IGJhY2tncm91bmQ6IHJnYmEoMjU1LCAxMzgsIDEwMiwgMC4xOCk7IGNvbG9yOiAjZmZjNWIyOyB9CgoudGFibGUgewogIHdpZHRoOiAxMDAlOwogIGJvcmRlci1jb2xsYXBzZTogY29sbGFwc2U7CiAgZm9udC1zaXplOiAxM3B4Owp9Ci50YWJsZSB0aCwgLnRhYmxlIHRkIHsKICBib3JkZXItYm90dG9tOiAxcHggc29saWQgcmdiYSgxNDgsIDE2MywgMTg0LCAwLjIpOwogIHBhZGRpbmc6IDEwcHg7CiAgdGV4dC1hbGlnbjogbGVmdDsKICB2ZXJ0aWNhbC1hbGlnbjogdG9wOwogIG92ZXJmbG93LXdyYXA6IGFueXdoZXJlOwp9Ci50YWJsZSB0aCB7CiAgYmFja2dyb3VuZDogcmdiYSgxNDgsIDE2MywgMTg0LCAwLjEpOwogIHBvc2l0aW9uOiBzdGlja3k7CiAgdG9wOiAwOwp9Ci50YWJsZS1saW5rIHsKICBjb2xvcjogdmFyKC0tYWNjZW50KTsKICB0ZXh0LWRlY29yYXRpb246IG5vbmU7Cn0KLnRhYmxlLWxpbms6aG92ZXIgewogIHRleHQtZGVjb3JhdGlvbjogdW5kZXJsaW5lOwp9Ci50cnVuY2F0ZSB7CiAgbWF4LXdpZHRoOiAyODBweDsKICB3aGl0ZS1zcGFjZTogbm93cmFwOwogIG92ZXJmbG93OiBoaWRkZW47CiAgdGV4dC1vdmVyZmxvdzogZWxsaXBzaXM7Cn0KCi5wb3N0LXRleHQtY2VsbCB7CiAgZGlzcGxheTogZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGdhcDogOHB4Owp9CgoucG9zdC12aWV3LWJ0biB7CiAgYm9yZGVyOiAxcHggc29saWQgcmdiYSgxNDgsIDE2MywgMTg0LCAwLjM1KTsKICBiYWNrZ3JvdW5kOiByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMTIpOwogIGNvbG9yOiAjZDVkZWVhOwogIGJvcmRlci1yYWRpdXM6IDEwcHg7CiAgcGFkZGluZzogNnB4OwogIGN1cnNvcjogcG9pbnRlcjsKICBkaXNwbGF5OiBpbmxpbmUtZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGp1c3RpZnktY29udGVudDogY2VudGVyOwp9CgoucG9zdC12aWV3LWJ0biBzdmcgewogIHdpZHRoOiAxNnB4OwogIGhlaWdodDogMTZweDsKfQoKLnBvc3Qtdmlldy1idG46aG92ZXIgewogIGJvcmRlci1jb2xvcjogcmdiYSg2OCwgMjE1LCAxOTcsIDAuNik7CiAgY29sb3I6ICNiN2ZmZjM7Cn0KCi5wb3N0LW1vZGFsIHsKICBwb3NpdGlvbjogZml4ZWQ7CiAgaW5zZXQ6IDA7CiAgZGlzcGxheTogZ3JpZDsKICBwbGFjZS1pdGVtczogY2VudGVyOwogIG9wYWNpdHk6IDA7CiAgcG9pbnRlci1ldmVudHM6IG5vbmU7CiAgdHJhbnNpdGlvbjogb3BhY2l0eSAwLjJzIGVhc2U7CiAgei1pbmRleDogNTA7Cn0KCi5wb3N0LW1vZGFsLm9wZW4gewogIG9wYWNpdHk6IDE7CiAgcG9pbnRlci1ldmVudHM6IGF1dG87Cn0KCi5wb3N0LW1vZGFsLWJhY2tkcm9wIHsKICBwb3NpdGlvbjogYWJzb2x1dGU7CiAgaW5zZXQ6IDA7CiAgYmFja2dyb3VuZDogcmdiYSgyLCA2LCAyMywgMC43KTsKfQoKLnBvc3QtbW9kYWwtY2FyZCB7CiAgcG9zaXRpb246IHJlbGF0aXZlOwogIHdpZHRoOiBtaW4oNzIwcHgsIDkydncpOwogIG1heC1oZWlnaHQ6IDgwdmg7CiAgYmFja2dyb3VuZDogdmFyKC0tY2FyZC0yKTsKICBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1ib3JkZXItc3Ryb25nKTsKICBib3JkZXItcmFkaXVzOiAxNnB4OwogIHBhZGRpbmc6IDE2cHg7CiAgYm94LXNoYWRvdzogdmFyKC0tc2hhZG93LXN0cm9uZyk7CiAgZGlzcGxheTogZ3JpZDsKICBnYXA6IDEycHg7CiAgei1pbmRleDogMTsKfQoKLnRyYWNraW5nLW1vZGFsLWNhcmQgewogIHdpZHRoOiBtaW4oOTgwcHgsIDk0dncpOwp9CgoudHJhY2tpbmctc3RhdHMtZ3JpZCB7CiAgZGlzcGxheTogZ3JpZDsKICBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IHJlcGVhdCg0LCBtaW5tYXgoMCwgMWZyKSk7CiAgZ2FwOiAxMnB4Owp9CgoudHJhY2tpbmctaGlnaGxpZ2h0IHsKICBkaXNwbGF5OiBmbGV4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuOwogIGdhcDogMTJweDsKICBwYWRkaW5nOiAxMnB4IDE0cHg7CiAgYm9yZGVyOiAxcHggc29saWQgdmFyKC0tYm9yZGVyKTsKICBib3JkZXItcmFkaXVzOiAxNHB4OwogIGJhY2tncm91bmQ6IHZhcigtLWNhcmQtMyk7Cn0KCi50cmFja2luZy10YWJsZS13cmFwIHsKICBtYXgtaGVpZ2h0OiA0OHZoOwogIG92ZXJmbG93OiBhdXRvOwogIGJvcmRlcjogMXB4IHNvbGlkIHZhcigtLWJvcmRlcik7CiAgYm9yZGVyLXJhZGl1czogMTRweDsKfQoKLnBvc3QtbW9kYWwtaGVhZCB7CiAgZGlzcGxheTogZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjsKICBnYXA6IDEycHg7Cn0KCi5wb3N0LW1vZGFsLWNsb3NlIHsKICBib3JkZXI6IDFweCBzb2xpZCByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMyk7CiAgYmFja2dyb3VuZDogdHJhbnNwYXJlbnQ7CiAgY29sb3I6ICNjN2QyZGY7CiAgYm9yZGVyLXJhZGl1czogMTBweDsKICBwYWRkaW5nOiA2cHggMTBweDsKICBjdXJzb3I6IHBvaW50ZXI7Cn0KCi5wb3N0LW1vZGFsLWJvZHkgewogIGNvbG9yOiB2YXIoLS1pbmspOwogIGZvbnQtc2l6ZTogMTRweDsKICBsaW5lLWhlaWdodDogMS42OwogIG92ZXJmbG93OiBhdXRvOwogIHdoaXRlLXNwYWNlOiBwcmUtd3JhcDsKfQoKLmxpbmUtcmV2aWV3IHsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogOHB4OwogIG1hcmdpbi10b3A6IDEycHg7Cn0KCi5saW5lIHsKICBwYWRkaW5nOiAxMHB4IDEycHg7CiAgYm9yZGVyLXJhZGl1czogMTBweDsKICBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIGJhY2tncm91bmQ6IHZhcigtLWNhcmQtMik7Cn0KCi5saW5lLmdvb2QgewogIGJvcmRlci1jb2xvcjogcmdiYSg2OCwgMjE1LCAxOTcsIDAuNCk7CiAgYmFja2dyb3VuZDogcmdiYSg2OCwgMjE1LCAxOTcsIDAuMTIpOwp9CgoubGluZS5uZWVkcyB7CiAgYm9yZGVyLWNvbG9yOiByZ2JhKDI1NSwgMTM4LCAxMDIsIDAuNDUpOwogIGJhY2tncm91bmQ6IHJnYmEoMjU1LCAxMzgsIDEwMiwgMC4xMik7Cn0KCi5saW5lIC5tZXRhIHsKICBmb250LXNpemU6IDEycHg7CiAgY29sb3I6IHZhcigtLW11dGVkKTsKfQoKLnRvb2xiYXIgewogIGRpc3BsYXk6IGZsZXg7CiAgZ2FwOiAxMnB4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAgbWFyZ2luOiAxMnB4IDA7Cn0KLnBhZ2VyIHsKICBtYXJnaW4tbGVmdDogYXV0bzsKICBkaXNwbGF5OiBmbGV4OwogIGdhcDogOHB4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAgZmxleC13cmFwOiB3cmFwOwp9CgouZmlsdGVyLWJhciB7CiAgZGlzcGxheTogZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjsKICBnYXA6IDEycHg7CiAgZmxleC13cmFwOiB3cmFwOwogIG1hcmdpbjogMTJweCAwOwp9CgouZmlsdGVyLWlucHV0IHsKICBmbGV4OiAxIDEgMjgwcHg7CiAgcGFkZGluZzogMTBweCAxMnB4OwogIGJvcmRlci1yYWRpdXM6IDEycHg7CiAgYm9yZGVyOiAxcHggc29saWQgdmFyKC0tYm9yZGVyKTsKICBiYWNrZ3JvdW5kOiB2YXIoLS1jYXJkLTMpOwogIGNvbG9yOiB2YXIoLS1pbmspOwogIGZvbnQtc2l6ZTogMTRweDsKfQoKLm1ldHJpY3MgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiByZXBlYXQoYXV0by1maXQsIG1pbm1heCgyMjBweCwgMWZyKSk7CiAgZ2FwOiAxNnB4Owp9CgoubWV0cmljLWNhcmQgewogIGJhY2tncm91bmQ6IHZhcigtLWNhcmQpOwogIGJvcmRlci1yYWRpdXM6IDE2cHg7CiAgcGFkZGluZzogMThweDsKICBib3gtc2hhZG93OiB2YXIoLS1zaGFkb3cpOwp9CgoubWV0cmljLWNhcmQtaGVhZCB7CiAgZGlzcGxheTogZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjsKICBnYXA6IDEycHg7Cn0KCi5tZXRyaWMtb3Blbi1pY29uIHsKICB3aWR0aDogMjhweDsKICBoZWlnaHQ6IDI4cHg7CiAgYm9yZGVyLXJhZGl1czogOTk5cHg7CiAgZGlzcGxheTogaW5saW5lLWZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsKICBiYWNrZ3JvdW5kOiByZ2JhKDY4LCAyMTUsIDE5NywgMC4xNCk7CiAgYm9yZGVyOiAxcHggc29saWQgcmdiYSg2OCwgMjE1LCAxOTcsIDAuMjgpOwogIGNvbG9yOiAjYjdmZmYzOwogIGZsZXg6IDAgMCBhdXRvOwogIHRyYW5zaXRpb246IHRyYW5zZm9ybSAwLjE4cyBlYXNlLCBiYWNrZ3JvdW5kIDAuMThzIGVhc2UsIGJvcmRlci1jb2xvciAwLjE4cyBlYXNlOwp9CgoubWV0cmljLW9wZW4taWNvbiBzdmcgewogIHdpZHRoOiAxNHB4OwogIGhlaWdodDogMTRweDsKfQoKLm1ldHJpYy1jYXJkLWJ1dHRvbiB7CiAgYm9yZGVyOiAxcHggc29saWQgdmFyKC0tYm9yZGVyKTsKICBjb2xvcjogaW5oZXJpdDsKICB0ZXh0LWFsaWduOiBsZWZ0OwogIGZvbnQ6IGluaGVyaXQ7CiAgY3Vyc29yOiBwb2ludGVyOwogIHRyYW5zaXRpb246IHRyYW5zZm9ybSAwLjE4cyBlYXNlLCBib3JkZXItY29sb3IgMC4xOHMgZWFzZSwgYm94LXNoYWRvdyAwLjE4cyBlYXNlOwp9CgoubWV0cmljLWNhcmQtYnV0dG9uOmhvdmVyIHsKICB0cmFuc2Zvcm06IHRyYW5zbGF0ZVkoLTJweCk7CiAgYm9yZGVyLWNvbG9yOiByZ2JhKDY4LCAyMTUsIDE5NywgMC40NSk7CiAgYm94LXNoYWRvdzogdmFyKC0tc2hhZG93LXN0cm9uZyk7Cn0KCi5tZXRyaWMtY2FyZC1idXR0b246aG92ZXIgLm1ldHJpYy1vcGVuLWljb24gewogIHRyYW5zZm9ybTogdHJhbnNsYXRlKDFweCwgLTFweCk7CiAgYmFja2dyb3VuZDogcmdiYSg2OCwgMjE1LCAxOTcsIDAuMjIpOwogIGJvcmRlci1jb2xvcjogcmdiYSg2OCwgMjE1LCAxOTcsIDAuNDIpOwp9CgoubWV0cmljLWNhcmQtYnV0dG9uOmZvY3VzLXZpc2libGUgewogIG91dGxpbmU6IDJweCBzb2xpZCByZ2JhKDY4LCAyMTUsIDE5NywgMC40Mik7CiAgb3V0bGluZS1vZmZzZXQ6IDJweDsKfQoKLm1ldHJpYy12YWx1ZSB7CiAgZm9udC1zaXplOiAyOHB4OwogIGZvbnQtd2VpZ2h0OiA3MDA7Cn0KCi5jaGFydCB7CiAgbWFyZ2luLXRvcDogMTJweDsKICBiYWNrZ3JvdW5kOiByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMik7CiAgYm9yZGVyLXJhZGl1czogOTk5cHg7CiAgaGVpZ2h0OiAxMHB4OwogIG92ZXJmbG93OiBoaWRkZW47Cn0KCi5jaGFydC1iYXIgewogIGhlaWdodDogMTAwJTsKICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoOTBkZWcsIHZhcigtLWFjY2VudCksIHZhcigtLWFjY2VudC0yKSk7Cn0KCi5kYXNoYm9hcmQtZ3JpZCB7CiAgZGlzcGxheTogZ3JpZDsKICBnYXA6IDEycHg7CiAgYWxpZ24taXRlbXM6IHN0YXJ0OwogIGdyaWQtYXV0by1yb3dzOiBtaW5tYXgobWluLWNvbnRlbnQsIG1heC1jb250ZW50KTsKfQoKLmRhc2hib2FyZC1ncmlkLnR3byB7CiAgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiByZXBlYXQoMiwgbWlubWF4KDAsIDFmcikpOwp9CgouZGFzaGJvYXJkLWdyaWQgPiAuY2FyZCB7CiAgYWxpZ24tc2VsZjogc3RhcnQ7Cn0KCi5iZW50by1ncmlkIHsKICBkaXNwbGF5OiBncmlkOwogIGdyaWQtdGVtcGxhdGUtY29sdW1uczogcmVwZWF0KDEyLCBtaW5tYXgoMCwgMWZyKSk7CiAgZ2FwOiAxMnB4OwogIGFsaWduLWl0ZW1zOiBzdGFydDsKICBhbGlnbi1jb250ZW50OiBzdGFydDsKICBncmlkLWF1dG8tcm93czogbWlubWF4KG1pbi1jb250ZW50LCBtYXgtY29udGVudCk7CiAgZ3JpZC1hdXRvLWZsb3c6IHJvdzsKfQoKLmJlbnRvLWdyaWQgLmJlbnRvLWNhcmQgewogIGdyaWQtY29sdW1uOiBzcGFuIDY7CiAgYWxpZ24tc2VsZjogc3RhcnQ7CiAgaGVpZ2h0OiBhdXRvOwogIGRpc3BsYXk6IGZsZXg7CiAgZmxleC1kaXJlY3Rpb246IGNvbHVtbjsKICBnYXA6IDEwcHg7Cn0KCi5iZW50by10b3AtY2FyZCB7CiAgaGVpZ2h0OiBhdXRvOwp9CgouYmVudG8tZ3JpZCAuY2FyZCwKLmRhc2hib2FyZC1ncmlkIC5jYXJkIHsKICBtYXJnaW4tdG9wOiAwOwp9CgouYmVudG8tZ3JpZCAuc3Bhbi0xMiB7IGdyaWQtY29sdW1uOiBzcGFuIDEyOyB9Ci5iZW50by1ncmlkIC5zcGFuLTggeyBncmlkLWNvbHVtbjogc3BhbiA4OyB9Ci5iZW50by1ncmlkIC5zcGFuLTYgeyBncmlkLWNvbHVtbjogc3BhbiA2OyB9Ci5iZW50by1ncmlkIC5zcGFuLTQgeyBncmlkLWNvbHVtbjogc3BhbiA0OyB9CgouY2FyZC1oZWFkIHsKICBkaXNwbGF5OiBmbGV4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuOwogIGdhcDogMTBweDsKICBtYXJnaW4tYm90dG9tOiAxMnB4OwogIHBhZGRpbmctYm90dG9tOiA4cHg7CiAgYm9yZGVyLWJvdHRvbTogMXB4IHNvbGlkIHJnYmEoMTQ4LCAxNjMsIDE4NCwgMC4yKTsKICBmbGV4LXdyYXA6IHdyYXA7Cn0KCi5jYXJkLWhlYWQgaDMgewogIGZsZXg6IDEgMSBhdXRvOwp9CgouY2FyZC1oZWFkIC5waWxsIHsKICB3aGl0ZS1zcGFjZTogbm93cmFwOwp9CgoucGlsbCB7CiAgYmFja2dyb3VuZDogcmdiYSgxNDgsIDE2MywgMTg0LCAwLjE4KTsKICBjb2xvcjogI2U3ZWVmODsKICBmb250LXdlaWdodDogNjAwOwogIGZvbnQtc2l6ZTogMTJweDsKICBwYWRkaW5nOiA2cHggMTJweDsKICBib3JkZXItcmFkaXVzOiA5OTlweDsKfQoKLmF1dG8tc3VtbWFyeS1ncmlkIHsKICBtYXJnaW4tYm90dG9tOiAxOHB4Owp9CgouYXV0by1zdGF0LWNvbXBhY3QgewogIGZvbnQtc2l6ZTogMTZweDsKICBsaW5lLWhlaWdodDogMS4zNTsKfQoKLmF1dG8tZ3JpZCB7CiAgYWxpZ24taXRlbXM6IHN0YXJ0Owp9CgouYXV0by1zaWRlLWNhcmQgewogIG1pbi1oZWlnaHQ6IDEwMCU7Cn0KCi5hdXRvLWZvY3VzLWxpc3QgewogIG1hcmdpbi10b3A6IDE0cHg7Cn0KCi5jaGVjay1ncmlkIHsKICBkaXNwbGF5OiBncmlkOwogIGdyaWQtdGVtcGxhdGUtY29sdW1uczogcmVwZWF0KGF1dG8tZml0LCBtaW5tYXgoMTYwcHgsIDFmcikpOwogIGdhcDogMTBweDsKICBtYXJnaW4tdG9wOiAxNHB4Owp9CgouY2hlY2stcGlsbCB7CiAgZGlzcGxheTogZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGdhcDogMTBweDsKICBwYWRkaW5nOiAxMHB4IDEycHg7CiAgYm9yZGVyLXJhZGl1czogMTJweDsKICBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIGJhY2tncm91bmQ6IHZhcigtLWNhcmQtMyk7CiAgY29sb3I6IHZhcigtLWluayk7CiAgY3Vyc29yOiBwb2ludGVyOwogIGZvbnQtc2l6ZTogMTRweDsKICBmb250LXdlaWdodDogNjAwOwp9CgouY2hlY2stcGlsbCBpbnB1dCB7CiAgbWFyZ2luOiAwOwp9CgouYXV0by1jb250cm9sLWdyaWQgewogIG1hcmdpbi10b3A6IDA7Cn0KCi5hdXRvLWNvbmZpZy1ncmlkIHsKICBtYXJnaW4tdG9wOiAxNnB4Owp9CgouYXV0by1mb3JtLWZvb3RlciB7CiAgZGlzcGxheTogZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjsKICBnYXA6IDE2cHg7CiAgZmxleC13cmFwOiB3cmFwOwogIG1hcmdpbi10b3A6IDE4cHg7CiAgcGFkZGluZy10b3A6IDE2cHg7CiAgYm9yZGVyLXRvcDogMXB4IHNvbGlkIHJnYmEoMTQ4LCAxNjMsIDE4NCwgMC4xOCk7Cn0KCi5yZWZlcmVuY2UtdXJsLWxpYnJhcnkgewogIGdhcDogMTJweDsKfQoKLnJlZmVyZW5jZS1wYWNrLWFjdGlvbnMgewogIGRpc3BsYXk6IGZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBnYXA6IDEwcHg7CiAgZmxleC13cmFwOiB3cmFwOwp9CgoucmVmZXJlbmNlLXBhY2stYWN0aW9ucyAuYnRuIHsKICBwYWRkaW5nOiAxMHB4IDE2cHg7CiAgZm9udC1zaXplOiAxM3B4Owp9CgoucmVmZXJlbmNlLWdyb3VwLWdyaWQgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiAxMnB4OwogIGdyaWQtdGVtcGxhdGUtY29sdW1uczogcmVwZWF0KGF1dG8tZml0LCBtaW5tYXgoMjYwcHgsIDFmcikpOwp9CgoucmVmZXJlbmNlLWdyb3VwLWNhcmQgewogIHBhZGRpbmc6IDE0cHg7CiAgYm9yZGVyLXJhZGl1czogMTRweDsKICBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIGJhY2tncm91bmQ6IHZhcigtLWNhcmQtMyk7Cn0KCi5yZWZlcmVuY2UtZ3JvdXAtY2FyZFtvcGVuXSB7CiAgYm9yZGVyLWNvbG9yOiByZ2JhKDY4LCAyMTUsIDE5NywgMC4zMik7CiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDE2MGRlZywgcmdiYSg2OCwgMjE1LCAxOTcsIDAuMDgpLCByZ2JhKDExLCAyMCwgMzYsIDAuOTYpKTsKfQoKLnJlZmVyZW5jZS1ncm91cC1zdW1tYXJ5IHsKICBkaXNwbGF5OiBmbGV4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuOwogIGdhcDogMTBweDsKICBjdXJzb3I6IHBvaW50ZXI7CiAgZm9udC13ZWlnaHQ6IDcwMDsKICBsaXN0LXN0eWxlOiBub25lOwp9CgoucmVmZXJlbmNlLWdyb3VwLXN1bW1hcnk6Oi13ZWJraXQtZGV0YWlscy1tYXJrZXIgewogIGRpc3BsYXk6IG5vbmU7Cn0KCi5yZWZlcmVuY2UtdXJsLXRleHQgewogIG1hcmdpbi10b3A6IDEwcHg7CiAgbWluLWhlaWdodDogMTIwcHg7CiAgcmVzaXplOiB2ZXJ0aWNhbDsKICBmb250LXNpemU6IDEzcHg7CiAgbGluZS1oZWlnaHQ6IDEuNTU7Cn0KCi5wbGF0Zm9ybS1ncmlkIHsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogMTJweDsKfQoKLnBsYXRmb3JtLWNhcmQgewogIHBhZGRpbmc6IDE0cHg7CiAgYm9yZGVyLXJhZGl1czogMTRweDsKICBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIGJhY2tncm91bmQ6IHZhcigtLWNhcmQtMik7Cn0KCi5wbGF0Zm9ybS1taXNzaW5nIHsKICBvcGFjaXR5OiAwLjkyOwp9CgoucGxhdGZvcm0tY29ubmVjdGVkIHsKICBib3JkZXItY29sb3I6IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjQpOwogIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCgxNjBkZWcsIHJnYmEoNjgsIDIxNSwgMTk3LCAwLjEyKSwgcmdiYSgxOSwgMzYsIDU4LCAwLjk1KSk7Cn0KCi5wbGF0Zm9ybS1yZWFkeSB7CiAgYm9yZGVyLWNvbG9yOiByZ2JhKDI0NSwgMjEwLCAxMDYsIDAuMzgpOwogIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCgxNjBkZWcsIHJnYmEoMjQ1LCAyMTAsIDEwNiwgMC4xMiksIHJnYmEoMTksIDM2LCA1OCwgMC45NSkpOwp9CgoucGxhdGZvcm0tYXR0ZW50aW9uIHsKICBib3JkZXItY29sb3I6IHJnYmEoMjU1LCAxMzgsIDEwMiwgMC4zOCk7CiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDE2MGRlZywgcmdiYSgyNTUsIDEzOCwgMTAyLCAwLjEyKSwgcmdiYSgxOSwgMzYsIDU4LCAwLjk1KSk7Cn0KCi5wbGF0Zm9ybS10b3AgewogIGRpc3BsYXk6IGZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47CiAgZ2FwOiAxMHB4OwogIG1hcmdpbi1ib3R0b206IDEwcHg7CiAgZmxleC13cmFwOiB3cmFwOwp9CgoucGxhdGZvcm0tdmFsdWUgewogIGZvbnQtc2l6ZTogMTVweDsKICBmb250LXdlaWdodDogNzAwOwogIGNvbG9yOiAjZWVmNWZmOwogIG92ZXJmbG93LXdyYXA6IGFueXdoZXJlOwp9Cgouc3RhdHVzLXBpbGwgewogIGRpc3BsYXk6IGlubGluZS1mbGV4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAganVzdGlmeS1jb250ZW50OiBjZW50ZXI7CiAgcGFkZGluZzogNHB4IDEwcHg7CiAgYm9yZGVyLXJhZGl1czogOTk5cHg7CiAgZm9udC1zaXplOiAxMXB4OwogIGZvbnQtd2VpZ2h0OiA3MDA7CiAgdGV4dC10cmFuc2Zvcm06IGNhcGl0YWxpemU7CiAgbGV0dGVyLXNwYWNpbmc6IDAuMnB4OwogIHdoaXRlLXNwYWNlOiBub3dyYXA7Cn0KCi5zdGF0dXMtY29ubmVjdGVkIHsKICBiYWNrZ3JvdW5kOiByZ2JhKDY4LCAyMTUsIDE5NywgMC4xOCk7CiAgY29sb3I6ICNiN2ZmZjM7Cn0KCi5zdGF0dXMtcXVldWVkIHsKICBiYWNrZ3JvdW5kOiByZ2JhKDY4LCAyMTUsIDE5NywgMC4xOCk7CiAgY29sb3I6ICNiN2ZmZjM7Cn0KCi5zdGF0dXMtcmVhZHkgewogIGJhY2tncm91bmQ6IHJnYmEoMjQ1LCAyMTAsIDEwNiwgMC4xOCk7CiAgY29sb3I6ICNmYmU3YTg7Cn0KCi5zdGF0dXMtYXR0ZW50aW9uIHsKICBiYWNrZ3JvdW5kOiByZ2JhKDI1NSwgMTM4LCAxMDIsIDAuMTgpOwogIGNvbG9yOiAjZmZkMGMxOwp9Cgouc3RhdHVzLW1pc3NpbmcgewogIGJhY2tncm91bmQ6IHJnYmEoMTQ4LCAxNjMsIDE4NCwgMC4xOCk7CiAgY29sb3I6ICNkNGRlZWE7Cn0KCi5oaXN0b3J5LWxpc3QgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiAxMnB4Owp9CgouaGlzdG9yeS1pdGVtIHsKICBwYWRkaW5nOiAxNHB4OwogIGJvcmRlci1yYWRpdXM6IDE0cHg7CiAgYm9yZGVyOiAxcHggc29saWQgdmFyKC0tYm9yZGVyKTsKICBiYWNrZ3JvdW5kOiB2YXIoLS1jYXJkLTIpOwp9CgouaGlzdG9yeS1tYWluIHsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogNHB4Owp9CgouaGlzdG9yeS1zdW1tYXJ5IHsKICBmb250LXNpemU6IDE1cHg7CiAgZm9udC13ZWlnaHQ6IDcwMDsKICBjb2xvcjogI2VlZjVmZjsKfQoKLmhpc3RvcnktaXNzdWVzIHsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogOHB4OwogIG1hcmdpbi10b3A6IDEwcHg7Cn0KCi5oaXN0b3J5LWlzc3VlIHsKICBwYWRkaW5nOiAxMHB4IDEycHg7CiAgYm9yZGVyLXJhZGl1czogMTJweDsKICBiYWNrZ3JvdW5kOiByZ2JhKDI1NSwgMTM4LCAxMDIsIDAuMTIpOwogIGJvcmRlcjogMXB4IHNvbGlkIHJnYmEoMjU1LCAxMzgsIDEwMiwgMC4yMik7CiAgY29sb3I6ICNmZmQ5Y2U7CiAgZm9udC1zaXplOiAxM3B4Owp9Cgouc3RhdHMtZ3JpZCB7CiAgZGlzcGxheTogZ3JpZDsKICBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IHJlcGVhdChhdXRvLWZpdCwgbWlubWF4KDE2MHB4LCAxZnIpKTsKICBnYXA6IDEycHg7CiAgbWFyZ2luLXRvcDogMTZweDsKfQoKLnN0YXQgewogIGJhY2tncm91bmQ6IHZhcigtLWNhcmQtMik7CiAgYm9yZGVyOiAxcHggc29saWQgdmFyKC0tYm9yZGVyKTsKICBib3JkZXItcmFkaXVzOiAxMnB4OwogIHBhZGRpbmc6IDEycHg7Cn0KCi5zdGF0LWxhYmVsIHsKICBkaXNwbGF5OiBibG9jazsKICBmb250LXNpemU6IDEycHg7CiAgY29sb3I6IHZhcigtLW11dGVkKTsKfQoKLnN0YXQtdmFsdWUgewogIGZvbnQtc2l6ZTogMThweDsKICBmb250LXdlaWdodDogNzAwOwp9Cgouc3RhdHVzLWJhZGdlIHsKICBtYXJnaW4tdG9wOiA2cHg7CiAgZGlzcGxheTogaW5saW5lLWZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsKICBwYWRkaW5nOiAycHggOHB4OwogIGZvbnQtc2l6ZTogMTBweDsKICBmb250LXdlaWdodDogNzAwOwogIGJvcmRlci1yYWRpdXM6IDk5OXB4OwogIHRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7CiAgbGV0dGVyLXNwYWNpbmc6IDAuNXB4Owp9Cgouc3RhdHVzLWJhZGdlLm9wdGltYWwgewogIGJhY2tncm91bmQ6IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjE4KTsKICBjb2xvcjogI2I3ZmZmMzsKfQoKLnN0YXR1cy1iYWRnZS5zaG9ydCB7CiAgYmFja2dyb3VuZDogcmdiYSgyNTUsIDk5LCAxMjQsIDAuMik7CiAgY29sb3I6ICNmZmQwZDg7Cn0KCi5zdGF0dXMtYmFkZ2UubG9uZyB7CiAgYmFja2dyb3VuZDogcmdiYSgyNDUsIDIxMCwgMTA2LCAwLjE4KTsKICBjb2xvcjogI2ZiZTdhODsKfQoKLnJhZGFyIHsKICBkaXNwbGF5OiBncmlkOwogIHBsYWNlLWl0ZW1zOiBjZW50ZXI7CiAgbWluLWhlaWdodDogMjIwcHg7Cn0KCi5yYWRhciBzdmcgewogIHdpZHRoOiAxMDAlOwogIGhlaWdodDogMjIwcHg7Cn0KCi5yYWRhciBjYW52YXMgewogIHdpZHRoOiAxMDAlOwogIG1heC13aWR0aDogMzIwcHg7CiAgaGVpZ2h0OiAyNDBweDsKfQoKLmNoaXBzIHsKICBkaXNwbGF5OiBmbGV4OwogIGZsZXgtd3JhcDogd3JhcDsKICBnYXA6IDhweDsKICBtYXJnaW4tdG9wOiA4cHg7Cn0KCi5jaGlwIHsKICBiYWNrZ3JvdW5kOiByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMTYpOwogIGNvbG9yOiAjZTJlOWYzOwogIHBhZGRpbmc6IDZweCAxMnB4OwogIGJvcmRlci1yYWRpdXM6IDk5OXB4OwogIGZvbnQtc2l6ZTogMTJweDsKICBmb250LXdlaWdodDogNjAwOwogIG1heC13aWR0aDogMTAwJTsKICBvdmVyZmxvdy13cmFwOiBhbnl3aGVyZTsKfQoKLmNoaXAtdG9wIHsKICBiYWNrZ3JvdW5kOiByZ2JhKDY4LCAyMTUsIDE5NywgMC4xOCk7CiAgY29sb3I6ICNiN2ZmZjM7Cn0KCi5jaGlwLXJvbGUgewogIGJhY2tncm91bmQ6IHJnYmEoNTksIDEzMCwgMjQ2LCAwLjIyKTsKICBjb2xvcjogI2M3ZGNmZjsKfQoKLmNoaXAtbWlzc2luZyB7CiAgYmFja2dyb3VuZDogcmdiYSgyNTUsIDk5LCAxMjQsIDAuMik7CiAgY29sb3I6ICNmZmQwZDg7CiAgZGlzcGxheTogaW5saW5lLWZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBnYXA6IDZweDsKfQoKLmtleXdvcmQtYWN0aW9uIHsKICBib3JkZXI6IG5vbmU7CiAgY3Vyc29yOiBwb2ludGVyOwogIGZvbnQtZmFtaWx5OiBpbmhlcml0OwogIHRyYW5zaXRpb246IHRyYW5zZm9ybSAwLjJzIGVhc2UsIGJveC1zaGFkb3cgMC4ycyBlYXNlOwp9Cgoua2V5d29yZC1hY3Rpb246aG92ZXIgewogIHRyYW5zZm9ybTogdHJhbnNsYXRlWSgtMXB4KTsKICBib3gtc2hhZG93OiAwIDZweCAxNHB4IHJnYmEoMjU1LCA5OSwgMTI0LCAwLjI1KTsKfQoKLmNoaXAtaWNvbiB7CiAgd2lkdGg6IDE2cHg7CiAgaGVpZ2h0OiAxNnB4OwogIGRpc3BsYXk6IGlubGluZS1mbGV4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAganVzdGlmeS1jb250ZW50OiBjZW50ZXI7CiAgYm9yZGVyLXJhZGl1czogOTk5cHg7CiAgYmFja2dyb3VuZDogcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjE2KTsKICBmb250LXNpemU6IDExcHg7CiAgZm9udC13ZWlnaHQ6IDcwMDsKfQoKLmNoaXAuc29mdCB7CiAgYmFja2dyb3VuZDogcmdiYSgyNDUsIDIxMCwgMTA2LCAwLjE4KTsKICBjb2xvcjogI2ZiZTdhODsKfQoKLmNoaXAud2FybiB7CiAgYmFja2dyb3VuZDogcmdiYSgyNTUsIDEzOCwgMTAyLCAwLjE4KTsKICBjb2xvcjogI2ZmZDBjMTsKfQoKLmZvY3VzLWxpc3QgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiAxMnB4Owp9CgouZm9jdXMtaXRlbSB7CiAgYmFja2dyb3VuZDogdmFyKC0tY2FyZC0yKTsKICBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIGJvcmRlci1yYWRpdXM6IDEycHg7CiAgcGFkZGluZzogMTJweDsKfQoKLmFjY29yZGlvbi1pdGVtIHsKICBvdmVyZmxvdzogaGlkZGVuOwp9CgouYWNjb3JkaW9uLXN1bW1hcnkgewogIGxpc3Qtc3R5bGU6IG5vbmU7CiAgY3Vyc29yOiBwb2ludGVyOwogIGRpc3BsYXk6IGZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47Cn0KCi5hY2NvcmRpb24tc3VtbWFyeTo6LXdlYmtpdC1kZXRhaWxzLW1hcmtlciB7CiAgZGlzcGxheTogbm9uZTsKfQoKLmFjY29yZGlvbi1zdW1tYXJ5OjphZnRlciB7CiAgY29udGVudDogIisiOwogIGZvbnQtd2VpZ2h0OiA3MDA7CiAgY29sb3I6ICNjN2QyZGY7CiAgbWFyZ2luLWxlZnQ6IGF1dG87Cn0KCmRldGFpbHNbb3Blbl0gPiAuYWNjb3JkaW9uLXN1bW1hcnk6OmFmdGVyIHsKICBjb250ZW50OiAi4oCTIjsKfQoKLmFjY29yZGlvbi1ib2R5IHsKICBtYXJnaW4tdG9wOiA4cHg7CiAgZGlzcGxheTogZ3JpZDsKICBnYXA6IDhweDsKfQoKLmZvY3VzLXRpdGxlIHsKICBkaXNwbGF5OiBmbGV4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuOwogIG1hcmdpbi1ib3R0b206IDZweDsKICBnYXA6IDhweDsKICBmbGV4LXdyYXA6IHdyYXA7Cn0KCi5wcmlvcml0eSB7CiAgZm9udC1zaXplOiAxMnB4OwogIGZvbnQtd2VpZ2h0OiA3MDA7CiAgcGFkZGluZzogNHB4IDEwcHg7CiAgYm9yZGVyLXJhZGl1czogOTk5cHg7CiAgYmFja2dyb3VuZDogcmdiYSgxNDgsIDE2MywgMTg0LCAwLjE4KTsKICBjb2xvcjogI2RmZTdmMTsKfQoKLnByaW9yaXR5LmhpZ2ggewogIGJhY2tncm91bmQ6IHJnYmEoMjU1LCAxMzgsIDEwMiwgMC4yKTsKICBjb2xvcjogI2ZmYzNiMzsKfQoKLnByaW9yaXR5Lm1lZGl1bSB7CiAgYmFja2dyb3VuZDogcmdiYSgyNDUsIDIxMCwgMTA2LCAwLjE4KTsKICBjb2xvcjogI2ZmZTNhMDsKfQoKLnByaW9yaXR5LmxvdyB7CiAgYmFja2dyb3VuZDogcmdiYSg2OCwgMjE1LCAxOTcsIDAuMTYpOwogIGNvbG9yOiAjYjhmZmYwOwp9Cgouc2NvcmUtZ3JpZCB7CiAgZGlzcGxheTogZ3JpZDsKICBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IHJlcGVhdChhdXRvLWZpdCwgbWlubWF4KDE4MHB4LCAxZnIpKTsKICBnYXA6IDEycHg7Cn0KCi5zY29yZS1pdGVtIHsKICBiYWNrZ3JvdW5kOiB2YXIoLS1jYXJkLTIpOwogIGJvcmRlcjogMXB4IHNvbGlkIHZhcigtLWJvcmRlcik7CiAgYm9yZGVyLXJhZGl1czogMTJweDsKICBwYWRkaW5nOiAxMnB4Owp9Cgouc2NvcmUtdGl0bGUgewogIGZvbnQtd2VpZ2h0OiA2MDA7CiAgZm9udC1zaXplOiAxM3B4Owp9Cgouc2NvcmUtdmFsdWUgewogIGZvbnQtc2l6ZTogMThweDsKICBmb250LXdlaWdodDogNzAwOwogIG1hcmdpbjogNHB4IDAgOHB4Owp9Cgouc2NvcmUtYmFyIHsKICBoZWlnaHQ6IDhweDsKICBiYWNrZ3JvdW5kOiByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMik7CiAgYm9yZGVyLXJhZGl1czogOTk5cHg7CiAgb3ZlcmZsb3c6IGhpZGRlbjsKfQoKLnNjb3JlLWZpbGwgewogIGhlaWdodDogMTAwJTsKICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoOTBkZWcsIHZhcigtLWFjY2VudCksIHZhcigtLWFjY2VudC0yKSk7Cn0KCi5wcmVtaXVtIHsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogMTRweDsKfQoKLmhlcm8gewogIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCgxMzVkZWcsIHJnYmEoMTgsIDMwLCA0OCwgMC45OCksIHJnYmEoOCwgMTQsIDI0LCAwLjkyKSk7CiAgYm9yZGVyLXJhZGl1czogMjRweDsKICBwYWRkaW5nOiAxNHB4IDE2cHg7CiAgYm94LXNoYWRvdzoKICAgIDAgMjRweCA1OHB4IHJnYmEoMiwgNiwgMjMsIDAuNzUpLAogICAgMCA2cHggMTZweCByZ2JhKDIsIDYsIDIzLCAwLjM1KTsKICBib3JkZXI6IDFweCBzb2xpZCByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMjUpOwp9CgouaGVybyAuc3VidGl0bGUgewogIGNvbG9yOiAjYThiNmM2Owp9CgouaGVyby10b3AgewogIGRpc3BsYXk6IGZsZXg7CiAgYWxpZ24taXRlbXM6IGZsZXgtc3RhcnQ7CiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuOwogIGdhcDogMjBweDsKICBmbGV4LXdyYXA6IHdyYXA7Cn0KCi5oZXJvLXRvcCA+IGRpdjpmaXJzdC1jaGlsZCB7CiAgZmxleDogMSAxIDM2MHB4OwogIG1pbi13aWR0aDogMjQwcHg7Cn0KCi5leWVicm93IHsKICBmb250LXNpemU6IDExcHg7CiAgdGV4dC10cmFuc2Zvcm06IHVwcGVyY2FzZTsKICBsZXR0ZXItc3BhY2luZzogMS42cHg7CiAgY29sb3I6ICM5ZmIwYzM7CiAgZm9udC13ZWlnaHQ6IDcwMDsKICBtYXJnaW4tYm90dG9tOiA2cHg7Cn0KCi5oZXJvLWdyaWQgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiByZXBlYXQoMywgbWlubWF4KDAsIDFmcikpOwogIGdhcDogOHB4OwogIG1hcmdpbi10b3A6IDEwcHg7Cn0KCi5oZXJvLWNhcmQgewogIGJhY2tncm91bmQ6IHZhcigtLWNhcmQtMik7CiAgYm9yZGVyLXJhZGl1czogMTZweDsKICBwYWRkaW5nOiAxNnB4OwogIGJvcmRlcjogMXB4IHNvbGlkIHZhcigtLWJvcmRlcik7Cn0KCi5iZW5jaG1hcmsgewogIG1hcmdpbi10b3A6IDEycHg7CiAgZGlzcGxheTogZ3JpZDsKICBnYXA6IDEwcHg7Cn0KCi5iZW5jaG1hcmstcm93IHsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogNnB4Owp9CgouYmVuY2htYXJrLWxhYmVsIHsKICBmb250LXNpemU6IDEycHg7CiAgY29sb3I6IHZhcigtLW11dGVkKTsKfQoKLmJlbmNobWFyay10cmFjayB7CiAgcG9zaXRpb246IHJlbGF0aXZlOwogIGhlaWdodDogMTBweDsKICBiYWNrZ3JvdW5kOiByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMik7CiAgYm9yZGVyLXJhZGl1czogOTk5cHg7CiAgb3ZlcmZsb3c6IGhpZGRlbjsKfQoKLmJlbmNobWFyay1iYXIgewogIHBvc2l0aW9uOiBhYnNvbHV0ZTsKICBsZWZ0OiAwOwogIHRvcDogMDsKICBoZWlnaHQ6IDEwMCU7CiAgYm9yZGVyLXJhZGl1czogOTk5cHg7Cn0KCi5iZW5jaG1hcmstYmFyLmN1cnJlbnQgewogIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCg5MGRlZywgcmdiYSg2OCwgMjE1LCAxOTcsIDAuOCksIHJnYmEoNjgsIDIxNSwgMTk3LCAwLjQpKTsKICB6LWluZGV4OiAyOwp9CgouYmVuY2htYXJrLWJhci50YXJnZXQgewogIGJhY2tncm91bmQ6IGxpbmVhci1ncmFkaWVudCg5MGRlZywgcmdiYSgyNDUsIDIxMCwgMTA2LCAwLjY1KSwgcmdiYSgyNTUsIDEzOCwgMTAyLCAwLjU1KSk7CiAgei1pbmRleDogMTsKfQoKLmJlbmNobWFyay1tZXRhIHsKICBkaXNwbGF5OiBmbGV4OwogIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjsKICBmb250LXNpemU6IDExcHg7CiAgY29sb3I6ICNkNWRlZWE7Cn0KCi5iZW5jaG1hcmstdGFnIHsKICBjb2xvcjogI2ZiZTdhODsKfQoKLnRlbXBsYXRlLWdyaWQgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiAxMnB4OwogIGdyaWQtdGVtcGxhdGUtY29sdW1uczogcmVwZWF0KGF1dG8tZml0LCBtaW5tYXgoMjIwcHgsIDFmcikpOwogIG1hcmdpbi10b3A6IDEwcHg7Cn0KCi50ZW1wbGF0ZS1jYXJkIHsKICBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIGJhY2tncm91bmQ6IHZhcigtLWNhcmQtMik7CiAgYm9yZGVyLXJhZGl1czogMTRweDsKICBwYWRkaW5nOiAxMnB4OwogIGN1cnNvcjogcG9pbnRlcjsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogNnB4OwogIHRyYW5zaXRpb246IGJvcmRlci1jb2xvciAwLjJzIGVhc2UsIGJveC1zaGFkb3cgMC4ycyBlYXNlLCB0cmFuc2Zvcm0gMC4ycyBlYXNlOwp9CgoudGVtcGxhdGUtY2FyZCBpbnB1dCB7CiAgZGlzcGxheTogbm9uZTsKfQoKLnRlbXBsYXRlLWNhcmQuYWN0aXZlIHsKICBib3JkZXItY29sb3I6IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjYpOwogIGJveC1zaGFkb3c6IGluc2V0IDAgMCAwIDFweCByZ2JhKDY4LCAyMTUsIDE5NywgMC4zKTsKICB0cmFuc2Zvcm06IHRyYW5zbGF0ZVkoLTFweCk7Cn0KCi50ZW1wbGF0ZS10aXRsZSB7CiAgZm9udC13ZWlnaHQ6IDcwMDsKICBmb250LXNpemU6IDE0cHg7CiAgY29sb3I6ICNlN2VlZjg7Cn0KCi50b2dnbGUtbGluZSB7CiAgZGlzcGxheTogaW5saW5lLWZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBnYXA6IDhweDsKICBmb250LXNpemU6IDEzcHg7CiAgY29sb3I6ICNkOGUyZWY7Cn0KCi5wcmV2aWV3LWJsb2NrIHsKICBiYWNrZ3JvdW5kOiB2YXIoLS1jYXJkLTMpOwogIGJvcmRlcjogMXB4IHNvbGlkIHZhcigtLWJvcmRlcik7CiAgYm9yZGVyLXJhZGl1czogMTJweDsKICBwYWRkaW5nOiAxMnB4OwogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiAxMnB4Owp9CgoucHJldmlldy1zdWJqZWN0IHsKICBmb250LXdlaWdodDogNzAwOwogIGZvbnQtc2l6ZTogMTRweDsKICBjb2xvcjogI2U2ZWRmNzsKfQoKLnByZXZpZXctYm9keSB7CiAgbWFyZ2luOiAwOwogIHdoaXRlLXNwYWNlOiBwcmUtd3JhcDsKICBmb250LWZhbWlseTogIk1hbnJvcGUiLCAiU2Vnb2UgVUkiLCBzYW5zLXNlcmlmOwogIGZvbnQtc2l6ZTogMTNweDsKICBsaW5lLWhlaWdodDogMS42OwogIGNvbG9yOiAjZGZlN2YxOwp9Cgouc2NvcmUtd2lkZ2V0IHsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogMTJweDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGp1c3RpZnktaXRlbXM6IGNlbnRlcjsKfQoKLnNjb3JlLXdpZGdldC5jb21wYWN0IHsKICBqdXN0aWZ5LWl0ZW1zOiBzdGFydDsKICBhbGlnbi1pdGVtczogc3RhcnQ7CiAgd2lkdGg6IDEwMCU7Cn0KCi5zY29yZS1jYW52YXMtd3JhcCB7CiAgcG9zaXRpb246IHJlbGF0aXZlOwogIHdpZHRoOiAxNjBweDsKICBoZWlnaHQ6IDE2MHB4Owp9Cgouc2NvcmUtY2FudmFzLXdyYXAgY2FudmFzIHsKICB3aWR0aDogMTYwcHg7CiAgaGVpZ2h0OiAxNjBweDsKfQoKLnNjb3JlLWNlbnRlciB7CiAgcG9zaXRpb246IGFic29sdXRlOwogIGluc2V0OiAwOwogIGRpc3BsYXk6IGZsZXg7CiAgZmxleC1kaXJlY3Rpb246IGNvbHVtbjsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGp1c3RpZnktY29udGVudDogY2VudGVyOwogIHBvaW50ZXItZXZlbnRzOiBub25lOwogIGdhcDogMnB4Owp9Cgouc2NvcmUtc3BhcmtsaW5lIHsKICB3aWR0aDogMTYwcHg7Cn0KCi5zY29yZS1zcGFya2xpbmUgY2FudmFzIHsKICB3aWR0aDogMTAwJTsKICBoZWlnaHQ6IDU2cHg7Cn0KCi5wcm9maWxlLW1ldGEgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiA4cHg7CiAgbWFyZ2luLXRvcDogNnB4Owp9CgoubWV0YS1yb3cgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiAycHg7Cn0KCi5tZXRhLWxhYmVsIHsKICBmb250LXNpemU6IDExcHg7CiAgY29sb3I6IHZhcigtLW11dGVkKTsKICB0ZXh0LXRyYW5zZm9ybTogdXBwZXJjYXNlOwogIGxldHRlci1zcGFjaW5nOiAwLjZweDsKfQoKLm1ldGEtdmFsdWUgewogIGZvbnQtc2l6ZTogMTNweDsKICBjb2xvcjogI2UyZTlmMzsKfQoKLmRpZmYtY29udHJvbHMgewogIGRpc3BsYXk6IGZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47CiAgZ2FwOiAxMHB4Owp9CgouZGlmZi10b2dnbGUtYnRuIHsKICBib3JkZXI6IDFweCBzb2xpZCByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMyk7CiAgYmFja2dyb3VuZDogcmdiYSgxNDgsIDE2MywgMTg0LCAwLjE2KTsKICBjb2xvcjogI2U2ZWRmNzsKICBwYWRkaW5nOiA2cHggMTJweDsKICBib3JkZXItcmFkaXVzOiA5OTlweDsKICBmb250LXNpemU6IDEycHg7CiAgZm9udC13ZWlnaHQ6IDYwMDsKICBjdXJzb3I6IHBvaW50ZXI7Cn0KCi5kaWZmLWJsb2NrIHsKICBtYXJnaW4tdG9wOiAxMHB4OwogIHBhZGRpbmc6IDEycHg7CiAgYm9yZGVyLXJhZGl1czogMTJweDsKICBiYWNrZ3JvdW5kOiB2YXIoLS1jYXJkLTMpOwogIGJvcmRlcjogMXB4IHNvbGlkIHZhcigtLWJvcmRlcik7CiAgbGluZS1oZWlnaHQ6IDEuNjsKICBtaW4taGVpZ2h0OiA5NnB4Owp9CgouZGlmZi1hZGQgewogIGJhY2tncm91bmQ6IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjI1KTsKICBjb2xvcjogI2VhZmZmOTsKICBwYWRkaW5nOiAwIDRweDsKICBib3JkZXItcmFkaXVzOiA2cHg7Cn0KCi5kaWZmLWRlbCB7CiAgY29sb3I6ICNmZmI0YzE7CiAgdGV4dC1kZWNvcmF0aW9uOiBsaW5lLXRocm91Z2g7CiAgdGV4dC1kZWNvcmF0aW9uLXRoaWNrbmVzczogMnB4Owp9CgouaW5zaWdodHMtdGFicyB7CiAgZGlzcGxheTogZmxleDsKICBnYXA6IDhweDsKICBtYXJnaW4tdG9wOiAxNHB4OwogIGZsZXgtd3JhcDogd3JhcDsKfQoKLmluc2lnaHQtYnRuIHsKICBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIGJhY2tncm91bmQ6IHJnYmEoMTQ4LCAxNjMsIDE4NCwgMC4xNik7CiAgY29sb3I6ICNlNmVkZjc7CiAgcGFkZGluZzogNnB4IDEycHg7CiAgYm9yZGVyLXJhZGl1czogOTk5cHg7CiAgZm9udC1zaXplOiAxMnB4OwogIGZvbnQtd2VpZ2h0OiA2MDA7CiAgY3Vyc29yOiBwb2ludGVyOwp9CgouaW5zaWdodC1idG4uYWN0aXZlIHsKICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTM1ZGVnLCByZ2JhKDY4LCAyMTUsIDE5NywgMC4yNSksIHJnYmEoMjU1LCAxMzgsIDEwMiwgMC4yKSk7CiAgYm9yZGVyLWNvbG9yOiByZ2JhKDY4LCAyMTUsIDE5NywgMC41KTsKICBjb2xvcjogI2VhZmZmOTsKfQoKLmluc2lnaHRzLXBhbmVscyB7CiAgbWFyZ2luLXRvcDogMTBweDsKfQoKLmluc2lnaHQtcGFuZWwgewogIGRpc3BsYXk6IG5vbmU7Cn0KCi5pbnNpZ2h0LXBhbmVsLmFjdGl2ZSB7CiAgZGlzcGxheTogYmxvY2s7Cn0KCi5rZXl3b3JkLWFjdGlvbi5sb2FkaW5nIHsKICBvcGFjaXR5OiAwLjc7CiAgY3Vyc29yOiB3YWl0Owp9Cgoua3BpIHsKICBmb250LXNpemU6IDE1cHg7CiAgZm9udC13ZWlnaHQ6IDcwMDsKICBjb2xvcjogdmFyKC0taW5rKTsKICBtYXJnaW4tYm90dG9tOiA2cHg7CiAgb3ZlcmZsb3ctd3JhcDogYW55d2hlcmU7Cn0KCi5zY29yZS1yaW5nIHsKICB3aWR0aDogMTQwcHg7CiAgaGVpZ2h0OiAxNDBweDsKICBib3JkZXItcmFkaXVzOiA1MCU7CiAgYmFja2dyb3VuZDogY29uaWMtZ3JhZGllbnQodmFyKC0tYWNjZW50KSBjYWxjKHZhcigtLXNjb3JlKSAqIDElKSwgcmdiYSgxNDgsIDE2MywgMTg0LCAwLjIpIDApOwogIGRpc3BsYXk6IGdyaWQ7CiAgcGxhY2UtaXRlbXM6IGNlbnRlcjsKICBwb3NpdGlvbjogcmVsYXRpdmU7CiAgZmxleDogMCAwIGF1dG87Cn0KCi5zY29yZS1yaW5nOjphZnRlciB7CiAgY29udGVudDogIiI7CiAgcG9zaXRpb246IGFic29sdXRlOwogIGluc2V0OiAxMnB4OwogIGJhY2tncm91bmQ6ICMwYjEyMjA7CiAgYm9yZGVyLXJhZGl1czogNTAlOwogIGJvcmRlcjogMXB4IHNvbGlkIHJnYmEoMTQ4LCAxNjMsIDE4NCwgMC4yNSk7CiAgei1pbmRleDogMDsKfQoKLnNjb3JlLW51bWJlciwKLnNjb3JlLWxhYmVsIHsKICBwb3NpdGlvbjogcmVsYXRpdmU7CiAgei1pbmRleDogMTsKICB0ZXh0LWFsaWduOiBjZW50ZXI7Cn0KCi5zY29yZS1udW1iZXIgewogIGZvbnQtc2l6ZTogMzBweDsKICBmb250LXdlaWdodDogNzAwOwp9Cgouc2NvcmUtZGVsdGEgewogIGZvbnQtc2l6ZTogMTFweDsKICBmb250LXdlaWdodDogNjAwOwogIGNvbG9yOiAjZmJlN2E4OwogIG1hcmdpbi10b3A6IDRweDsKICB0ZXh0LWFsaWduOiBjZW50ZXI7Cn0KCi5zY29yZS1sYWJlbCB7CiAgZm9udC1zaXplOiAxMnB4OwogIGNvbG9yOiB2YXIoLS1tdXRlZCk7Cn0KCi5sZWFkIHsKICBmb250LXNpemU6IDE1cHg7CiAgbGluZS1oZWlnaHQ6IDEuNjsKICBjb2xvcjogI2RjZTVmMTsKICBvdmVyZmxvdy13cmFwOiBhbnl3aGVyZTsKfQoKLnBpbGwuYWkgewogIGJhY2tncm91bmQ6IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjE4KTsKICBjb2xvcjogI2I3ZmZmMzsKfQoKLnBpbGwubWluaSB7CiAgZm9udC1zaXplOiAxMXB4OwogIHBhZGRpbmc6IDRweCAxMHB4Owp9Cgoud2FybmluZyB7CiAgYm9yZGVyOiAxcHggZGFzaGVkIHJnYmEoMjU1LCAxMzgsIDEwMiwgMC41KTsKICBiYWNrZ3JvdW5kOiByZ2JhKDI1NSwgMTM4LCAxMDIsIDAuMTIpOwp9CgoucmV3cml0ZS1ncmlkIHsKICBkaXNwbGF5OiBncmlkOwogIGdyaWQtdGVtcGxhdGUtY29sdW1uczogcmVwZWF0KDIsIG1pbm1heCgwLCAxZnIpKTsKICBnYXA6IDEwcHg7CiAgYWxpZ24taXRlbXM6IHN0YXJ0OwogIGdyaWQtYXV0by1yb3dzOiBtaW5tYXgobWluLWNvbnRlbnQsIG1heC1jb250ZW50KTsKfQoKLnJld3JpdGUtZ3JpZCA+IC5yZXdyaXRlLWNhcmQgewogIGFsaWduLXNlbGY6IHN0YXJ0Owp9CgoucmV3cml0ZS1jYXJkIHsKICBiYWNrZ3JvdW5kOiB2YXIoLS1jYXJkLTIpOwogIGJvcmRlcjogMXB4IHNvbGlkIHZhcigtLWJvcmRlcik7CiAgYm9yZGVyLXJhZGl1czogMTZweDsKICBwYWRkaW5nOiAxNHB4OwogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiA4cHg7CiAgb3ZlcmZsb3ctd3JhcDogYW55d2hlcmU7CiAgYWxpZ24tY29udGVudDogc3RhcnQ7Cn0KCi5yZXdyaXRlLXRpdGxlIHsKICBmb250LXdlaWdodDogNzAwOwogIGZvbnQtc2l6ZTogMTRweDsKICBtYXJnaW4tYm90dG9tOiAycHg7Cn0KCi5yZXdyaXRlLXN0YWNrIHsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogMTBweDsKfQoKLnJld3JpdGUtcGFpciB7CiAgZGlzcGxheTogZ3JpZDsKICBnYXA6IDhweDsKICBwYWRkaW5nOiAxMHB4OwogIGJvcmRlcjogMXB4IHNvbGlkIHZhcigtLWJvcmRlcik7CiAgYm9yZGVyLXJhZGl1czogMTJweDsKICBiYWNrZ3JvdW5kOiB2YXIoLS1jYXJkLTMpOwp9CgoucmV3cml0ZS1wYWlyLmNvbXBhcmUtY2FyZHMgewogIGdyaWQtdGVtcGxhdGUtY29sdW1uczogcmVwZWF0KDIsIG1pbm1heCgwLCAxZnIpKTsKICBhbGlnbi1pdGVtczogc3RyZXRjaDsKfQoKLnJld3JpdGUtcGFpci5jb21wYXJlLWNhcmRzIC5ub3RlIHsKICBncmlkLWNvbHVtbjogMSAvIC0xOwp9CgoucmV3cml0ZS1wYWlyICsgLnJld3JpdGUtcGFpciB7CiAgbWFyZ2luLXRvcDogMTBweDsKfQoKLmJlZm9yZSwKLmFmdGVyIHsKICBib3JkZXItcmFkaXVzOiAxMnB4OwogIHBhZGRpbmc6IDEwcHg7CiAgYmFja2dyb3VuZDogcmdiYSgxNDgsIDE2MywgMTg0LCAwLjEyKTsKICBib3JkZXItbGVmdDogNHB4IHNvbGlkIHJnYmEoMTQ4LCAxNjMsIDE4NCwgMC4zNSk7CiAgZm9udC1zaXplOiAxM3B4OwogIHdoaXRlLXNwYWNlOiBwcmUtbGluZTsKICBvdmVyZmxvdy13cmFwOiBhbnl3aGVyZTsKICBsaW5lLWhlaWdodDogMS41Owp9CgouYWZ0ZXItaGVhZCB7CiAgZGlzcGxheTogZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjsKICBnYXA6IDEwcHg7CiAgbWFyZ2luLWJvdHRvbTogNHB4Owp9CgouY29weS1idG4gewogIGJvcmRlcjogMXB4IHNvbGlkIHJnYmEoNjgsIDIxNSwgMTk3LCAwLjQpOwogIGJhY2tncm91bmQ6IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjE2KTsKICBjb2xvcjogI2I3ZmZmMzsKICBib3JkZXItcmFkaXVzOiA5OTlweDsKICB3aWR0aDogMjhweDsKICBoZWlnaHQ6IDI4cHg7CiAgZGlzcGxheTogaW5saW5lLWZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsKICBwYWRkaW5nOiAwOwogIGZvbnQtc2l6ZTogMTFweDsKICBmb250LXdlaWdodDogNjAwOwogIGN1cnNvcjogcG9pbnRlcjsKICB0cmFuc2l0aW9uOiBiYWNrZ3JvdW5kIDAuMnMgZWFzZSwgdHJhbnNmb3JtIDAuMnMgZWFzZTsKfQoKLmNvcHktYnRuIC5pY29uIHsKICB3aWR0aDogMTZweDsKICBoZWlnaHQ6IDE2cHg7CiAgZGlzcGxheTogaW5saW5lLWZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsKfQoKLmNvcHktYnRuIHN2ZyB7CiAgd2lkdGg6IDE2cHg7CiAgaGVpZ2h0OiAxNnB4OwogIGZpbGw6IGN1cnJlbnRDb2xvcjsKfQoKLmNvcHktYnRuOmhvdmVyIHsKICBiYWNrZ3JvdW5kOiByZ2JhKDY4LCAyMTUsIDE5NywgMC4yOCk7CiAgdHJhbnNmb3JtOiB0cmFuc2xhdGVZKC0xcHgpOwp9CgouY29weS1idG4uY29waWVkIHsKICBiYWNrZ3JvdW5kOiByZ2JhKDI0NSwgMjEwLCAxMDYsIDAuMjIpOwogIGJvcmRlci1jb2xvcjogcmdiYSgyNDUsIDIxMCwgMTA2LCAwLjQpOwogIGNvbG9yOiAjZmJlN2E4Owp9CgouaGlnaGxpZ2h0LWFkZCB7CiAgYmFja2dyb3VuZDogcmdiYSg2OCwgMjE1LCAxOTcsIDAuMzUpOwogIGNvbG9yOiAjZWFmZmY5OwogIHBhZGRpbmc6IDAgNHB4OwogIGJvcmRlci1yYWRpdXM6IDZweDsKfQoKLmJlZm9yZSBwLAouYWZ0ZXIgcCB7CiAgbWFyZ2luOiAwOwp9CgouYWZ0ZXIgewogIGJhY2tncm91bmQ6IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjE0KTsKICBib3JkZXItbGVmdC1jb2xvcjogdmFyKC0tYWNjZW50KTsKfQoKLm1pbmktbGFiZWwgewogIGRpc3BsYXk6IGJsb2NrOwogIGZvbnQtc2l6ZTogMTFweDsKICB0ZXh0LXRyYW5zZm9ybTogdXBwZXJjYXNlOwogIGxldHRlci1zcGFjaW5nOiAxcHg7CiAgY29sb3I6ICM5ZmIwYzM7CiAgbWFyZ2luLWJvdHRvbTogNnB4OwogIGZvbnQtd2VpZ2h0OiA3MDA7Cn0KCi5jb21wYXJlLWdyaWQgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiByZXBlYXQoMiwgbWlubWF4KDAsIDFmcikpOwogIGdhcDogMTBweDsKICBhbGlnbi1pdGVtczogc3RhcnQ7CiAgZ3JpZC1hdXRvLXJvd3M6IG1pbm1heChtaW4tY29udGVudCwgbWF4LWNvbnRlbnQpOwp9CgouY29tcGFyZS1ncmlkID4gZGl2IHsKICBhbGlnbi1zZWxmOiBzdGFydDsKfQoKLmNvbXBhcmUtZ3JpZCA+IGRpdiB7CiAgYmFja2dyb3VuZDogdmFyKC0tY2FyZC0yKTsKICBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIGJvcmRlci1yYWRpdXM6IDEycHg7CiAgcGFkZGluZzogMTJweDsKfQoKLmNvbXBhcmUtZ3JpZCBoNCB7CiAgbWFyZ2luOiAwIDAgNnB4OwogIGZvbnQtc2l6ZTogMTRweDsKfQoKLmNvbXBhcmUtY2FyZHMgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiByZXBlYXQoMiwgbWlubWF4KDAsIDFmcikpOwogIGdhcDogMTJweDsKICBhbGlnbi1pdGVtczogc3RyZXRjaDsKfQoKLmNvbXBhcmUtY2FyZCB7CiAgYmFja2dyb3VuZDogdmFyKC0tY2FyZC0yKTsKICBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIGJvcmRlci1yYWRpdXM6IDE0cHg7CiAgcGFkZGluZzogMTJweDsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogOHB4OwogIG1pbi1oZWlnaHQ6IDEwMCU7Cn0KCi5jb21wYXJlLWNhcmQub3JpZ2luYWwgewogIGJvcmRlci1jb2xvcjogcmdiYSgyNTUsIDk5LCAxMjQsIDAuMzUpOwogIGJveC1zaGFkb3c6IGluc2V0IDAgMCAwIDFweCByZ2JhKDI1NSwgOTksIDEyNCwgMC4xMik7Cn0KCi5jb21wYXJlLWNhcmQuc3VnZ2VzdGVkIHsKICBib3JkZXItY29sb3I6IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjQ1KTsKICBib3gtc2hhZG93OiBpbnNldCAwIDAgMCAxcHggcmdiYSg2OCwgMjE1LCAxOTcsIDAuMTgpOwp9CgouY29tcGFyZS1oZWFkIHsKICBkaXNwbGF5OiBmbGV4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuOwogIGdhcDogOHB4Owp9CgouY29tcGFyZS1oZWFkIC5taW5pLWxhYmVsIHsKICBtYXJnaW4tYm90dG9tOiAwOwp9CgouZ2FwLWJveCB7CiAgbWFyZ2luLXRvcDogMTRweDsKICBwYWRkaW5nOiAxMnB4OwogIGJvcmRlci1yYWRpdXM6IDEycHg7CiAgYmFja2dyb3VuZDogcmdiYSgyNDUsIDIxMCwgMTA2LCAwLjE2KTsKICBjb2xvcjogI2ZmZTNhMDsKICBib3JkZXI6IDFweCBzb2xpZCByZ2JhKDI0NSwgMjEwLCAxMDYsIDAuMzUpOwp9CgouY2xlYW4tbGlzdCB7CiAgbGlzdC1zdHlsZTogbm9uZTsKICBwYWRkaW5nOiAwOwogIG1hcmdpbjogOHB4IDAgMDsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogNnB4Owp9CgouY2xlYW4tbGlzdCBsaSB7CiAgcGFkZGluZzogOHB4IDEycHg7CiAgcG9zaXRpb246IHJlbGF0aXZlOwogIG92ZXJmbG93LXdyYXA6IGFueXdoZXJlOwogIGxpbmUtaGVpZ2h0OiAxLjQ1OwogIGJhY2tncm91bmQ6IHZhcigtLWNhcmQtMyk7CiAgYm9yZGVyOiAxcHggc29saWQgdmFyKC0tYm9yZGVyKTsKICBib3JkZXItcmFkaXVzOiAxMHB4OwogIGJvcmRlci1sZWZ0OiAzcHggc29saWQgdmFyKC0tYWNjZW50KTsKfQoKLmNsZWFuLWxpc3QgbGk6OmJlZm9yZSB7CiAgY29udGVudDogbm9uZTsKfQoKLnRhZy1saXN0IHsKICBkaXNwbGF5OiBmbGV4OwogIGZsZXgtd3JhcDogd3JhcDsKICBnYXA6IDhweDsKICBtYXJnaW4tdG9wOiA2cHg7Cn0KCi50YWcgewogIGJhY2tncm91bmQ6IHJnYmEoMTQ4LCAxNjMsIDE4NCwgMC4xNik7CiAgY29sb3I6ICNlMmU5ZjM7CiAgcGFkZGluZzogNnB4IDEwcHg7CiAgYm9yZGVyLXJhZGl1czogOTk5cHg7CiAgZm9udC1zaXplOiAxMnB4OwogIGZvbnQtd2VpZ2h0OiA2MDA7CiAgbWF4LXdpZHRoOiAxMDAlOwogIG92ZXJmbG93LXdyYXA6IGFueXdoZXJlOwp9CgoudGFnLndhcm4gewogIGJhY2tncm91bmQ6IHJnYmEoMjU1LCAxMzgsIDEwMiwgMC4xOCk7CiAgY29sb3I6ICNmZmQwYzE7Cn0KCi5wYXRoIHsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogMTBweDsKfQoKLnBhdGgtc3RlcCB7CiAgcG9zaXRpb246IHJlbGF0aXZlOwogIHBhZGRpbmc6IDEycHggMTRweDsKICBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1ib3JkZXIpOwogIGJvcmRlci1sZWZ0OiAzcHggc29saWQgdmFyKC0tYWNjZW50KTsKICBib3JkZXItcmFkaXVzOiAxMnB4OwogIGJhY2tncm91bmQ6IHZhcigtLWNhcmQtMik7Cn0KCi5wYXRoLXN0ZXA6OmJlZm9yZSB7CiAgY29udGVudDogbm9uZTsKfQoKLnBhdGgtaGVhZCB7CiAgZGlzcGxheTogZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGdhcDogMTBweDsKICBmbGV4LXdyYXA6IHdyYXA7Cn0KCi5zdGF0cy1ncmlkLmNvbXBhY3QgewogIG1hcmdpbi10b3A6IDEycHg7Cn0KCi5zY2FuLWhpc3RvcnkgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiAxMnB4Owp9Cgouc2Nhbi1oaXN0b3J5LWl0ZW0gewogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiAxMnB4OwogIHBhZGRpbmc6IDE0cHggMTZweDsKICBib3JkZXItcmFkaXVzOiAxNHB4OwogIGJvcmRlcjogMXB4IHNvbGlkIHZhcigtLWJvcmRlcik7CiAgYmFja2dyb3VuZDogdmFyKC0tY2FyZC0yKTsKfQoKLnNjYW4taGlzdG9yeS1tYWluIHsKICBkaXNwbGF5OiBmbGV4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuOwogIGdhcDogMTJweDsKICBmbGV4LXdyYXA6IHdyYXA7Cn0KCi5zY2FuLWhpc3RvcnktbWFpbiA+IDpmaXJzdC1jaGlsZCB7CiAgbWluLXdpZHRoOiAwOwogIGZsZXg6IDEgMSAyODBweDsKfQoKLnNjYW4taGlzdG9yeS10aXRsZSB7CiAgZm9udC13ZWlnaHQ6IDcwMDsKICBmb250LXNpemU6IDE1cHg7CiAgY29sb3I6ICNlN2VlZjg7Cn0KCi5zY2FuLWhpc3RvcnktY29tcGFuaWVzIHsKICBtYXJnaW4tdG9wOiA0cHg7CiAgZm9udC1zaXplOiAxM3B4OwogIGNvbG9yOiB2YXIoLS1tdXRlZCk7CiAgbWF4LXdpZHRoOiA3NjBweDsKfQoKLnNjYW4taGlzdG9yeS1tZXRhIHsKICBkaXNwbGF5OiBmbGV4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAgZ2FwOiAxMHB4OwogIGZsZXgtd3JhcDogd3JhcDsKICBmb250LXNpemU6IDEycHg7CiAgY29sb3I6IHZhcigtLW11dGVkKTsKICBqdXN0aWZ5LWNvbnRlbnQ6IGZsZXgtZW5kOwp9Cgouc2Nhbi1vcGVuLWJ0biB7CiAgd2lkdGg6IDQycHg7CiAgaGVpZ2h0OiA0MnB4OwogIGJvcmRlcjogMXB4IHNvbGlkIHJnYmEoNjgsIDIxNSwgMTk3LCAwLjIyKTsKICBib3JkZXItcmFkaXVzOiAxMnB4OwogIGJhY2tncm91bmQ6IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjA4KTsKICBjb2xvcjogI2RjZmJmNzsKICBkaXNwbGF5OiBpbmxpbmUtZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGp1c3RpZnktY29udGVudDogY2VudGVyOwogIGN1cnNvcjogcG9pbnRlcjsKICB0cmFuc2l0aW9uOiB0cmFuc2Zvcm0gMC4xOHMgZWFzZSwgYm9yZGVyLWNvbG9yIDAuMThzIGVhc2UsIGJhY2tncm91bmQgMC4xOHMgZWFzZTsKfQoKLnNjYW4tb3Blbi1idG4gc3ZnIHsKICB3aWR0aDogMThweDsKICBoZWlnaHQ6IDE4cHg7Cn0KCi5zY2FuLW9wZW4tYnRuOmhvdmVyIHsKICB0cmFuc2Zvcm06IHRyYW5zbGF0ZVkoLTFweCk7CiAgYm9yZGVyLWNvbG9yOiByZ2JhKDY4LCAyMTUsIDE5NywgMC40NSk7CiAgYmFja2dyb3VuZDogcmdiYSg2OCwgMjE1LCAxOTcsIDAuMTYpOwp9Cgouc2Nhbi1oaXN0b3J5LWZpbGVzIHsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogMTBweDsKfQoKLnNjYW4tbW9kYWwtYm9keSB7CiAgZGlzcGxheTogZ3JpZDsKICBnYXA6IDEycHg7CiAgb3ZlcmZsb3c6IGF1dG87Cn0KCi5zY2FuLW1vZGFsLXN1bW1hcnkgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiA2cHg7CiAgcGFkZGluZzogMTJweCAxNHB4OwogIGJvcmRlci1yYWRpdXM6IDE0cHg7CiAgYm9yZGVyOiAxcHggc29saWQgcmdiYSgxNDgsIDE2MywgMTg0LCAwLjE4KTsKICBiYWNrZ3JvdW5kOiByZ2JhKDExLCAyMCwgMzYsIDAuNzIpOwp9Cgouc2Nhbi1tb2RhbC1zdW1tYXJ5LXRpdGxlIHsKICBmb250LXNpemU6IDE1cHg7CiAgZm9udC13ZWlnaHQ6IDcwMDsKICBjb2xvcjogI2VlZjVmZjsKfQoKLnNjYW4tbW9kYWwtc3VtbWFyeS1ub3RlIHsKICBmb250LXNpemU6IDEzcHg7CiAgY29sb3I6IHZhcigtLW11dGVkKTsKfQoKLnNjYW4tbW9kYWwtYWN0aW9ucyB7CiAgZGlzcGxheTogZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGdhcDogMTBweDsKICBmbGV4LXdyYXA6IHdyYXA7Cn0KCi5zY2FuLWZpbGUtcm93IHsKICBkaXNwbGF5OiBmbGV4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAganVzdGlmeS1jb250ZW50OiBzcGFjZS1iZXR3ZWVuOwogIGdhcDogMTJweDsKICBwYWRkaW5nOiAxMnB4IDE0cHg7CiAgYm9yZGVyLXJhZGl1czogMTJweDsKICBib3JkZXI6IDFweCBzb2xpZCByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMTgpOwogIGJhY2tncm91bmQ6IHJnYmEoMTEsIDIwLCAzNiwgMC43Mik7CiAgZmxleC13cmFwOiB3cmFwOwp9Cgouc2Nhbi1maWxlLW1ldGEgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiA0cHg7Cn0KCi5zY2FuLWZpbGUtbmFtZSB7CiAgZm9udC1zaXplOiAxNHB4OwogIGZvbnQtd2VpZ2h0OiA3MDA7CiAgY29sb3I6ICNlN2VlZjg7Cn0KCi5zY2FuLWZpbGUtc2l6ZSB7CiAgZm9udC1zaXplOiAxMnB4OwogIGNvbG9yOiB2YXIoLS1tdXRlZCk7Cn0KCi5zY2FuLWZpbGUtYWN0aW9ucyB7CiAgZGlzcGxheTogZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGdhcDogMTBweDsKICBmbGV4LXdyYXA6IHdyYXA7Cn0KCi5zY2FuLWZpbGUtbGluayB7CiAgZGlzcGxheTogaW5saW5lLWZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsKICBnYXA6IDhweDsKICBtaW4td2lkdGg6IDEyMHB4OwogIHBhZGRpbmc6IDEwcHggMTRweDsKICBib3JkZXItcmFkaXVzOiAxMnB4OwogIGJvcmRlcjogMXB4IHNvbGlkIHJnYmEoNjgsIDIxNSwgMTk3LCAwLjIyKTsKICBiYWNrZ3JvdW5kOiByZ2JhKDY4LCAyMTUsIDE5NywgMC4wOCk7CiAgY29sb3I6ICNkZmY3ZjQ7CiAgdGV4dC1kZWNvcmF0aW9uOiBub25lOwogIGZvbnQtc2l6ZTogMTNweDsKICB0cmFuc2l0aW9uOiB0cmFuc2Zvcm0gMC4xOHMgZWFzZSwgYm9yZGVyLWNvbG9yIDAuMThzIGVhc2UsIGJhY2tncm91bmQgMC4xOHMgZWFzZTsKfQoKLnNjYW4tZmlsZS1saW5rOmhvdmVyIHsKICB0cmFuc2Zvcm06IHRyYW5zbGF0ZVkoLTFweCk7CiAgYm9yZGVyLWNvbG9yOiByZ2JhKDY4LCAyMTUsIDE5NywgMC40KTsKICBiYWNrZ3JvdW5kOiByZ2JhKDY4LCAyMTUsIDE5NywgMC4xNCk7Cn0KCi5zY2FuLWZpbGUtbWFpbCB7CiAgZGlzcGxheTogaW5saW5lLWZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBqdXN0aWZ5LWNvbnRlbnQ6IGNlbnRlcjsKICBtaW4td2lkdGg6IDE0MHB4OwogIHBhZGRpbmc6IDEwcHggMTRweDsKICBib3JkZXItcmFkaXVzOiAxMnB4OwogIGJvcmRlcjogMXB4IHNvbGlkIHJnYmEoMjU1LCAxMzgsIDEwMiwgMC4yMik7CiAgYmFja2dyb3VuZDogcmdiYSgyNTUsIDEzOCwgMTAyLCAwLjA4KTsKICBjb2xvcjogI2ZmZDljZTsKICB0ZXh0LWRlY29yYXRpb246IG5vbmU7CiAgZm9udC1zaXplOiAxM3B4OwogIGZvbnQtd2VpZ2h0OiA2MDA7CiAgdHJhbnNpdGlvbjogdHJhbnNmb3JtIDAuMThzIGVhc2UsIGJvcmRlci1jb2xvciAwLjE4cyBlYXNlLCBiYWNrZ3JvdW5kIDAuMThzIGVhc2U7Cn0KCi5zY2FuLWZpbGUtbWFpbDpob3ZlciB7CiAgdHJhbnNmb3JtOiB0cmFuc2xhdGVZKC0xcHgpOwogIGJvcmRlci1jb2xvcjogcmdiYSgyNTUsIDEzOCwgMTAyLCAwLjQpOwogIGJhY2tncm91bmQ6IHJnYmEoMjU1LCAxMzgsIDEwMiwgMC4xNCk7Cn0KCkBtZWRpYSAobWF4LXdpZHRoOiA3MjBweCkgewogIC5zY2FuLWhpc3RvcnktbWFpbiB7CiAgICBhbGlnbi1pdGVtczogZmxleC1zdGFydDsKICB9CgogIC5zY2FuLWhpc3RvcnktbWV0YSB7CiAgICBqdXN0aWZ5LWNvbnRlbnQ6IGZsZXgtc3RhcnQ7CiAgfQp9Cgouc2lnbmF0dXJlIHsKICBwb3NpdGlvbjogZml4ZWQ7CiAgcmlnaHQ6IDI0cHg7CiAgYm90dG9tOiAxOHB4OwogIG1hcmdpbjogMDsKICBjb2xvcjogIzlmYjBjMzsKICBmb250LXNpemU6IDEycHg7CiAgdGV4dC1hbGlnbjogcmlnaHQ7CiAgbGluZS1oZWlnaHQ6IDEuNDsKICB6LWluZGV4OiAxMDsKICBwb2ludGVyLWV2ZW50czogbm9uZTsKfQoKQGtleWZyYW1lcyBmYWRlVXAgewogIGZyb20geyBvcGFjaXR5OiAwOyB0cmFuc2Zvcm06IHRyYW5zbGF0ZVkoOHB4KTsgfQogIHRvIHsgb3BhY2l0eTogMTsgdHJhbnNmb3JtOiB0cmFuc2xhdGVZKDApOyB9Cn0KCkBwYWdlIHsKICBtYXJnaW46IDE0bW07Cn0KCkBtZWRpYSBwcmludCB7CiAgYm9keSB7CiAgICBiYWNrZ3JvdW5kOiAjZmZmZmZmICFpbXBvcnRhbnQ7CiAgICBjb2xvcjogIzExMTgyNyAhaW1wb3J0YW50OwogIH0KCiAgYm9keTo6YmVmb3JlLAogIC5zaWRlYmFyLAogIC5zaWduYXR1cmUsCiAgLnRvZ2dsZSwKICAuZmFiLAogIC5saS1wcmludC1oaWRlLAogIC5wb3N0LW1vZGFsIHsKICAgIGRpc3BsYXk6IG5vbmUgIWltcG9ydGFudDsKICB9CgogIC5sYXlvdXQgewogICAgZGlzcGxheTogYmxvY2sgIWltcG9ydGFudDsKICB9CgogIC5tYWluIHsKICAgIHBhZGRpbmc6IDAgIWltcG9ydGFudDsKICB9CgogIC5wYWdlLAogIC5saS1zaGVsbCB7CiAgICBtYXgtd2lkdGg6IG5vbmUgIWltcG9ydGFudDsKICAgIG1hcmdpbjogMCAhaW1wb3J0YW50OwogICAgcGFkZGluZzogMCAhaW1wb3J0YW50OwogICAgYmFja2dyb3VuZDogI2ZmZmZmZiAhaW1wb3J0YW50OwogICAgY29sb3I6ICMxMTE4MjcgIWltcG9ydGFudDsKICAgIGJvcmRlcjogbm9uZSAhaW1wb3J0YW50OwogICAgYm94LXNoYWRvdzogbm9uZSAhaW1wb3J0YW50OwogIH0KCiAgLmNhcmQsCiAgLmxpLWNhcmQsCiAgLmxpLWZvY3VzLWl0ZW0sCiAgLnN0YXQsCiAgLm1ldHJpYy1jYXJkIHsKICAgIGJhY2tncm91bmQ6ICNmZmZmZmYgIWltcG9ydGFudDsKICAgIGNvbG9yOiAjMTExODI3ICFpbXBvcnRhbnQ7CiAgICBib3gtc2hhZG93OiBub25lICFpbXBvcnRhbnQ7CiAgICBib3JkZXI6IDFweCBzb2xpZCAjZDFkNWRiICFpbXBvcnRhbnQ7CiAgICBicmVhay1pbnNpZGU6IGF2b2lkOwogICAgcGFnZS1icmVhay1pbnNpZGU6IGF2b2lkOwogIH0KCiAgLmhlYWRlciwKICAubGktaGVybywKICAubGktZ3JpZCwKICAuc2NvcmUtZ3JpZCwKICAuc3RhdHMtZ3JpZCwKICAudHJhY2tpbmctc3RhdHMtZ3JpZCB7CiAgICBicmVhay1pbnNpZGU6IGF2b2lkOwogICAgcGFnZS1icmVhay1pbnNpZGU6IGF2b2lkOwogIH0KCiAgLmljb24tYmFkZ2UsCiAgLmxpLXNjb3JlIHsKICAgIGJveC1zaGFkb3c6IG5vbmUgIWltcG9ydGFudDsKICB9CgogIGgxLCBoMiwgaDMsIGg0LAogIC5zdWJ0aXRsZSwKICAubm90ZSwKICAubGktbm90ZSwKICAubGktbXV0ZWQsCiAgLnN0YXQtbGFiZWwsCiAgLmxpLXN1YnRpdGxlLAogIC5saS1raWNrZXIsCiAgLm1ldHJpYy12YWx1ZSwKICAuc3RhdC12YWx1ZSwKICAubGktc2NvcmUtbnVtLAogIC5saS1zY29yZS1sYWJlbCB7CiAgICBjb2xvcjogIzExMTgyNyAhaW1wb3J0YW50OwogIH0KCiAgYSwKICAudGFibGUtbGluaywKICAubGktbGluayB7CiAgICBjb2xvcjogIzExMTgyNyAhaW1wb3J0YW50OwogICAgdGV4dC1kZWNvcmF0aW9uOiBub25lICFpbXBvcnRhbnQ7CiAgfQoKICAuYWN0aW9ucywKICAuYnRuLAogIC5idG4tZ2hvc3QsCiAgLmJ0bi1zZWNvbmRhcnksCiAgLmxpbmstYnRuLAogIC5saS1idG4sCiAgLmxpLWNvcHksCiAgLmNvcHktYnRuLAogIC5wb3N0LXZpZXctYnRuIHsKICAgIGRpc3BsYXk6IG5vbmUgIWltcG9ydGFudDsKICB9CgogIC5jaGFydCwKICAuc2NvcmUtYmFyLAogIC5saS1iYXItdHJhY2ssCiAgLmxpLWNoYXJ0IGNhbnZhcyB7CiAgICBib3JkZXI6IDFweCBzb2xpZCAjZDFkNWRiICFpbXBvcnRhbnQ7CiAgICBiYWNrZ3JvdW5kOiAjZjhmYWZjICFpbXBvcnRhbnQ7CiAgfQp9CgpAbWVkaWEgKG1heC13aWR0aDogOTAwcHgpIHsKICAubGF5b3V0IHsgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiAxZnI7IH0KICAuc2lkZWJhciB7IHBvc2l0aW9uOiByZWxhdGl2ZTsgaGVpZ2h0OiBhdXRvOyB9CiAgLmhlcm8tdG9wIHsgZmxleC1kaXJlY3Rpb246IGNvbHVtbjsgYWxpZ24taXRlbXM6IGZsZXgtc3RhcnQ7IH0KICAuc2NvcmUtcmluZyB7IHdpZHRoOiAxMjBweDsgaGVpZ2h0OiAxMjBweDsgfQogIC5zY29yZS1jYW52YXMtd3JhcCB7IHdpZHRoOiAxMzBweDsgaGVpZ2h0OiAxMzBweDsgfQogIC5zY29yZS1jYW52YXMtd3JhcCBjYW52YXMgeyB3aWR0aDogMTMwcHg7IGhlaWdodDogMTMwcHg7IH0KICAuc2NvcmUtc3BhcmtsaW5lIHsgd2lkdGg6IDEzMHB4OyB9CiAgLm1haW4geyBwYWRkaW5nOiAzMnB4IDE4cHggNjBweDsgfQogIC5zaWduYXR1cmUgeyBwb3NpdGlvbjogZml4ZWQ7IHJpZ2h0OiAxNnB4OyBib3R0b206IDE0cHg7IHRleHQtYWxpZ246IHJpZ2h0OyB9CiAgLmRhc2hib2FyZC1ncmlkLnR3byB7IGdyaWQtdGVtcGxhdGUtY29sdW1uczogMWZyOyB9CiAgLnJld3JpdGUtZ3JpZCB7IGdyaWQtdGVtcGxhdGUtY29sdW1uczogMWZyOyB9CiAgLmNvbXBhcmUtZ3JpZCB7IGdyaWQtdGVtcGxhdGUtY29sdW1uczogMWZyOyB9CiAgLmNvbXBhcmUtY2FyZHMgeyBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IDFmcjsgfQogIC5yZXdyaXRlLXBhaXIuY29tcGFyZS1jYXJkcyB7IGdyaWQtdGVtcGxhdGUtY29sdW1uczogMWZyOyB9CiAgLmhlcm8tZ3JpZCB7IGdyaWQtdGVtcGxhdGUtY29sdW1uczogMWZyOyB9CiAgLmJlbnRvLWdyaWQgeyBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IDFmcjsgfQogIC5iZW50by1ncmlkIC5iZW50by1jYXJkIHsgZ3JpZC1jb2x1bW46IHNwYW4gMTsgfQogIC5iZW50by10b3AtY2FyZCB7IG1pbi1oZWlnaHQ6IGF1dG87IH0KICAudHJhY2tpbmctc3RhdHMtZ3JpZCB7IGdyaWQtdGVtcGxhdGUtY29sdW1uczogcmVwZWF0KDIsIG1pbm1heCgwLCAxZnIpKTsgfQogIC50cmFja2luZy1oaWdobGlnaHQgeyBmbGV4LWRpcmVjdGlvbjogY29sdW1uOyBhbGlnbi1pdGVtczogZmxleC1zdGFydDsgfQp9CgpAbWVkaWEgKG1heC13aWR0aDogMTIwMHB4KSB7CiAgLmRhc2hib2FyZC1ncmlkLnR3byB7IGdyaWQtdGVtcGxhdGUtY29sdW1uczogMWZyOyB9CiAgLnJld3JpdGUtZ3JpZCB7IGdyaWQtdGVtcGxhdGUtY29sdW1uczogMWZyOyB9CiAgLmNvbXBhcmUtZ3JpZCB7IGdyaWQtdGVtcGxhdGUtY29sdW1uczogMWZyOyB9CiAgLmNvbXBhcmUtY2FyZHMgeyBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IDFmcjsgfQogIC5yZXdyaXRlLXBhaXIuY29tcGFyZS1jYXJkcyB7IGdyaWQtdGVtcGxhdGUtY29sdW1uczogMWZyOyB9CiAgLmJlbnRvLWdyaWQgeyBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IDFmcjsgfQogIC5iZW50by1ncmlkIC5iZW50by1jYXJkIHsgZ3JpZC1jb2x1bW46IHNwYW4gMTsgfQp9Cg==","mimetype":"text/css"},"linkedin.css":{"b64":"77u/QGltcG9ydCB1cmwoImh0dHBzOi8vZm9udHMuZ29vZ2xlYXBpcy5jb20vY3NzMj9mYW1pbHk9U3BhY2UrR3JvdGVzazp3Z2h0QDQwMDs1MDA7NjAwOzcwMCZmYW1pbHk9SUJNK1BsZXgrU2Fuczp3Z2h0QDQwMDs1MDA7NjAwJmRpc3BsYXk9c3dhcCIpOwoKLmxpLXNoZWxsIHsKICAtLWxpLWJnOiB2YXIoLS1iZy0yKTsKICAtLWxpLXBhbmVsOiB2YXIoLS1jYXJkKTsKICAtLWxpLWNhcmQ6IHZhcigtLWNhcmQtMik7CiAgLS1saS1pbms6IHZhcigtLWluayk7CiAgLS1saS1tdXRlZDogdmFyKC0tbXV0ZWQpOwogIC0tbGktYWNjZW50OiB2YXIoLS1hY2NlbnQpOwogIC0tbGktYWNjZW50LTI6IHZhcigtLWFjY2VudC0yKTsKICAtLWxpLWFjY2VudC0zOiB2YXIoLS1hY2NlbnQtMyk7CiAgLS1saS1saW5lOiB2YXIoLS1ib3JkZXIpOwogIC0tbGktc2hhZG93OiB2YXIoLS1zaGFkb3ctc3Ryb25nKTsKICBmb250LWZhbWlseTogIk1hbnJvcGUiLCAiU2Vnb2UgVUkiLCBzYW5zLXNlcmlmOwogIGNvbG9yOiB2YXIoLS1saS1pbmspOwogIGJhY2tncm91bmQ6CiAgICByYWRpYWwtZ3JhZGllbnQoOTAwcHggNTAwcHggYXQgMTUlIC0xMCUsIHJnYmEoMjQ1LCAyMTAsIDEwNiwgMC4xKSwgdHJhbnNwYXJlbnQgNjAlKSwKICAgIHJhZGlhbC1ncmFkaWVudCg4MDBweCA1MDBweCBhdCA5MCUgMTAlLCByZ2JhKDY4LCAyMTUsIDE5NywgMC4xMiksIHRyYW5zcGFyZW50IDU1JSksCiAgICBsaW5lYXItZ3JhZGllbnQoMTYwZGVnLCByZ2JhKDIwLCAzMiwgNTIsIDAuOTgpLCByZ2JhKDgsIDE0LCAyNCwgMC45NikpOwogIGJvcmRlcjogMXB4IHNvbGlkIHJnYmEoMTQ4LCAxNjMsIDE4NCwgMC4yNCk7CiAgYm9yZGVyLXJhZGl1czogMjBweDsKICBwYWRkaW5nOiAyNHB4OwogIGJveC1zaGFkb3c6IHZhcigtLWxpLXNoYWRvdyk7CiAgcG9zaXRpb246IHJlbGF0aXZlOwogIG92ZXJmbG93OiBoaWRkZW47CiAgbWF4LXdpZHRoOiAxMjAwcHg7CiAgbWFyZ2luOiAwIGF1dG87Cn0KCi5saS1zaGVsbDo6YmVmb3JlIHsKICBjb250ZW50OiAiIjsKICBwb3NpdGlvbjogYWJzb2x1dGU7CiAgaW5zZXQ6IDA7CiAgYmFja2dyb3VuZC1pbWFnZTogcmFkaWFsLWdyYWRpZW50KHJnYmEoMjU1LCAyNTUsIDI1NSwgMC4wNSkgMXB4LCB0cmFuc3BhcmVudCAxcHgpOwogIGJhY2tncm91bmQtc2l6ZTogMjZweCAyNnB4OwogIG9wYWNpdHk6IDAuMjU7CiAgcG9pbnRlci1ldmVudHM6IG5vbmU7Cn0KCi5saS1zaGVsbCA+ICogewogIHBvc2l0aW9uOiByZWxhdGl2ZTsKICB6LWluZGV4OiAxOwp9CgoubGktcGFnZSBoMSwKLmxpLWRldGFpbCBoMSwKLmxpLXBhZ2UgaDIsCi5saS1kZXRhaWwgaDIsCi5saS1wYWdlIGgzLAoubGktZGV0YWlsIGgzIHsKICBmb250LWZhbWlseTogIkZyYXVuY2VzIiwgIkdlb3JnaWEiLCBzZXJpZjsKfQoKLmxpLWhlcm8gewogIGRpc3BsYXk6IGZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBqdXN0aWZ5LWNvbnRlbnQ6IHNwYWNlLWJldHdlZW47CiAgZ2FwOiAyNHB4OwogIG1hcmdpbi1ib3R0b206IDI0cHg7Cn0KCi5saS1raWNrZXIgewogIGZvbnQtc2l6ZTogMTJweDsKICBsZXR0ZXItc3BhY2luZzogMC4xOGVtOwogIHRleHQtdHJhbnNmb3JtOiB1cHBlcmNhc2U7CiAgY29sb3I6IHZhcigtLWxpLW11dGVkKTsKICBtYXJnaW4tYm90dG9tOiA4cHg7Cn0KCi5saS1zdWJ0aXRsZSB7CiAgY29sb3I6IHZhcigtLWxpLW11dGVkKTsKICBtYXgtd2lkdGg6IDYwMHB4Owp9CgoubGktaGVyby1tZXRhIHsKICBkaXNwbGF5OiBmbGV4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7CiAgZ2FwOiAxMnB4Owp9CgoubGktcGlsbCB7CiAgZGlzcGxheTogaW5saW5lLWZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBnYXA6IDZweDsKICBwYWRkaW5nOiA2cHggMTJweDsKICBib3JkZXItcmFkaXVzOiA5OTlweDsKICBmb250LXNpemU6IDEycHg7CiAgbGV0dGVyLXNwYWNpbmc6IDAuMDJlbTsKICBib3JkZXI6IDFweCBzb2xpZCB2YXIoLS1saS1saW5lKTsKICBiYWNrZ3JvdW5kOiByZ2JhKDE1LCAyNiwgNDMsIDAuODgpOwp9CgoubGktcGlsbC5vbiB7CiAgY29sb3I6ICMwODEyMGY7CiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDEzNWRlZywgdmFyKC0tbGktYWNjZW50KSwgIzg4ZWZlMik7CiAgYm9yZGVyLWNvbG9yOiB0cmFuc3BhcmVudDsKICBmb250LXdlaWdodDogNjAwOwp9CgoubGktcGlsbC5vZmYgewogIGNvbG9yOiB2YXIoLS1saS1tdXRlZCk7Cn0KCi5saS1waWxsLWhpZ2ggewogIGJhY2tncm91bmQ6IHJnYmEoMjU1LCAxMjAsIDEyMCwgMC4xNSk7CiAgY29sb3I6ICNmZjliOWI7Cn0KCi5saS1waWxsLW1lZGl1bSB7CiAgYmFja2dyb3VuZDogcmdiYSgyNTUsIDEzOCwgMTAyLCAwLjE2KTsKICBjb2xvcjogI2ZmZDBjMTsKfQoKLmxpLXBpbGwtbG93IHsKICBiYWNrZ3JvdW5kOiByZ2JhKDI0NSwgMjEwLCAxMDYsIDAuMTgpOwogIGNvbG9yOiAjZmJlN2E4Owp9CgoubGktc2NvcmUgewogIHdpZHRoOiAxNjBweDsKICBoZWlnaHQ6IDE2MHB4OwogIGJvcmRlci1yYWRpdXM6IDUwJTsKICBiYWNrZ3JvdW5kOgogICAgY29uaWMtZ3JhZGllbnQodmFyKC0tbGktYWNjZW50KSBjYWxjKHZhcigtLXNjb3JlKSAqIDElKSwgcmdiYSgyNTUsIDI1NSwgMjU1LCAwLjEpIDAlKTsKICBkaXNwbGF5OiBncmlkOwogIHBsYWNlLWl0ZW1zOiBjZW50ZXI7CiAgcG9zaXRpb246IHJlbGF0aXZlOwp9CgoubGktc2NvcmU6OmFmdGVyIHsKICBjb250ZW50OiAiIjsKICBwb3NpdGlvbjogYWJzb2x1dGU7CiAgaW5zZXQ6IDEwcHg7CiAgYm9yZGVyLXJhZGl1czogNTAlOwogIGJhY2tncm91bmQ6IHZhcigtLWxpLXBhbmVsKTsKICBib3JkZXI6IDFweCBzb2xpZCByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMjQpOwp9CgoubGktc2NvcmUtaW5uZXIgewogIHBvc2l0aW9uOiByZWxhdGl2ZTsKICB6LWluZGV4OiAxOwogIHRleHQtYWxpZ246IGNlbnRlcjsKfQoKLmxpLXNjb3JlLW51bSB7CiAgZm9udC1zaXplOiAzNnB4OwogIGZvbnQtd2VpZ2h0OiA3MDA7Cn0KCi5saS1zY29yZS1sYWJlbCB7CiAgZm9udC1zaXplOiAxMnB4OwogIGNvbG9yOiB2YXIoLS1saS1tdXRlZCk7Cn0KCi5saS1hbGVydCB7CiAgYmFja2dyb3VuZDogcmdiYSgyNTUsIDEyMCwgMTIwLCAwLjEyKTsKICBib3JkZXI6IDFweCBzb2xpZCByZ2JhKDI1NSwgMTIwLCAxMjAsIDAuMyk7CiAgY29sb3I6ICNmZmI2YjY7CiAgcGFkZGluZzogMTJweCAxNHB4OwogIGJvcmRlci1yYWRpdXM6IDE0cHg7CiAgbWFyZ2luLWJvdHRvbTogMThweDsKfQoKLmxpLWdyaWQgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiByZXBlYXQoYXV0by1maXQsIG1pbm1heCgyNDBweCwgMWZyKSk7CiAgZ2FwOiAxOHB4OwogIG1hcmdpbi1ib3R0b206IDIwcHg7Cn0KCi5saS1taW5pLWdyaWQgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiAxZnI7CiAgZ2FwOiAxNHB4OwogIG1hcmdpbi10b3A6IDE4cHg7Cn0KCi5saS1taW5pLXRpdGxlIHsKICBmb250LXdlaWdodDogNjAwOwp9CgoubGktbWluaS1ib2R5IHsKICBjb2xvcjogdmFyKC0tbGktbXV0ZWQpOwogIGZvbnQtc2l6ZTogMTRweDsKfQoKLmxpLWNhcmQgewogIGJhY2tncm91bmQ6IHZhcigtLWxpLWNhcmQpOwogIGJvcmRlcjogMXB4IHNvbGlkIHZhcigtLWxpLWxpbmUpOwogIGJvcmRlci1yYWRpdXM6IDE4cHg7CiAgcGFkZGluZzogMThweDsKICBib3gtc2hhZG93OiAwIDE4cHggNDBweCByZ2JhKDIsIDYsIDIzLCAwLjQ1KTsKICBhbmltYXRpb246IGxpLXJpc2UgMC41cyBlYXNlIGJvdGg7Cn0KCi5saS1jaGFydCB7CiAgcGFkZGluZzogMTZweDsKfQoKLmxpLWNoYXJ0IGNhbnZhcyB7CiAgd2lkdGg6IDEwMCU7CiAgaGVpZ2h0OiAxNDBweDsKICBiYWNrZ3JvdW5kOiByZ2JhKDExLCAyMCwgMzYsIDAuODgpOwogIGJvcmRlcjogMXB4IHNvbGlkIHJnYmEoMTQ4LCAxNjMsIDE4NCwgMC4yMik7CiAgYm9yZGVyLXJhZGl1czogMTRweDsKICBtYXJnaW4tYm90dG9tOiAxMHB4Owp9CgoubGktbGVnZW5kIHsKICBkaXNwbGF5OiBmbGV4OwogIGZsZXgtd3JhcDogd3JhcDsKICBnYXA6IDE0cHg7CiAgY29sb3I6IHZhcigtLWxpLW11dGVkKTsKICBmb250LXNpemU6IDEycHg7Cn0KCi5saS1sZWdlbmQgc3BhbiB7CiAgZGlzcGxheTogaW5saW5lLWZsZXg7CiAgYWxpZ24taXRlbXM6IGNlbnRlcjsKICBnYXA6IDZweDsKfQoKLmxpLWRvdCB7CiAgd2lkdGg6IDEwcHg7CiAgaGVpZ2h0OiAxMHB4OwogIGJvcmRlci1yYWRpdXM6IDk5OXB4OwogIGRpc3BsYXk6IGlubGluZS1ibG9jazsKfQoKLmxpLWRvdC1wYXN0IHsKICBiYWNrZ3JvdW5kOiB2YXIoLS1saS1hY2NlbnQtMyk7Cn0KCi5saS1kb3Qtbm93IHsKICBiYWNrZ3JvdW5kOiB2YXIoLS1saS1hY2NlbnQpOwp9CgoubGktZG90LXBvdGVudGlhbCB7CiAgYmFja2dyb3VuZDogdmFyKC0tbGktYWNjZW50LTIpOwp9CgoubGktaGlnaGxpZ2h0IHsKICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTM1ZGVnLCByZ2JhKDY4LCAyMTUsIDE5NywgMC4xNCksIHJnYmEoMjU1LCAxMzgsIDEwMiwgMC4xMikpOwp9CgoubGktY2FyZC1oZWFkIHsKICBkaXNwbGF5OiBmbGV4OwogIGp1c3RpZnktY29udGVudDogc3BhY2UtYmV0d2VlbjsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIGdhcDogMTJweDsKICBtYXJnaW4tYm90dG9tOiAxMnB4Owp9CgoubGktY2FyZCBoMyB7CiAgbWFyZ2luOiAwOwp9CgoubGktdGFnIHsKICBkaXNwbGF5OiBpbmxpbmUtZmxleDsKICBhbGlnbi1pdGVtczogY2VudGVyOwogIHBhZGRpbmc6IDZweCAxMHB4OwogIGJvcmRlci1yYWRpdXM6IDk5OXB4OwogIGZvbnQtc2l6ZTogMTJweDsKICBiYWNrZ3JvdW5kOiByZ2JhKDY4LCAyMTUsIDE5NywgMC4xNik7CiAgY29sb3I6ICNjOWZmZjI7CiAgYm9yZGVyOiAxcHggc29saWQgcmdiYSg2OCwgMjE1LCAxOTcsIDAuMyk7Cn0KCi5saS10YWctd2FybiB7CiAgYmFja2dyb3VuZDogcmdiYSgyNTUsIDEzOCwgMTAyLCAwLjE2KTsKICBjb2xvcjogI2ZmZDBjMTsKICBib3JkZXItY29sb3I6IHJnYmEoMjU1LCAxMzgsIDEwMiwgMC4zKTsKfQoKLmxpLXRhZy1hY2NlbnQgewogIGJhY2tncm91bmQ6IHJnYmEoMjQ1LCAyMTAsIDEwNiwgMC4xOCk7CiAgY29sb3I6ICNmYmU3YTg7CiAgYm9yZGVyLWNvbG9yOiByZ2JhKDI0NSwgMjEwLCAxMDYsIDAuMyk7Cn0KCi5saS10YWctZ3JvdXAgewogIGRpc3BsYXk6IGZsZXg7CiAgZmxleC13cmFwOiB3cmFwOwogIGdhcDogOHB4Owp9CgoubGktZm9ybSB7CiAgZGlzcGxheTogZ3JpZDsKICBnYXA6IDEwcHg7Cn0KCi5saS1mb3JtIGxhYmVsIHsKICBmb250LXNpemU6IDEzcHg7CiAgY29sb3I6IHZhcigtLWxpLW11dGVkKTsKfQoKLmxpLWZvcm0gaW5wdXQsCi5saS1mb3JtIHRleHRhcmVhIHsKICB3aWR0aDogMTAwJTsKICBiYWNrZ3JvdW5kOiByZ2JhKDExLCAyMCwgMzYsIDAuOTIpOwogIGNvbG9yOiB2YXIoLS1saS1pbmspOwogIGJvcmRlcjogMXB4IHNvbGlkIHJnYmEoMTQ4LCAxNjMsIDE4NCwgMC4yNCk7CiAgYm9yZGVyLXJhZGl1czogMTJweDsKICBwYWRkaW5nOiAxMnB4IDE0cHg7CiAgZm9udC1mYW1pbHk6IGluaGVyaXQ7Cn0KCi5saS1mb3JtIGlucHV0W3R5cGU9ImNoZWNrYm94Il0gewogIHdpZHRoOiBhdXRvOwogIG1hcmdpbi1yaWdodDogNnB4Owp9CgoubGktZm9ybSBsYWJlbCBpbnB1dFt0eXBlPSJjaGVja2JveCJdIHsKICBhY2NlbnQtY29sb3I6IHZhcigtLWxpLWFjY2VudCk7Cn0KCi5saS1mb3JtIGlucHV0OmZvY3VzLAoubGktZm9ybSB0ZXh0YXJlYTpmb2N1cyB7CiAgb3V0bGluZTogbm9uZTsKICBib3JkZXItY29sb3I6IHZhcigtLWxpLWFjY2VudCk7CiAgYm94LXNoYWRvdzogMCAwIDAgM3B4IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjE4KTsKfQoKLmxpLWJ0biB7CiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDEzNWRlZywgdmFyKC0tbGktYWNjZW50KSwgIzFlYTZhMCk7CiAgY29sb3I6ICMwODEyMGY7CiAgYm9yZGVyOiBub25lOwogIGJvcmRlci1yYWRpdXM6IDk5OXB4OwogIHBhZGRpbmc6IDEycHggMjBweDsKICBmb250LXdlaWdodDogNjAwOwogIGN1cnNvcjogcG9pbnRlcjsKICB0cmFuc2l0aW9uOiB0cmFuc2Zvcm0gMC4ycyBlYXNlLCBib3gtc2hhZG93IDAuMnMgZWFzZTsKfQoKLmxpLWJ0bjpob3ZlciB7CiAgdHJhbnNmb3JtOiB0cmFuc2xhdGVZKC0ycHgpOwogIGJveC1zaGFkb3c6IDAgMTJweCAyNHB4IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjI1KTsKfQoKLmxpLW5vdGUgewogIGNvbG9yOiB2YXIoLS1saS1tdXRlZCk7CiAgZm9udC1zaXplOiAxM3B4Owp9CgoubGktZGl2aWRlciB7CiAgaGVpZ2h0OiAxcHg7CiAgYmFja2dyb3VuZDogdmFyKC0tbGktbGluZSk7CiAgbWFyZ2luOiAxOHB4IDA7Cn0KCi5saS10YWJsZSB7CiAgZGlzcGxheTogZ3JpZDsKICBnYXA6IDEwcHg7Cn0KCi5saS10YWJsZS1oZWFkLAoubGktdGFibGUtcm93IHsKICBkaXNwbGF5OiBncmlkOwogIGdyaWQtdGVtcGxhdGUtY29sdW1uczogMS42ZnIgMC41ZnIgMC41ZnIgMC41ZnI7CiAgZ2FwOiAxMnB4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7Cn0KCi5saS10YWJsZS1oZWFkIHsKICBmb250LXNpemU6IDEycHg7CiAgdGV4dC10cmFuc2Zvcm06IHVwcGVyY2FzZTsKICBsZXR0ZXItc3BhY2luZzogMC4xZW07CiAgY29sb3I6IHZhcigtLWxpLW11dGVkKTsKfQoKLmxpLXRhYmxlLXJvdyB7CiAgYmFja2dyb3VuZDogcmdiYSgxMSwgMjAsIDM2LCAwLjg4KTsKICBwYWRkaW5nOiAxMHB4IDEycHg7CiAgYm9yZGVyLXJhZGl1czogMTJweDsKICBib3JkZXI6IDFweCBzb2xpZCByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMjIpOwp9CgoubGktbGluayB7CiAgY29sb3I6IHZhcigtLWxpLWFjY2VudCk7CiAgdGV4dC1kZWNvcmF0aW9uOiBub25lOwogIGZvbnQtd2VpZ2h0OiA2MDA7CiAgb3ZlcmZsb3ctd3JhcDogYW55d2hlcmU7Cn0KCi5saS1tb25vIHsKICBmb250LWZhbWlseTogdWktbW9ub3NwYWNlLCBTRk1vbm8tUmVndWxhciwgTWVubG8sIE1vbmFjbywgQ29uc29sYXMsICJMaWJlcmF0aW9uIE1vbm8iLCBtb25vc3BhY2U7Cn0KCi5saS1zdGF0LWdyaWQgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiByZXBlYXQoYXV0by1maXQsIG1pbm1heCgxMjBweCwgMWZyKSk7CiAgZ2FwOiAxMnB4Owp9CgoubGktc3RhdCB7CiAgcGFkZGluZzogMTJweDsKICBib3JkZXItcmFkaXVzOiAxNHB4OwogIGJhY2tncm91bmQ6IHJnYmEoMTEsIDIwLCAzNiwgMC44OCk7CiAgYm9yZGVyOiAxcHggc29saWQgcmdiYSgxNDgsIDE2MywgMTg0LCAwLjIyKTsKfQoKLmxpLXN0YXQgc3BhbiB7CiAgZGlzcGxheTogYmxvY2s7CiAgY29sb3I6IHZhcigtLWxpLW11dGVkKTsKICBmb250LXNpemU6IDEycHg7CiAgbWFyZ2luLWJvdHRvbTogNnB4Owp9CgoubGktc3RhdCBzdHJvbmcgewogIGZvbnQtc2l6ZTogMjBweDsKfQoKLmxpLWJhcnMgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiAxMnB4Owp9CgoubGktYmFyIHsKICBkaXNwbGF5OiBncmlkOwogIGdyaWQtdGVtcGxhdGUtY29sdW1uczogMTQwcHggMWZyIDQwcHg7CiAgZ2FwOiAxMnB4OwogIGFsaWduLWl0ZW1zOiBjZW50ZXI7Cn0KCi5saS1iYXItbGFiZWwgewogIGNvbG9yOiB2YXIoLS1saS1tdXRlZCk7CiAgZm9udC1zaXplOiAxM3B4Owp9CgoubGktYmFyLXZhbCB7CiAgZm9udC13ZWlnaHQ6IDYwMDsKICB0ZXh0LWFsaWduOiByaWdodDsKfQoKLmxpLWJhci10cmFjayB7CiAgcG9zaXRpb246IHJlbGF0aXZlOwogIGhlaWdodDogMTBweDsKICBiYWNrZ3JvdW5kOiByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMTYpOwogIGJvcmRlci1yYWRpdXM6IDk5OXB4OwogIG92ZXJmbG93OiBoaWRkZW47Cn0KCi5saS1iYXItdHJhY2sgc3BhbiB7CiAgZGlzcGxheTogYmxvY2s7CiAgaGVpZ2h0OiAxMDAlOwogIHdpZHRoOiBjYWxjKHZhcigtLXZhbCkgKiAxJSk7CiAgYmFja2dyb3VuZDogbGluZWFyLWdyYWRpZW50KDEzNWRlZywgdmFyKC0tbGktYWNjZW50KSwgdmFyKC0tbGktYWNjZW50LTIpKTsKICBib3JkZXItcmFkaXVzOiBpbmhlcml0OwogIHRyYW5zaXRpb246IHdpZHRoIDAuNnMgZWFzZTsKfQoKLmxpLXRhYi1idXR0b25zIHsKICBkaXNwbGF5OiBmbGV4OwogIGZsZXgtd3JhcDogd3JhcDsKICBnYXA6IDEwcHg7CiAgbWFyZ2luOiAyMHB4IDAgMTRweDsKfQoKLmxpLXRhYi1idG4gewogIGJhY2tncm91bmQ6IHJnYmEoMTEsIDIwLCAzNiwgMC44OCk7CiAgY29sb3I6IHZhcigtLWxpLW11dGVkKTsKICBib3JkZXI6IDFweCBzb2xpZCByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMjQpOwogIGJvcmRlci1yYWRpdXM6IDk5OXB4OwogIHBhZGRpbmc6IDhweCAxNHB4OwogIGN1cnNvcjogcG9pbnRlcjsKfQoKLmxpLXRhYi1idG4uYWN0aXZlIHsKICBjb2xvcjogIzA4MTIwZjsKICBiYWNrZ3JvdW5kOiBsaW5lYXItZ3JhZGllbnQoMTM1ZGVnLCByZ2JhKDY4LCAyMTUsIDE5NywgMC45NSksIHJnYmEoMjU1LCAxMzgsIDEwMiwgMC44MikpOwogIGJvcmRlci1jb2xvcjogdHJhbnNwYXJlbnQ7CiAgZm9udC13ZWlnaHQ6IDYwMDsKfQoKLmxpLXRhYi1wYW5lbCB7CiAgZGlzcGxheTogbm9uZTsKICBhbmltYXRpb246IGxpLWZhZGUgMC40cyBlYXNlOwp9CgoubGktdGFiLXBhbmVsLmFjdGl2ZSB7CiAgZGlzcGxheTogZ3JpZDsKICBnYXA6IDE2cHg7Cn0KCi5saS1jb21wYXJlIHsKICBkaXNwbGF5OiBncmlkOwogIGdyaWQtdGVtcGxhdGUtY29sdW1uczogcmVwZWF0KGF1dG8tZml0LCBtaW5tYXgoMjAwcHgsIDFmcikpOwogIGdhcDogMTZweDsKfQoKLmxpLW11dGVkIHsKICBjb2xvcjogdmFyKC0tbGktbXV0ZWQpOwogIGZvbnQtc2l6ZTogMTJweDsKICBkaXNwbGF5OiBpbmxpbmUtYmxvY2s7CiAgbWFyZ2luLWJvdHRvbTogNnB4Owp9CgoubGktY29weSB7CiAgYmFja2dyb3VuZDogcmdiYSgxMSwgMjAsIDM2LCAwLjg4KTsKICBjb2xvcjogdmFyKC0tbGktaW5rKTsKICBib3JkZXI6IDFweCBzb2xpZCByZ2JhKDE0OCwgMTYzLCAxODQsIDAuMjQpOwogIGJvcmRlci1yYWRpdXM6IDEwcHg7CiAgcGFkZGluZzogNnB4IDEycHg7CiAgY3Vyc29yOiBwb2ludGVyOwogIGZvbnQtc2l6ZTogMTJweDsKfQoKLmxpLWNvcHk6aG92ZXIgewogIGJvcmRlci1jb2xvcjogdmFyKC0tbGktYWNjZW50KTsKfQoKLmxpLWNvcHktYmxvY2sgewogIGJhY2tncm91bmQ6IHJnYmEoMTEsIDIwLCAzNiwgMC44OCk7CiAgYm9yZGVyOiAxcHggc29saWQgcmdiYSgxNDgsIDE2MywgMTg0LCAwLjIyKTsKICBib3JkZXItcmFkaXVzOiAxMnB4OwogIHBhZGRpbmc6IDEycHg7CiAgd2hpdGUtc3BhY2U6IHByZS13cmFwOwp9CgoubGktbGlzdCB7CiAgZGlzcGxheTogZ3JpZDsKICBnYXA6IDEwcHg7CiAgbWFyZ2luOiAwOwogIHBhZGRpbmc6IDA7CiAgbGlzdC1zdHlsZTogbm9uZTsKfQoKLmxpLWxpc3QgbGkgewogIHBvc2l0aW9uOiByZWxhdGl2ZTsKICBwYWRkaW5nLWxlZnQ6IDE4cHg7CiAgbGluZS1oZWlnaHQ6IDEuNTU7Cn0KCi5saS1saXN0IGxpOjpiZWZvcmUgewogIGNvbnRlbnQ6ICIiOwogIHBvc2l0aW9uOiBhYnNvbHV0ZTsKICBsZWZ0OiAwOwogIHRvcDogMC41NWVtOwogIHdpZHRoOiA4cHg7CiAgaGVpZ2h0OiA4cHg7CiAgYm9yZGVyLXJhZGl1czogNTAlOwogIGJhY2tncm91bmQ6IHZhcigtLWxpLWFjY2VudCk7CiAgYm94LXNoYWRvdzogMCAwIDAgM3B4IHJnYmEoNjgsIDIxNSwgMTk3LCAwLjE1KTsKfQoKLmxpLXRpbWVsaW5lIHsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogMTZweDsKfQoKLmxpLXRpbWVsaW5lLWl0ZW0gewogIGRpc3BsYXk6IGdyaWQ7CiAgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiAxMjBweCAxZnI7CiAgZ2FwOiAxMnB4OwogIGFsaWduLWl0ZW1zOiBzdGFydDsKfQoKLmxpLXRpbWUgewogIGNvbG9yOiB2YXIoLS1saS1hY2NlbnQpOwogIGZvbnQtd2VpZ2h0OiA2MDA7Cn0KCi5saS10aW1lbGluZS10aXRsZSB7CiAgZm9udC13ZWlnaHQ6IDYwMDsKICBtYXJnaW4tYm90dG9tOiA2cHg7Cn0KCi5saS1mb2N1cy1saXN0IHsKICBkaXNwbGF5OiBncmlkOwogIGdhcDogMTJweDsKfQoKLmxpLWZvY3VzLWl0ZW0gewogIHBhZGRpbmc6IDEycHg7CiAgYm9yZGVyLXJhZGl1czogMTRweDsKICBiYWNrZ3JvdW5kOiByZ2JhKDExLCAyMCwgMzYsIDAuODgpOwogIGJvcmRlcjogMXB4IHNvbGlkIHJnYmEoMTQ4LCAxNjMsIDE4NCwgMC4yMik7Cn0KCi5saS1mb2N1cy10aXRsZSB7CiAgZm9udC13ZWlnaHQ6IDYwMDsKICBtYXJnaW4tYm90dG9tOiA4cHg7Cn0KCi5saS1sZWFkIHsKICBmb250LXNpemU6IDE2cHg7CiAgbGluZS1oZWlnaHQ6IDEuNjsKfQoKLmxpLXJhdyBzdW1tYXJ5IHsKICBjdXJzb3I6IHBvaW50ZXI7CiAgZm9udC13ZWlnaHQ6IDYwMDsKfQoKLmxpLXJhdyBwcmUgewogIG1hcmdpbi10b3A6IDEycHg7CiAgYmFja2dyb3VuZDogcmdiYSgxMSwgMjAsIDM2LCAwLjg4KTsKICBib3JkZXItcmFkaXVzOiAxMnB4OwogIHBhZGRpbmc6IDEycHg7CiAgd2hpdGUtc3BhY2U6IHByZS13cmFwOwp9CgoubGktc2VjdGlvbi1zdGFjayB7CiAgZGlzcGxheTogZ3JpZDsKICBnYXA6IDE2cHg7Cn0KCi5saS1zZWN0aW9uLWNhcmQgewogIGdhcDogMTRweDsKfQoKLmxpLXNlY3Rpb24tYmxvY2sgewogIGRpc3BsYXk6IGdyaWQ7CiAgZ2FwOiA4cHg7Cn0KCkBrZXlmcmFtZXMgbGktcmlzZSB7CiAgZnJvbSB7CiAgICBvcGFjaXR5OiAwOwogICAgdHJhbnNmb3JtOiB0cmFuc2xhdGVZKDEycHgpOwogIH0KICB0byB7CiAgICBvcGFjaXR5OiAxOwogICAgdHJhbnNmb3JtOiB0cmFuc2xhdGVZKDApOwogIH0KfQoKQGtleWZyYW1lcyBsaS1mYWRlIHsKICBmcm9tIHsKICAgIG9wYWNpdHk6IDA7CiAgICB0cmFuc2Zvcm06IHRyYW5zbGF0ZVkoNnB4KTsKICB9CiAgdG8gewogICAgb3BhY2l0eTogMTsKICAgIHRyYW5zZm9ybTogdHJhbnNsYXRlWSgwKTsKICB9Cn0KCkBtZWRpYSAobWF4LXdpZHRoOiA5MDBweCkgewogIC5saS1oZXJvIHsKICAgIGZsZXgtZGlyZWN0aW9uOiBjb2x1bW47CiAgICBhbGlnbi1pdGVtczogZmxleC1zdGFydDsKICB9CgogIC5saS1zY29yZSB7CiAgICB3aWR0aDogMTQwcHg7CiAgICBoZWlnaHQ6IDE0MHB4OwogIH0KCiAgLmxpLXRhYmxlLWhlYWQsCiAgLmxpLXRhYmxlLXJvdyB7CiAgICBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IDFmciAwLjRmciAwLjRmcjsKICB9CgogIC5saS10YWJsZS1yb3cgYSB7CiAgICBncmlkLWNvbHVtbjogMSAvIC0xOwogICAgbWFyZ2luLXRvcDogNnB4OwogIH0KfQoKQG1lZGlhIChtYXgtd2lkdGg6IDcyMHB4KSB7CiAgLmxpLWJhciB7CiAgICBncmlkLXRlbXBsYXRlLWNvbHVtbnM6IDFmcjsKICAgIGdhcDogNnB4OwogIH0KCiAgLmxpLXRpbWVsaW5lLWl0ZW0gewogICAgZ3JpZC10ZW1wbGF0ZS1jb2x1bW5zOiAxZnI7CiAgfQp9DQo=","mimetype":"text/css"},"linkedin.js":{"b64":"77u/ZG9jdW1lbnQuYWRkRXZlbnRMaXN0ZW5lcigiRE9NQ29udGVudExvYWRlZCIsICgpID0+IHsKICBjb25zdCB0YWJCdXR0b25zID0gQXJyYXkuZnJvbShkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCJbZGF0YS1saS10YWJdIikpOwogIGNvbnN0IHRhYlBhbmVscyA9IEFycmF5LmZyb20oZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgiW2RhdGEtbGktcGFuZWxdIikpOwoKICBpZiAodGFiQnV0dG9ucy5sZW5ndGggJiYgdGFiUGFuZWxzLmxlbmd0aCkgewogICAgdGFiQnV0dG9ucy5mb3JFYWNoKChidG4pID0+IHsKICAgICAgYnRuLmFkZEV2ZW50TGlzdGVuZXIoImNsaWNrIiwgKCkgPT4gewogICAgICAgIGNvbnN0IHRhcmdldCA9IGJ0bi5nZXRBdHRyaWJ1dGUoImRhdGEtbGktdGFiIik7CiAgICAgICAgdGFiQnV0dG9ucy5mb3JFYWNoKChiKSA9PiBiLmNsYXNzTGlzdC50b2dnbGUoImFjdGl2ZSIsIGIgPT09IGJ0bikpOwogICAgICAgIHRhYlBhbmVscy5mb3JFYWNoKChwYW5lbCkgPT4gewogICAgICAgICAgcGFuZWwuY2xhc3NMaXN0LnRvZ2dsZSgiYWN0aXZlIiwgcGFuZWwuZ2V0QXR0cmlidXRlKCJkYXRhLWxpLXBhbmVsIikgPT09IHRhcmdldCk7CiAgICAgICAgfSk7CiAgICAgIH0pOwogICAgfSk7CiAgfQoKICBjb25zdCBjb3B5QnV0dG9ucyA9IEFycmF5LmZyb20oZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgiW2RhdGEtY29weS10YXJnZXRdIikpOwogIGNvcHlCdXR0b25zLmZvckVhY2goKGJ0bikgPT4gewogICAgYnRuLmFkZEV2ZW50TGlzdGVuZXIoImNsaWNrIiwgYXN5bmMgKCkgPT4gewogICAgICBjb25zdCB0YXJnZXRJZCA9IGJ0bi5nZXRBdHRyaWJ1dGUoImRhdGEtY29weS10YXJnZXQiKTsKICAgICAgaWYgKCF0YXJnZXRJZCkgcmV0dXJuOwogICAgICBjb25zdCB0YXJnZXQgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCh0YXJnZXRJZCk7CiAgICAgIGlmICghdGFyZ2V0KSByZXR1cm47CiAgICAgIGNvbnN0IHRleHQgPSB0YXJnZXQuaW5uZXJUZXh0LnRyaW0oKTsKICAgICAgaWYgKCF0ZXh0KSByZXR1cm47CgogICAgICB0cnkgewogICAgICAgIGlmIChuYXZpZ2F0b3IuY2xpcGJvYXJkICYmIG5hdmlnYXRvci5jbGlwYm9hcmQud3JpdGVUZXh0KSB7CiAgICAgICAgICBhd2FpdCBuYXZpZ2F0b3IuY2xpcGJvYXJkLndyaXRlVGV4dCh0ZXh0KTsKICAgICAgICB9IGVsc2UgewogICAgICAgICAgY29uc3QgYXJlYSA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoInRleHRhcmVhIik7CiAgICAgICAgICBhcmVhLnZhbHVlID0gdGV4dDsKICAgICAgICAgIGRvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQoYXJlYSk7CiAgICAgICAgICBhcmVhLnNlbGVjdCgpOwogICAgICAgICAgZG9jdW1lbnQuZXhlY0NvbW1hbmQoImNvcHkiKTsKICAgICAgICAgIGRvY3VtZW50LmJvZHkucmVtb3ZlQ2hpbGQoYXJlYSk7CiAgICAgICAgfQogICAgICAgIGNvbnN0IG9yaWdpbmFsID0gYnRuLnRleHRDb250ZW50OwogICAgICAgIGJ0bi50ZXh0Q29udGVudCA9ICJDb3BpZWQiOwogICAgICAgIHNldFRpbWVvdXQoKCkgPT4gewogICAgICAgICAgYnRuLnRleHRDb250ZW50ID0gb3JpZ2luYWw7CiAgICAgICAgfSwgMTUwMCk7CiAgICAgIH0gY2F0Y2ggKGVycikgewogICAgICAgIGNvbnNvbGUud2FybigiQ29weSBmYWlsZWQiLCBlcnIpOwogICAgICB9CiAgICB9KTsKICB9KTsKCiAgY29uc3QgZHJhd1Njb3JlVHJlbmQgPSAoY2FudmFzKSA9PiB7CiAgICBpZiAoIWNhbnZhcykgcmV0dXJuOwogICAgY29uc3QgY3R4ID0gY2FudmFzLmdldENvbnRleHQoIjJkIik7CiAgICBjb25zdCBoaXN0b3J5UmF3ID0gY2FudmFzLmdldEF0dHJpYnV0ZSgiZGF0YS1oaXN0b3J5Iik7CiAgICBsZXQgaGlzdG9yeSA9IFtdOwogICAgdHJ5IHsKICAgICAgaGlzdG9yeSA9IEpTT04ucGFyc2UoaGlzdG9yeVJhdyB8fCAiW10iKTsKICAgIH0gY2F0Y2ggKGVycikgewogICAgICBoaXN0b3J5ID0gW107CiAgICB9CgogICAgY29uc3QgcmVjZW50ID0gaGlzdG9yeS5zbGljZSgwLCA1KS5yZXZlcnNlKCk7CiAgICBjb25zdCBzY29yZXMgPSByZWNlbnQubWFwKChoKSA9PiBOdW1iZXIoaC5vdmVyYWxsX3Njb3JlIHx8IDApKTsKICAgIGlmICghc2NvcmVzLmxlbmd0aCkgewogICAgICByZXR1cm47CiAgICB9CgogICAgY29uc3QgbGFiZWxzID0gcmVjZW50Lm1hcCgoaCkgPT4gewogICAgICBjb25zdCByYXcgPSBTdHJpbmcoaC50aW1lc3RhbXAgfHwgIiIpOwogICAgICBpZiAoIXJhdykgcmV0dXJuICIiOwogICAgICBjb25zdCBwYXJ0cyA9IHJhdy5zcGxpdCgiICIpOwogICAgICBjb25zdCBkYXRlID0gcGFydHNbMF0gfHwgIiI7CiAgICAgIGNvbnN0IHRpbWUgPSBwYXJ0c1sxXSB8fCAiIjsKICAgICAgY29uc3QgbW1kZCA9IGRhdGUubGVuZ3RoID49IDEwID8gZGF0ZS5zbGljZSg1KSA6IGRhdGU7CiAgICAgIGNvbnN0IGhtID0gdGltZSA/IHRpbWUuc2xpY2UoMCwgNSkgOiAiIjsKICAgICAgcmV0dXJuIGhtID8gYCR7bW1kZH0gJHtobX1gIDogbW1kZDsKICAgIH0pOwoKICAgIGNvbnN0IGRwciA9IHdpbmRvdy5kZXZpY2VQaXhlbFJhdGlvIHx8IDE7CiAgICBjb25zdCByZWN0ID0gY2FudmFzLmdldEJvdW5kaW5nQ2xpZW50UmVjdCgpOwogICAgY29uc3QgZGlzcGxheVdpZHRoID0gTWF0aC5tYXgocmVjdC53aWR0aCwgMzIwKTsKICAgIGNvbnN0IGRpc3BsYXlIZWlnaHQgPSBNYXRoLm1heChyZWN0LmhlaWdodCB8fCAxNDAsIDE0MCk7CiAgICBjYW52YXMud2lkdGggPSBNYXRoLmZsb29yKGRpc3BsYXlXaWR0aCAqIGRwcik7CiAgICBjYW52YXMuaGVpZ2h0ID0gTWF0aC5mbG9vcihkaXNwbGF5SGVpZ2h0ICogZHByKTsKICAgIGN0eC5zZXRUcmFuc2Zvcm0oZHByLCAwLCAwLCBkcHIsIDAsIDApOwoKICAgIGNvbnN0IHdpZHRoID0gZGlzcGxheVdpZHRoOwogICAgY29uc3QgaGVpZ2h0ID0gZGlzcGxheUhlaWdodDsKICAgIGNvbnN0IHBhZFggPSAxODsKICAgIGNvbnN0IHBhZFRvcCA9IDE0OwogICAgY29uc3QgcGFkQm90dG9tID0gMzA7CiAgICBjb25zdCBwbG90V2lkdGggPSB3aWR0aCAtIHBhZFggKiAyOwogICAgY29uc3QgcGxvdEhlaWdodCA9IGhlaWdodCAtIHBhZFRvcCAtIHBhZEJvdHRvbTsKCiAgICBjb25zdCBjdXJyZW50ID0gc2NvcmVzW3Njb3Jlcy5sZW5ndGggLSAxXTsKICAgIGNvbnN0IHBvdGVudGlhbCA9IE1hdGgubWluKDEwMCwgTWF0aC5yb3VuZChjdXJyZW50ICsgTWF0aC5tYXgoNiwgKDEwMCAtIGN1cnJlbnQpICogMC4zNSkpKTsKCiAgICBsZXQgbWluU2NvcmUgPSBNYXRoLm1pbiguLi5zY29yZXMsIHBvdGVudGlhbCkgLSA2OwogICAgbGV0IG1heFNjb3JlID0gTWF0aC5tYXgoLi4uc2NvcmVzLCBwb3RlbnRpYWwpICsgNjsKICAgIG1pblNjb3JlID0gTWF0aC5tYXgoMCwgbWluU2NvcmUpOwogICAgbWF4U2NvcmUgPSBNYXRoLm1pbigxMDAsIG1heFNjb3JlKTsKICAgIGlmIChtYXhTY29yZSAtIG1pblNjb3JlIDwgMTApIHsKICAgICAgbWluU2NvcmUgPSBNYXRoLm1heCgwLCBtaW5TY29yZSAtIDUpOwogICAgICBtYXhTY29yZSA9IE1hdGgubWluKDEwMCwgbWF4U2NvcmUgKyA1KTsKICAgIH0KCiAgICBjb25zdCB4Rm9yID0gKGlkeCkgPT4KICAgICAgcGFkWCArIChzY29yZXMubGVuZ3RoID09PSAxID8gMC41IDogaWR4IC8gKHNjb3Jlcy5sZW5ndGggLSAxKSkgKiBwbG90V2lkdGg7CiAgICBjb25zdCB5Rm9yID0gKHNjb3JlKSA9PgogICAgICBwYWRUb3AgKyAoMSAtIChzY29yZSAtIG1pblNjb3JlKSAvIChtYXhTY29yZSAtIG1pblNjb3JlIHx8IDEpKSAqIHBsb3RIZWlnaHQ7CgogICAgY3R4LmNsZWFyUmVjdCgwLCAwLCB3aWR0aCwgaGVpZ2h0KTsKCiAgICBjdHguc3Ryb2tlU3R5bGUgPSAicmdiYSgyNTUsMjU1LDI1NSwwLjA4KSI7CiAgICBjdHgubGluZVdpZHRoID0gMTsKICAgIGZvciAobGV0IGkgPSAwOyBpIDw9IDI7IGkgKz0gMSkgewogICAgICBjb25zdCB5ID0gcGFkVG9wICsgKHBsb3RIZWlnaHQgLyAyKSAqIGk7CiAgICAgIGN0eC5iZWdpblBhdGgoKTsKICAgICAgY3R4Lm1vdmVUbyhwYWRYLCB5KTsKICAgICAgY3R4LmxpbmVUbyh3aWR0aCAtIHBhZFgsIHkpOwogICAgICBjdHguc3Ryb2tlKCk7CiAgICB9CgogICAgaWYgKHNjb3Jlcy5sZW5ndGggPiAxKSB7CiAgICAgIGN0eC5zdHJva2VTdHlsZSA9ICIjN2FhMmZmIjsKICAgICAgY3R4LmxpbmVXaWR0aCA9IDI7CiAgICAgIGN0eC5iZWdpblBhdGgoKTsKICAgICAgc2NvcmVzLmZvckVhY2goKHNjb3JlLCBpZHgpID0+IHsKICAgICAgICBjb25zdCB4ID0geEZvcihpZHgpOwogICAgICAgIGNvbnN0IHkgPSB5Rm9yKHNjb3JlKTsKICAgICAgICBpZiAoaWR4ID09PSAwKSBjdHgubW92ZVRvKHgsIHkpOwogICAgICAgIGVsc2UgY3R4LmxpbmVUbyh4LCB5KTsKICAgICAgfSk7CiAgICAgIGN0eC5zdHJva2UoKTsKICAgIH0KCiAgICBzY29yZXMuZm9yRWFjaCgoc2NvcmUsIGlkeCkgPT4gewogICAgICBjb25zdCB4ID0geEZvcihpZHgpOwogICAgICBjb25zdCB5ID0geUZvcihzY29yZSk7CiAgICAgIGN0eC5maWxsU3R5bGUgPSBpZHggPT09IHNjb3Jlcy5sZW5ndGggLSAxID8gIiMzN2UwYjUiIDogIiM3YWEyZmYiOwogICAgICBjdHguYmVnaW5QYXRoKCk7CiAgICAgIGN0eC5hcmMoeCwgeSwgaWR4ID09PSBzY29yZXMubGVuZ3RoIC0gMSA/IDQgOiAzLCAwLCBNYXRoLlBJICogMik7CiAgICAgIGN0eC5maWxsKCk7CiAgICB9KTsKCiAgICBjdHguZmlsbFN0eWxlID0gInJnYmEoMjMzLDI0MCwyNDcsMC44NSkiOwogICAgY3R4LmZvbnQgPSAiMTFweCAnSUJNIFBsZXggU2FucycsIHNhbnMtc2VyaWYiOwogICAgc2NvcmVzLmZvckVhY2goKHNjb3JlLCBpZHgpID0+IHsKICAgICAgY29uc3QgeCA9IHhGb3IoaWR4KTsKICAgICAgY29uc3QgeSA9IHlGb3Ioc2NvcmUpOwogICAgICBjb25zdCBvZmZzZXQgPSBpZHggPT09IHNjb3Jlcy5sZW5ndGggLSAxID8gMTIgOiAxMDsKICAgICAgY3R4LnRleHRBbGlnbiA9ICJjZW50ZXIiOwogICAgICBjdHguZmlsbFRleHQoU3RyaW5nKHNjb3JlKSwgeCwgTWF0aC5tYXgoMTAsIHkgLSBvZmZzZXQpKTsKICAgIH0pOwoKICAgIGNvbnN0IGxhc3RYID0geEZvcihzY29yZXMubGVuZ3RoIC0gMSk7CiAgICBjb25zdCBsYXN0WSA9IHlGb3IoY3VycmVudCk7CiAgICBjdHguc3Ryb2tlU3R5bGUgPSAiI2ZmYjg2YyI7CiAgICBjdHguc2V0TGluZURhc2goWzYsIDVdKTsKICAgIGN0eC5iZWdpblBhdGgoKTsKICAgIGN0eC5tb3ZlVG8obGFzdFgsIGxhc3RZKTsKICAgIGN0eC5saW5lVG8od2lkdGggLSBwYWRYLCB5Rm9yKHBvdGVudGlhbCkpOwogICAgY3R4LnN0cm9rZSgpOwogICAgY3R4LnNldExpbmVEYXNoKFtdKTsKCiAgICBjdHguZmlsbFN0eWxlID0gIiNmZmI4NmMiOwogICAgY3R4LmJlZ2luUGF0aCgpOwogICAgY3R4LmFyYyh3aWR0aCAtIHBhZFgsIHlGb3IocG90ZW50aWFsKSwgMywgMCwgTWF0aC5QSSAqIDIpOwogICAgY3R4LmZpbGwoKTsKCiAgICBjdHguZmlsbFN0eWxlID0gIiNmZmI4NmMiOwogICAgY3R4LmZvbnQgPSAiMTFweCAnSUJNIFBsZXggU2FucycsIHNhbnMtc2VyaWYiOwogICAgY3R4LnRleHRBbGlnbiA9ICJyaWdodCI7CiAgICBjdHguZmlsbFRleHQoU3RyaW5nKHBvdGVudGlhbCksIHdpZHRoIC0gcGFkWCAtIDYsIE1hdGgubWF4KDEwLCB5Rm9yKHBvdGVudGlhbCkgLSA4KSk7CgogICAgY3R4LmZpbGxTdHlsZSA9ICJyZ2JhKDIzMywyNDAsMjQ3LDAuNzUpIjsKICAgIGN0eC5mb250ID0gIjExcHggJ0lCTSBQbGV4IFNhbnMnLCBzYW5zLXNlcmlmIjsKICAgIGxhYmVscy5mb3JFYWNoKChsYWJlbCwgaWR4KSA9PiB7CiAgICAgIGlmICghbGFiZWwpIHJldHVybjsKICAgICAgY29uc3QgeCA9IHhGb3IoaWR4KTsKICAgICAgY3R4LnRleHRBbGlnbiA9ICJjZW50ZXIiOwogICAgICBjdHguZmlsbFRleHQobGFiZWwsIHgsIGhlaWdodCAtIDEwKTsKICAgIH0pOwogIH07CgogIGRyYXdTY29yZVRyZW5kKGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJsaVNjb3JlVHJlbmQiKSk7CiAgZHJhd1Njb3JlVHJlbmQoZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoInJlc3VtZVNjb3JlVHJlbmQiKSk7Cn0pOw0K","mimetype":"text/javascript"}}

def _load_embedded_templates():
    templates = {}
    for name, b64 in EMBEDDED_TEMPLATES_B64.items():
        try:
            templates[name] = base64.b64decode(b64).decode('utf-8')
        except Exception:
            templates[name] = base64.b64decode(b64).decode('utf-8', errors='replace')
    return templates

EMBEDDED_TEMPLATES = _load_embedded_templates()
EMBEDDED_STATIC = EMBEDDED_STATIC_B64

app = Flask(__name__, static_folder=None)
app.jinja_loader = DictLoader(EMBEDDED_TEMPLATES)

@app.route('/static/<path:filename>', endpoint='static')
def _static_from_memory(filename):
    entry = EMBEDDED_STATIC.get(filename)
    if not entry:
        abort(404)
    data = base64.b64decode(entry['b64'])
    resp = app.response_class(data, mimetype=entry.get('mimetype') or 'application/octet-stream')
    resp.headers['Cache-Control'] = 'public, max-age=3600'
    return resp
JOBS = {}
EMAIL_SETS = {}
EMAIL_JOBS = {}
AUTO_APPLY_EXECUTIONS = {}
LAST_GEMINI_ERROR = ""
RESUME_AI_CACHE = {}
UPLOAD_DIR = APP_ROOT / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


def clean_bullet_text(value):
    if not isinstance(value, str):
        return value
    cleaned = value
    cleaned = re.sub(r"(?i)\\?u2022", "", cleaned)
    cleaned = cleaned.replace("\u2022", "").replace("•", "")
    cleaned = cleaned.replace("·", "")
    cleaned = cleaned.replace("Ã¢â‚¬Â¢", "").replace("â€¢", "")
    cleaned = re.sub(r"^[\s•\-–—]+", "", cleaned)
    cleaned = re.sub(r"[ \t]{2,}", " ", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def summarize_display_list(values, empty_text="No items saved", max_items=4):
    items = []
    seen = set()
    for value in values or []:
        text = clean_bullet_text(str(value or "")).strip(" ,")
        if not text:
            continue
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        items.append(text)
    if not items:
        return empty_text
    if len(items) <= max_items:
        return ", ".join(items)
    return f"{', '.join(items[:max_items])} +{len(items) - max_items} more"


app.jinja_env.filters["clean_bullets"] = clean_bullet_text


def get_defaults():
    return {
        "linkedin_username": os.getenv("LINKEDIN_USERNAME", ""),
    }


def get_dashboard_metrics():
    total_emails = 0
    latest = latest_master_quality_file()
    if latest:
        try:
            if latest.suffix.lower() == ".csv":
                df = pd.read_csv(latest)
            else:
                df = pd.read_excel(latest)
            combined = " ".join(
                str(x or "")
                for x in df.get("Emails", [])
            )
            total_emails = len(extract_emails(combined))
        except Exception:
            total_emails = 0

    total_sent = 0
    log_files = list(OUTPUT_DIR.glob("email_log_*.csv"))
    if log_files:
        last_log = max(log_files, key=lambda p: p.stat().st_mtime)
        try:
            log_df = pd.read_csv(last_log)
            total_sent = (log_df["status"] == "sent").sum()
        except Exception:
            total_sent = 0

    resume_score = 0
    resume_issues = 0
    reviews = list(RESUME_DIR.glob("*.json"))
    if reviews:
        latest = max(reviews, key=lambda p: p.stat().st_mtime)
        try:
            data = json.loads(latest.read_text(encoding="utf-8"))
            resume_score = int(data.get("overall_score", 0))
            resume_issues = len(data.get("issues", []))
        except Exception:
            resume_score = 0
            resume_issues = 0

    linkedin_score = 0
    linkedin_issues = 0
    linkedin_reviews = list(LINKEDIN_DIR.glob("*.json"))
    if linkedin_reviews:
        latest = max(linkedin_reviews, key=lambda p: p.stat().st_mtime)
        try:
            data = json.loads(latest.read_text(encoding="utf-8"))
            linkedin_score = int(data.get("overall_score", 0))
            linkedin_issues = len(data.get("issues", []))
        except Exception:
            linkedin_score = 0
            linkedin_issues = 0

    tracking_summary = get_tracking_summary()
    auto_apply_summary = get_auto_apply_summary()

    return {
        "total_emails": total_emails,
        "total_sent": total_sent,
        "open_rate": tracking_summary["open_rate"],
        "tracking_enabled": tracking_summary["tracking_enabled"],
        "tracked_emails": tracking_summary["tracked_emails"],
        "opened_emails": tracking_summary["opened_emails"],
        "total_open_events": tracking_summary["total_open_events"],
        "top_open_count": tracking_summary["top_open_count"],
        "top_open_subject": tracking_summary["top_open_subject"],
        "tracking_items": tracking_summary["items"],
        "tracking_note": tracking_summary["note"],
        "resume_score": resume_score,
        "resume_issues_count": resume_issues,
        "linkedin_score": linkedin_score,
        "linkedin_issues_count": linkedin_issues,
        "auto_apply_profile_completion": auto_apply_summary["profile_completion"],
        "auto_apply_ready_platforms": auto_apply_summary["ready_platforms"],
        "auto_apply_active_platforms": auto_apply_summary["active_platforms"],
        "auto_apply_saved_runs": auto_apply_summary["saved_runs"],
        "auto_apply_last_run_status": auto_apply_summary["last_run_status"],
        "auto_apply_last_run_timestamp": auto_apply_summary["last_run_timestamp"],
    }


def get_email_cfg():
    return {
        "credentials_path": os.getenv("GMAIL_CREDENTIALS", ""),
        "token_path": os.getenv("GMAIL_TOKEN", str(APP_ROOT / "secrets" / "token.json")),
        "client_id": os.getenv("GMAIL_CLIENT_ID", ""),
        "client_secret": os.getenv("GMAIL_CLIENT_SECRET", ""),
    }


AUTO_APPLY_PLATFORM_LABELS = {
    "gmail": "Gmail",
    "linkedin": "LinkedIn",
    "indeed": "Indeed",
    "naukri": "Naukri",
}
AUTO_APPLY_EXECUTION_KEYS = ("linkedin", "indeed", "naukri")


def clone_json_value(value):
    return json.loads(json.dumps(value))


def auto_apply_default_settings():
    return {
        "search": {
            "keywords": [],
            "roles": [],
            "companies": [],
            "locations": [],
            "exclude_keywords": [],
            "exclude_companies": [],
            "work_modes": ["remote", "hybrid"],
            "job_boards": ["LinkedIn", "Indeed", "Naukri"],
            "experience_range": "",
            "salary_target": "",
        },
        "profile": {
            "full_name": "",
            "email": "",
            "phone": "",
            "current_location": "",
            "years_experience": "",
            "notice_period": "",
            "work_authorization": "",
            "linkedin_url": "",
            "portfolio_url": "",
            "summary": "",
            "top_skills": [],
        },
        "accounts": {
            "gmail_address": "",
            "linkedin_username": "",
            "indeed_email": "",
            "naukri_email": "",
            "browser_profile": "",
            "verification_notes": "",
            "use_gmail": True,
            "use_linkedin": True,
            "use_indeed": True,
            "use_naukri": True,
        },
        "automation": {
            "enabled": True,
            "require_review": True,
            "store_answers": True,
            "max_applications_per_run": 20,
            "scan_interval_minutes": 180,
            "cooldown_hours": 12,
            "trigger_note": "",
        },
        "scanner": {
            "query": "",
            "keywords": "",
            "companies": "",
            "locations": "",
            "urls": "",
            "sources": "",
            "strategy": DEFAULT_AUTO_APPLY_SCAN_STRATEGY,
            "limit_per_source": "40",
            "max_pages": "2",
            "last_unsupported_report_xlsx": "",
            "last_unsupported_report_csv": "",
        },
    }


def merge_with_defaults(data, default):
    if isinstance(default, dict):
        source = data if isinstance(data, dict) else {}
        merged = {}
        for key, default_value in default.items():
            merged[key] = merge_with_defaults(source.get(key), default_value)
        for key, value in source.items():
            if key not in merged:
                merged[key] = value
        return merged
    if isinstance(default, list):
        if isinstance(data, list):
            return data
        return clone_json_value(default)
    return default if data is None else data


def read_json_file(path: Path, default):
    if not path.exists():
        return clone_json_value(default)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return clone_json_value(default)
    return merge_with_defaults(payload, default)


def write_json_file(path: Path, payload):
    path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")


def read_dataframe_file(path: Path):
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    return pd.read_excel(path)


def split_multivalue_text(value):
    if not isinstance(value, str):
        return []
    parts = re.split(r"[\n,]", value)
    return [part.strip() for part in parts if part and part.strip()]


def split_url_text(value):
    if isinstance(value, (list, tuple, set)):
        urls = []
        seen = set()
        for item in value:
            for url in split_url_text(item):
                lowered = url.lower()
                if lowered in seen:
                    continue
                seen.add(lowered)
                urls.append(url)
        return urls
    if not isinstance(value, str):
        return []
    text = value.replace("](", "\n").replace("[", "\n").replace(")", "\n")
    matches = re.findall(r"https?://[^\s\]\[<>{}\"',;]+", text, flags=re.I)
    parts = matches or re.split(r"[\n,;]+", value)
    urls = []
    seen = set()
    for part in parts:
        item = (part or "").strip().strip("<>[](){}\"'")
        item = re.sub(r"[\].,]+$", "", item)
        if not item:
            continue
        lowered = item.lower()
        if not lowered.startswith(("http://", "https://")):
            continue
        if lowered in seen:
            continue
        seen.add(lowered)
        urls.append(item)
    return urls


def infer_scan_sources_from_urls(urls):
    sources = []
    seen = set()
    for url in urls or []:
        source = detect_ats_platform_from_url(url)
        if source not in AUTO_APPLY_SUPPORTED_SOURCES:
            source = "generic"
        if source in seen:
            continue
        seen.add(source)
        sources.append(source)
    return sources


def sanitize_scanner_company_filters(query, keywords, companies):
    query_key = normalize_match_text(query)
    keyword_keys = {normalize_match_text(item) for item in (keywords or []) if normalize_match_text(item)}
    cleaned = []
    for company in companies or []:
        company_key = normalize_match_text(company)
        if not company_key:
            continue
        if company_key == query_key or company_key in keyword_keys:
            continue
        cleaned.append(company)
    return cleaned


def parse_int_field(value, default, min_value=None, max_value=None):
    try:
        number = int(str(value).strip())
    except Exception:
        number = default
    if min_value is not None:
        number = max(min_value, number)
    if max_value is not None:
        number = min(max_value, number)
    return number


def form_checkbox_on(form, name):
    return (form.get(name) or "").strip().lower() in {"1", "true", "on", "yes"}


def resolve_app_path(raw_path):
    raw_path = (raw_path or "").strip()
    if not raw_path:
        return None
    path = Path(raw_path)
    if not path.is_absolute():
        path = APP_ROOT / path
    return path


def list_output_files(pattern="*.*", suffixes=None):
    suffixes = {item.lower() for item in (suffixes or [])}
    files = []
    for path in OUTPUT_DIR.glob(pattern):
        if not path.is_file():
            continue
        if suffixes and path.suffix.lower() not in suffixes:
            continue
        files.append(path)
    files.sort(key=lambda item: (item.stat().st_mtime, item.name.lower()), reverse=True)
    return files


def latest_output_file(pattern="*.*", suffixes=None):
    files = list_output_files(pattern=pattern, suffixes=suffixes)
    return files[0] if files else None


def resolve_output_path(raw_path, must_exist=True):
    raw_path = (raw_path or "").strip()
    if not raw_path:
        return None
    base_dir = OUTPUT_DIR.resolve()
    try:
        candidate = (base_dir / raw_path).resolve()
        candidate.relative_to(base_dir)
    except Exception:
        return None
    if must_exist and (not candidate.exists() or not candidate.is_file()):
        return None
    return candidate


def relative_output_name(path: Path):
    return path.resolve().relative_to(OUTPUT_DIR.resolve()).as_posix()


def load_auto_apply_settings():
    return read_json_file(AUTO_APPLY_SETTINGS_PATH, auto_apply_default_settings())


def save_auto_apply_settings(settings):
    normalized = merge_with_defaults(settings, auto_apply_default_settings())
    write_json_file(AUTO_APPLY_SETTINGS_PATH, normalized)
    return normalized


def load_auto_apply_history(limit=None):
    history = read_json_file(AUTO_APPLY_HISTORY_PATH, [])
    if not isinstance(history, list):
        history = []
    history = [normalize_auto_apply_history_item(item) for item in history if isinstance(item, dict)]
    history.sort(key=lambda item: item.get("timestamp", ""), reverse=True)
    if isinstance(limit, int):
        return history[:limit]
    return history


def save_auto_apply_history(history):
    clean_history = history if isinstance(history, list) else []
    write_json_file(AUTO_APPLY_HISTORY_PATH, clean_history[:40])


def normalize_auto_apply_form(form, current_settings=None):
    current_settings = merge_with_defaults(current_settings or {}, auto_apply_default_settings())

    def form_text(name, default=""):
        if name in form:
            return form.get(name, "").strip()
        return str(default or "").strip()

    def form_list(name, default=None):
        if name in form:
            return split_multivalue_text(form.get(name, ""))
        return list(default or [])

    def form_bool(name, default=False):
        if name in form:
            return form_checkbox_on(form, name)
        return bool(default)

    def form_int(name, default, min_value=None, max_value=None):
        if name in form:
            return parse_int_field(form.get(name, ""), default, min_value=min_value, max_value=max_value)
        return default

    search_defaults = current_settings.get("search", {})
    profile_defaults = current_settings.get("profile", {})
    account_defaults = current_settings.get("accounts", {})
    automation_defaults = current_settings.get("automation", {})
    scanner_defaults = current_settings.get("scanner", {})

    return {
        "search": {
            "keywords": form_list("keywords", search_defaults.get("keywords")),
            "roles": form_list("roles", search_defaults.get("roles")),
            "companies": form_list("companies", search_defaults.get("companies")),
            "locations": form_list("locations", search_defaults.get("locations")),
            "exclude_keywords": form_list("exclude_keywords", search_defaults.get("exclude_keywords")),
            "exclude_companies": form_list("exclude_companies", search_defaults.get("exclude_companies")),
            "work_modes": form_list("work_modes", search_defaults.get("work_modes")),
            "job_boards": form_list("job_boards", search_defaults.get("job_boards")),
            "experience_range": form_text("experience_range", search_defaults.get("experience_range")),
            "salary_target": form_text("salary_target", search_defaults.get("salary_target")),
        },
        "profile": {
            "full_name": form_text("full_name", profile_defaults.get("full_name")),
            "email": form_text("email", profile_defaults.get("email")),
            "phone": form_text("phone", profile_defaults.get("phone")),
            "current_location": form_text("current_location", profile_defaults.get("current_location")),
            "years_experience": form_text("years_experience", profile_defaults.get("years_experience")),
            "notice_period": form_text("notice_period", profile_defaults.get("notice_period")),
            "work_authorization": form_text("work_authorization", profile_defaults.get("work_authorization")),
            "linkedin_url": form_text("linkedin_url", profile_defaults.get("linkedin_url")),
            "portfolio_url": form_text("portfolio_url", profile_defaults.get("portfolio_url")),
            "summary": form_text("summary", profile_defaults.get("summary")),
            "top_skills": form_list("top_skills", profile_defaults.get("top_skills")),
        },
        "accounts": {
            "gmail_address": form_text("gmail_address", account_defaults.get("gmail_address")),
            "linkedin_username": form_text("linkedin_username", account_defaults.get("linkedin_username")),
            "indeed_email": form_text("indeed_email", account_defaults.get("indeed_email")),
            "naukri_email": form_text("naukri_email", account_defaults.get("naukri_email")),
            "browser_profile": form_text("browser_profile", account_defaults.get("browser_profile")),
            "verification_notes": form_text("verification_notes", account_defaults.get("verification_notes")),
            "use_gmail": form_bool("use_gmail", account_defaults.get("use_gmail", True)),
            "use_linkedin": form_bool("use_linkedin", account_defaults.get("use_linkedin", True)),
            "use_indeed": form_bool("use_indeed", account_defaults.get("use_indeed", True)),
            "use_naukri": form_bool("use_naukri", account_defaults.get("use_naukri", True)),
        },
        "automation": {
            "enabled": form_bool("enabled", automation_defaults.get("enabled", True)),
            "require_review": form_bool("require_review", automation_defaults.get("require_review", True)),
            "store_answers": form_bool("store_answers", automation_defaults.get("store_answers", True)),
            "max_applications_per_run": form_int("max_applications_per_run", automation_defaults.get("max_applications_per_run", 20), min_value=1, max_value=250),
            "scan_interval_minutes": form_int("scan_interval_minutes", automation_defaults.get("scan_interval_minutes", 180), min_value=15, max_value=1440),
            "cooldown_hours": form_int("cooldown_hours", automation_defaults.get("cooldown_hours", 12), min_value=1, max_value=168),
            "trigger_note": form_text("trigger_note", automation_defaults.get("trigger_note")),
        },
        "scanner": {
            "query": form_text("scan_query", scanner_defaults.get("query")),
            "keywords": form_text("scan_keywords", scanner_defaults.get("keywords")),
            "companies": form_text("scan_companies", scanner_defaults.get("companies")),
            "locations": form_text("scan_locations", scanner_defaults.get("locations")),
            "urls": form_text("scan_urls", scanner_defaults.get("urls")),
            "sources": form_text("scan_sources", scanner_defaults.get("sources")),
            "strategy": form_text("scan_strategy", scanner_defaults.get("strategy", DEFAULT_AUTO_APPLY_SCAN_STRATEGY)),
            "limit_per_source": form_text("scan_limit_per_source", scanner_defaults.get("limit_per_source", "40")),
            "max_pages": form_text("scan_max_pages", scanner_defaults.get("max_pages", "2")),
        },
    }


def auto_apply_profile_completion(settings):
    profile = settings.get("profile", {})
    checks = [
        bool(profile.get("full_name")),
        bool(profile.get("email")),
        bool(profile.get("phone")),
        bool(profile.get("current_location")),
        bool(profile.get("years_experience")),
        bool(profile.get("linkedin_url")),
        bool(profile.get("summary")),
    ]
    return int(round((sum(1 for item in checks if item) / len(checks)) * 100))


def get_auto_apply_platform_statuses(settings):
    accounts = settings.get("accounts", {})
    connectors = get_auto_apply_connector_credentials()
    email_cfg = get_email_cfg()
    gmail_credentials = resolve_app_path(email_cfg.get("credentials_path"))
    gmail_token = resolve_app_path(email_cfg.get("token_path"))
    gmail_has_config = bool(
        (gmail_credentials and gmail_credentials.exists())
        or (email_cfg.get("client_id") and email_cfg.get("client_secret"))
    )
    gmail_connected = bool(gmail_has_config and gmail_token and gmail_token.exists())
    linkedin_connected = bool(connectors["linkedin"]["username"] and connectors["linkedin"]["password"])

    statuses = []
    if gmail_connected:
        statuses.append(
            {
                "key": "gmail",
                "label": AUTO_APPLY_PLATFORM_LABELS["gmail"],
                "state": "connected",
                "value": accounts.get("gmail_address") or "OAuth token detected",
                "detail": "Gmail verification can reuse the saved OAuth token.",
                "enabled": bool(accounts.get("use_gmail", True)),
            }
        )
    elif gmail_has_config:
        statuses.append(
            {
                "key": "gmail",
                "label": AUTO_APPLY_PLATFORM_LABELS["gmail"],
                "state": "attention",
                "value": accounts.get("gmail_address") or "Credentials configured",
                "detail": "OAuth credentials exist, but the verification token still needs to be completed once.",
                "enabled": bool(accounts.get("use_gmail", True)),
            }
        )
    else:
        statuses.append(
            {
                "key": "gmail",
                "label": AUTO_APPLY_PLATFORM_LABELS["gmail"],
                "state": "missing",
                "value": accounts.get("gmail_address") or "Not connected",
                "detail": "Add Gmail OAuth credentials in .env before using automated verification.",
                "enabled": bool(accounts.get("use_gmail", True)),
            }
        )

    for key, account_value, connected in [
        ("linkedin", accounts.get("linkedin_username"), linkedin_connected),
        ("indeed", accounts.get("indeed_email"), bool(connectors["indeed"]["username"] and connectors["indeed"]["password"])),
        ("naukri", accounts.get("naukri_email"), bool(connectors["naukri"]["username"] and connectors["naukri"]["password"])),
    ]:
        if connected:
            state = "connected"
            detail = "Environment credentials are already present for this platform."
        elif account_value:
            state = "attention"
            detail = "Account details are saved, but the current runner still needs platform credentials in .env."
        else:
            state = "missing"
            detail = "No account identifier saved yet."
        statuses.append(
            {
                "key": key,
                "label": AUTO_APPLY_PLATFORM_LABELS[key],
                "state": state,
                "value": account_value or "Not connected",
                "detail": detail,
                "enabled": bool(accounts.get(f"use_{key}", True)),
            }
        )
    return statuses


def build_auto_apply_target_summary(settings):
    search = settings.get("search", {})
    role_count = len(search.get("roles") or [])
    company_count = len(search.get("companies") or [])
    location_count = len(search.get("locations") or [])
    keyword_count = len(search.get("keywords") or [])
    return (
        f"{role_count or 0} roles, {company_count or 0} companies, "
        f"{location_count or 0} locations, {keyword_count or 0} keywords"
    )


def validate_auto_apply_settings(settings):
    search = settings.get("search", {})
    profile = settings.get("profile", {})
    issues = []
    if not (search.get("keywords") or search.get("roles") or search.get("companies")):
        issues.append("Add at least one keyword, role, or company before triggering auto-apply.")
    if not profile.get("full_name"):
        issues.append("Add your full name in the candidate profile.")
    if not profile.get("email"):
        issues.append("Add your primary email in the candidate profile.")
    return issues


def get_auto_apply_summary(settings=None, history=None):
    settings = settings or load_auto_apply_settings()
    history = history if history is not None else load_auto_apply_history(limit=5)
    statuses = get_auto_apply_platform_statuses(settings)
    ready_count = sum(
        1
        for item in statuses
        if item["key"] in AUTO_APPLY_EXECUTION_KEYS and item["state"] == "connected"
    )
    active_count = sum(
        1
        for item in statuses
        if item["key"] in AUTO_APPLY_EXECUTION_KEYS and item.get("enabled")
    )
    last_run = history[0] if history else None
    return {
        "profile_completion": auto_apply_profile_completion(settings),
        "ready_platforms": ready_count,
        "active_platforms": active_count,
        "target_summary": build_auto_apply_target_summary(settings),
        "saved_runs": len(load_auto_apply_history()),
        "last_run_status": last_run.get("status_label", "No triggers yet") if last_run else "No triggers yet",
        "last_run_timestamp": last_run.get("timestamp", "") if last_run else "",
    }


def get_auto_apply_workspace_metrics(history=None, scan_history=None):
    history = history if history is not None else load_auto_apply_history(limit=20)
    total_history = load_auto_apply_history()
    scan_history = scan_history if scan_history is not None else list_scan_history(limit=20)
    total_scan_history = list_scan_history(limit=200)
    latest_scan_count = 0
    latest_scan_time = ""
    latest_scan_file = latest_master_quality_file()
    if latest_scan_file:
        try:
            latest_scan_count = len(read_dataframe_file(latest_scan_file))
            latest_scan_time = datetime.fromtimestamp(latest_scan_file.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            latest_scan_count = 0
            latest_scan_time = ""

    latest_run_shortlisted = history[0].get("selected_count", 0) if history else 0
    total_applied = 0
    total_prepared = 0
    last_apply_time = ""
    for item in total_history:
        run_id = str(item.get("id", "") or "").strip()
        if not run_id:
            continue
        run = load_auto_apply_run(run_id)
        if not isinstance(run, dict):
            continue
        execution = run.get("last_execution") if isinstance(run.get("last_execution"), dict) else {}
        total_applied += int(execution.get("submitted", 0) or 0)
        total_prepared += int(execution.get("prepared", 0) or 0)
        if not last_apply_time and execution.get("timestamp"):
            last_apply_time = execution.get("timestamp")

    return {
        "latest_scan_found": latest_scan_count,
        "latest_scan_time": latest_scan_time,
        "latest_run_shortlisted": latest_run_shortlisted,
        "submitted_total": total_applied,
        "prepared_total": total_prepared,
        "saved_scans": len(total_scan_history),
        "saved_runs": len(total_history),
        "last_apply_time": last_apply_time,
    }


def build_scan_keywords():
    keywords_raw = os.getenv("KEYWORDS", "")
    keywords = [k.strip().lower() for k in keywords_raw.split(",") if k.strip()]
    if keywords:
        return keywords
    return ["hiring", "recruiting", "apply", "job", "opening", "position", "role", "career"]


def build_scan_run_label(query="", keywords=None, companies=None):
    parts = []
    if query:
        parts.append((query or "").strip())
    for item in keywords or []:
        text = str(item or "").strip()
        if text and text.lower() not in {part.lower() for part in parts}:
            parts.append(text)
        if len(parts) >= 3:
            break
    if not parts:
        for item in companies or []:
            text = str(item or "").strip()
            if text:
                parts.append(text)
            if len(parts) >= 2:
                break
    label = " ".join(parts).strip()
    return label or "job_scan"


def queue_scan_job(query, companies_raw, min_posts, max_scrolls):
    query = (query or "").strip()
    companies_raw = (companies_raw or "").strip()
    username = os.getenv("LINKEDIN_USERNAME", "")
    password = os.getenv("LINKEDIN_PASSWORD", "")
    headless = os.getenv("DEFAULT_HEADLESS", "0") == "1"

    if not query and not companies_raw:
        return {"error": "Enter a search query or a list of companies."}
    if not username or not password:
        return {"error": "Set LINKEDIN_USERNAME and LINKEDIN_PASSWORD in .env."}

    companies = [c.strip() for c in companies_raw.split(",") if c.strip()]
    if companies and not query:
        query = "hiring {company}"

    keywords = build_scan_keywords()
    job_id = uuid.uuid4().hex
    JOBS[job_id] = {
        "status": "Queued.",
        "done": False,
        "error": None,
        "files": {},
        "no_results": False,
        "raw_rows": 0,
        "quality_rows": 0,
        "current_company": "",
        "company_index": 0,
        "company_total": len(companies) if companies else 1,
        "updated_at": datetime.now().strftime("%H:%M:%S"),
    }

    thread = threading.Thread(
        target=job_worker,
        args=(job_id, query, companies or [""], username, password, min_posts, headless, keywords, max_scrolls, None),
        daemon=True,
    )
    thread.start()
    return {"job_id": job_id}


def resolve_auto_apply_scan_strategy(scan_strategy, companies, source_names="", custom_urls=None):
    strategy_key = DEFAULT_AUTO_APPLY_SCAN_STRATEGY
    strategy = AUTO_APPLY_SCAN_STRATEGIES[strategy_key]
    explicit_sources = []
    custom_urls = split_url_text(custom_urls)
    reference_urls = []
    if strategy.get("use_reference_urls") and not (strategy.get("direct_urls_only") and custom_urls):
        reference_urls = discover_reference_urls_for_companies(companies)
    combined_urls = []
    seen_urls = set()
    for url in custom_urls + reference_urls:
        lowered = url.lower()
        if lowered in seen_urls:
            continue
        seen_urls.add(lowered)
        combined_urls.append(url)

    inferred_sources = infer_scan_sources_from_urls(combined_urls)
    if explicit_sources:
        resolved_sources = explicit_sources[:]
        for source in inferred_sources:
            if source not in resolved_sources:
                resolved_sources.append(source)
    else:
        resolved_sources = inferred_sources or AUTO_APPLY_SUPPORTED_SOURCES[:]
    return strategy_key, strategy, resolved_sources, combined_urls


def queue_universal_scan_job(query, keywords, companies_raw, locations_raw, career_urls_raw, source_names, limit_per_source, max_pages, scan_strategy=DEFAULT_AUTO_APPLY_SCAN_STRATEGY):
    keywords = split_multivalue_text(keywords)
    companies = split_multivalue_text(companies_raw)
    companies = sanitize_scanner_company_filters(query, keywords, companies)
    locations = split_multivalue_text(locations_raw)
    custom_urls = split_url_text(career_urls_raw)
    strategy_key, strategy, resolved_sources, career_urls = resolve_auto_apply_scan_strategy(scan_strategy, companies, source_names, custom_urls)
    scan_label = build_scan_run_label(query=query, keywords=keywords, companies=companies)

    if not (query or keywords or companies or career_urls):
        return {"error": "Add a search query, keywords, companies, or pasted URLs before running the universal scan."}
    if not resolved_sources:
        resolved_sources = strategy["sources"][:]
    direct_urls_only = bool(strategy.get("direct_urls_only"))

    progress_total = len(career_urls) if direct_urls_only and career_urls else (len(resolved_sources) if resolved_sources else 1)

    job_id = uuid.uuid4().hex
    JOBS[job_id] = {
        "status": "Queued.",
        "done": False,
        "error": None,
        "files": {},
        "no_results": False,
        "raw_rows": 0,
        "quality_rows": 0,
        "current_company": "",
        "company_index": 0,
        "company_total": progress_total,
        "updated_at": datetime.now().strftime("%H:%M:%S"),
        "scan_mode": "universal",
        "scan_label": scan_label,
        "source_names": resolved_sources,
        "source_counts": {},
        "resolved_targets": [],
        "blocked_urls": [],
        "unsupported_urls": [],
        "unsupported_count": 0,
        "resolved_url_count": 0,
        "reference_url_count": len(career_urls),
        "scan_strategy": strategy_key,
        "scan_strategy_label": strategy["label"],
        "direct_urls_only": direct_urls_only,
    }

    thread = threading.Thread(
        target=universal_job_worker,
        args=(job_id, scan_label, query, keywords, companies, locations, career_urls, resolved_sources, limit_per_source, max_pages, direct_urls_only),
        daemon=True,
    )
    thread.start()
    return {"job_id": job_id}


def build_auto_apply_scan_defaults(settings=None, form=None):
    settings = settings or {}
    default_limit_per_source = "40"
    default_max_pages = "2"
    scanner = settings.get("scanner", {}) if isinstance(settings, dict) else {}
    if form is not None:
        def prefer_form(name, fallback=""):
            raw = form.get(name)
            if raw is None:
                return str(fallback or "").strip()
            text = str(raw).strip()
            return text if text else str(fallback or "").strip()

        return {
            "query": prefer_form("scan_query", scanner.get("query")),
            "keywords": prefer_form("scan_keywords", scanner.get("keywords")),
            "companies": prefer_form("scan_companies", scanner.get("companies")),
            "locations": prefer_form("scan_locations", scanner.get("locations")),
            "urls": prefer_form("scan_urls", scanner.get("urls")),
            "sources": prefer_form("scan_sources", scanner.get("sources")),
            "strategy": prefer_form("scan_strategy", scanner.get("strategy") or DEFAULT_AUTO_APPLY_SCAN_STRATEGY).lower(),
            "limit_per_source": prefer_form("scan_limit_per_source", scanner.get("limit_per_source") or default_limit_per_source),
            "max_pages": prefer_form("scan_max_pages", scanner.get("max_pages") or default_max_pages),
        }

    if scanner:
        return {
            "query": str(scanner.get("query") or "").strip(),
            "keywords": str(scanner.get("keywords") or "").strip(),
            "companies": str(scanner.get("companies") or "").strip(),
            "locations": str(scanner.get("locations") or "").strip(),
            "urls": str(scanner.get("urls") or "").strip(),
            "sources": str(scanner.get("sources") or "").strip(),
            "strategy": str(scanner.get("strategy") or DEFAULT_AUTO_APPLY_SCAN_STRATEGY).strip().lower(),
            "limit_per_source": str(scanner.get("limit_per_source") or default_limit_per_source).strip(),
            "max_pages": str(scanner.get("max_pages") or default_max_pages).strip(),
        }

    search = settings.get("search", {}) if isinstance(settings, dict) else {}
    roles = [item for item in (search.get("roles") or []) if item]
    keywords = [item for item in (search.get("keywords") or []) if item]
    query_parts = []
    if roles:
        query_parts.append(roles[0])
    for item in keywords:
        lowered = item.lower()
        if lowered not in {part.lower() for part in query_parts}:
            query_parts.append(item)
        if len(query_parts) >= 3:
            break
    query = " ".join(query_parts).strip() if query_parts else ""

    return {
        "query": query,
        "keywords": ", ".join(search.get("keywords") or []),
        "companies": ", ".join(search.get("companies") or []),
        "locations": ", ".join(search.get("locations") or []),
        "urls": "",
        "sources": "",
        "strategy": DEFAULT_AUTO_APPLY_SCAN_STRATEGY,
        "limit_per_source": default_limit_per_source,
        "max_pages": default_max_pages,
    }


def save_auto_apply_scan_defaults(settings, scan_defaults):
    settings = merge_with_defaults(settings or {}, auto_apply_default_settings())
    existing_scanner = settings.get("scanner", {}) if isinstance(settings.get("scanner"), dict) else {}
    scanner_payload = {
        "query": (scan_defaults.get("query") or "").strip(),
        "keywords": (scan_defaults.get("keywords") or "").strip(),
        "companies": (scan_defaults.get("companies") or "").strip(),
        "locations": (scan_defaults.get("locations") or "").strip(),
        "urls": (scan_defaults.get("urls") or "").strip(),
        "sources": (scan_defaults.get("sources") or "").strip(),
        "strategy": (scan_defaults.get("strategy") or DEFAULT_AUTO_APPLY_SCAN_STRATEGY).strip().lower(),
        "limit_per_source": str(scan_defaults.get("limit_per_source") or "40").strip(),
        "max_pages": str(scan_defaults.get("max_pages") or "2").strip(),
        "last_unsupported_report_xlsx": str(existing_scanner.get("last_unsupported_report_xlsx") or "").strip(),
        "last_unsupported_report_csv": str(existing_scanner.get("last_unsupported_report_csv") or "").strip(),
    }
    settings["scanner"] = scanner_payload
    return save_auto_apply_settings(settings)


def normalize_match_text(value):
    text = str(value or "").lower()
    text = re.sub(r"[^a-z0-9+#&/._-]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def match_phrases(text, phrases):
    haystack = f" {normalize_match_text(text)} "
    hits = []
    for phrase in phrases or []:
        normalized = normalize_match_text(phrase)
        if normalized and f" {normalized} " in haystack and phrase not in hits:
            hits.append(phrase)
    return hits


def split_link_values(value):
    parts = re.split(r"[;\n,]+", str(value or ""))
    out = []
    seen = set()
    for part in parts:
        item = part.strip()
        if item and item not in seen:
            out.append(item)
            seen.add(item)
    return out


def build_auto_apply_opportunities(source_path: Path):
    df = read_dataframe_file(source_path)
    opportunities = []
    for idx, row in df.iterrows():
        post_text = str(row.get("Post Text", "") or "").strip()
        company = str(row.get("Company", "") or "").strip()
        all_links = split_link_values(row.get("All Links", ""))
        apply_links = split_link_values(row.get("Apply Links", ""))
        emails = extract_emails(f"{row.get('Emails', '') or ''} {post_text} {' '.join(all_links)}")
        post_link = str(row.get("Post Link", "") or "").strip()
        if not post_link:
            for link in all_links:
                if "linkedin.com/feed/update" in link or "/posts/" in link or "/activity/" in link:
                    post_link = link
                    break

        quality_raw = row.get("Quality Score", 0)
        quality_score = int(quality_raw) if pd.notna(quality_raw) else 0
        date_raw = row.get("Date", "")
        date_text = "" if pd.isna(date_raw) else str(date_raw).strip()
        role_raw = row.get("Role", "")
        role = "" if pd.isna(role_raw) else str(role_raw).strip()
        if not role:
            role = extract_role_from_post(post_text)

        opportunities.append(
            {
                "row_id": str(idx + 1),
                "company": company,
                "role": role,
                "date": date_text,
                "post_text": post_text,
                "post_excerpt": _clean_sentence(post_text, max_len=220),
                "post_link": post_link,
                "apply_links": apply_links,
                "emails": emails,
                "all_links": all_links,
                "quality_score": quality_score,
                "quality_reasons": str(row.get("Quality Reasons", "") or "").strip(),
            }
        )
    return opportunities


def score_auto_apply_opportunity(opportunity, settings):
    search = settings.get("search", {})
    company = opportunity.get("company", "")
    role = opportunity.get("role", "")
    post_text = opportunity.get("post_text", "")
    apply_links = opportunity.get("apply_links", [])
    emails = opportunity.get("emails", [])

    text_blob = " ".join([company, role, post_text, " ".join(apply_links)])
    company_blob = " ".join([company, post_text])

    exclude_company_hits = match_phrases(company_blob, search.get("exclude_companies") or [])
    exclude_keyword_hits = match_phrases(text_blob, search.get("exclude_keywords") or [])
    if exclude_company_hits or exclude_keyword_hits:
        return None

    role_hits = match_phrases(" ".join([role, post_text]), search.get("roles") or [])
    keyword_hits = match_phrases(text_blob, search.get("keywords") or [])
    company_hits = match_phrases(company_blob, search.get("companies") or [])
    location_hits = match_phrases(post_text, search.get("locations") or [])
    work_mode_hits = match_phrases(post_text, search.get("work_modes") or [])

    components = []
    for weight, values, hits in [
        (35, search.get("roles") or [], role_hits),
        (28, search.get("keywords") or [], keyword_hits),
        (20, search.get("companies") or [], company_hits),
        (12, search.get("locations") or [], location_hits),
        (5, search.get("work_modes") or [], work_mode_hits),
    ]:
        if values:
            components.append((weight, len(hits) / len(values)))

    primary_filters = (search.get("roles") or []) + (search.get("keywords") or []) + (search.get("companies") or [])
    primary_hits = len(role_hits) + len(keyword_hits) + len(company_hits)
    if primary_filters and primary_hits == 0:
        return None
    if not components:
        return None

    total_weight = sum(weight for weight, _ in components)
    fit_score = int(round((sum(weight * ratio for weight, ratio in components) / total_weight) * 100))
    if fit_score < 30:
        return None

    if apply_links:
        action = "apply_link"
        action_label = "Open apply link"
    elif emails:
        action = "email_followup"
        action_label = "Email recruiter"
    else:
        action = "manual_review"
        action_label = "Manual review"

    reasons = []
    if role_hits:
        reasons.append(f"Role match: {', '.join(role_hits[:3])}")
    if keyword_hits:
        reasons.append(f"Keyword match: {', '.join(keyword_hits[:4])}")
    if company_hits:
        reasons.append(f"Company match: {', '.join(company_hits[:3])}")
    if location_hits:
        reasons.append(f"Location match: {', '.join(location_hits[:3])}")
    if work_mode_hits:
        reasons.append(f"Work mode: {', '.join(work_mode_hits[:2])}")
    if apply_links:
        reasons.append(f"{len(apply_links)} apply link(s)")
    if emails:
        reasons.append(f"{len(emails)} recruiter email(s)")

    enriched = dict(opportunity)
    enriched.update(
        {
            "fit_score": fit_score,
            "action": action,
            "action_label": action_label,
            "matched_roles": role_hits,
            "matched_keywords": keyword_hits,
            "matched_companies": company_hits,
            "matched_locations": location_hits,
            "matched_work_modes": work_mode_hits,
            "reason_summary": reasons,
        }
    )
    return enriched


def export_auto_apply_matches(run_id, matches):
    if not matches:
        return {}
    export_rows = []
    for item in matches:
        export_rows.append(
            {
                "Fit Score": item.get("fit_score", 0),
                "Action": item.get("action_label", ""),
                "Company": item.get("company", ""),
                "Role": item.get("role", ""),
                "Matched Roles": ", ".join(item.get("matched_roles") or []),
                "Matched Keywords": ", ".join(item.get("matched_keywords") or []),
                "Matched Companies": ", ".join(item.get("matched_companies") or []),
                "Matched Locations": ", ".join(item.get("matched_locations") or []),
                "Apply Links": "; ".join(item.get("apply_links") or []),
                "Recruiter Emails": "; ".join(item.get("emails") or []),
                "Post Link": item.get("post_link", ""),
                "Post Excerpt": item.get("post_excerpt", ""),
                "Reasons": " | ".join(item.get("reason_summary") or []),
            }
        )
    df = pd.DataFrame(export_rows)
    base_name = f"auto_apply_run_{run_id}_matches"
    xlsx_path = AUTO_APPLY_DIR / f"{base_name}.xlsx"
    csv_path = AUTO_APPLY_DIR / f"{base_name}.csv"
    df.to_excel(xlsx_path, index=False)
    df.to_csv(csv_path, index=False, encoding="utf-8")
    return {
        "xlsx": xlsx_path.relative_to(OUTPUT_DIR).as_posix(),
        "csv": csv_path.relative_to(OUTPUT_DIR).as_posix(),
    }


def save_auto_apply_run(run):
    path = AUTO_APPLY_RUNS_DIR / f"{run['id']}.json"
    write_json_file(path, run)
    return path


def load_auto_apply_run(run_id):
    path = AUTO_APPLY_RUNS_DIR / f"{run_id}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def collect_auto_apply_companies(run):
    companies = []
    seen = set()
    for item in (run.get("matches") or []):
        company = clean_bullet_text(str(item.get("company", ""))).strip(" ,")
        if not company:
            continue
        key = company.lower()
        if key in seen:
            continue
        seen.add(key)
        companies.append(company)
    if companies:
        return companies

    search_snapshot = run.get("search_snapshot", {}) if isinstance(run.get("search_snapshot"), dict) else {}
    for company in search_snapshot.get("companies", []) or []:
        name = clean_bullet_text(str(company or "")).strip(" ,")
        if not name:
            continue
        key = name.lower()
        if key in seen:
            continue
        seen.add(key)
        companies.append(name)
    return companies


def build_auto_apply_history_files(run):
    exports = run.get("exports", {}) if isinstance(run.get("exports"), dict) else {}
    files = []
    for key, label in [("xlsx", "Shortlist Excel"), ("csv", "Shortlist CSV")]:
        relative_name = str(exports.get(key, "") or "").strip()
        if not relative_name:
            continue
        file_path = OUTPUT_DIR / Path(relative_name)
        size_kb = 0
        if file_path.exists():
            size_kb = max(1, round(file_path.stat().st_size / 1024))
        files.append(
            {
                "name": relative_name.replace("\\", "/"),
                "label": label,
                "size_kb": size_kb,
            }
        )
    return files


def normalize_auto_apply_history_item(item):
    run_id = str(item.get("id", "") or "").strip()
    if run_id:
        run = load_auto_apply_run(run_id)
        if isinstance(run, dict):
            return build_auto_apply_history_item(run)

    companies = item.get("companies") if isinstance(item.get("companies"), list) else []
    company_text = summarize_display_list(
        companies,
        empty_text=item.get("target_summary") or "No company summary saved",
    )
    files = []
    exports = item.get("exports") if isinstance(item.get("exports"), dict) else {}
    for key, label in [("xlsx", "Shortlist Excel"), ("csv", "Shortlist CSV")]:
        relative_name = str(exports.get(key, "") or "").strip()
        if not relative_name:
            continue
        file_path = OUTPUT_DIR / Path(relative_name)
        size_kb = max(1, round(file_path.stat().st_size / 1024)) if file_path.exists() else 0
        files.append(
            {
                "name": relative_name.replace("\\", "/"),
                "label": label,
                "size_kb": size_kb,
            }
        )

    normalized = dict(item)
    normalized["companies"] = companies
    normalized["company_count"] = len(companies)
    normalized["company_text"] = company_text
    normalized["files"] = files
    return normalized


def build_auto_apply_history_item(run):
    companies = collect_auto_apply_companies(run)
    return {
        "id": run.get("id"),
        "timestamp": run.get("timestamp"),
        "status": run.get("status"),
        "status_label": run.get("status_label"),
        "target_summary": run.get("target_summary"),
        "job_boards": run.get("job_boards", []),
        "max_applications": run.get("max_applications", 0),
        "mode": run.get("mode", ""),
        "ready_platforms": run.get("ready_platforms", []),
        "issues": run.get("issues", []),
        "matched_count": run.get("matched_count", 0),
        "selected_count": run.get("selected_count", 0),
        "source_file": run.get("source_file", ""),
        "companies": companies,
        "company_count": len(companies),
        "company_text": summarize_display_list(
            companies,
            empty_text=run.get("target_summary") or "No company summary saved",
        ),
        "files": build_auto_apply_history_files(run),
    }


def get_run_execution_policy(run, execution_config=None):
    execution_config = execution_config or get_auto_apply_connector_credentials()
    automation = run.get("automation_snapshot") if isinstance(run.get("automation_snapshot"), dict) else {}
    automation_enabled = bool(automation.get("enabled", True))
    require_review = bool(automation.get("require_review", True))
    env_allow_submit = bool(execution_config.get("allow_submit"))
    effective_allow_submit = automation_enabled and not require_review and env_allow_submit
    can_execute = automation_enabled and bool(run.get("matches"))

    if not automation_enabled:
        mode_note = "This run is preview-only. Enable apply flow and create a new run to execute it."
        action_label = "Execution disabled"
    elif require_review:
        mode_note = "This run will open and prefill forms, but it will stop before final submission."
        action_label = "Start Review Run"
    elif env_allow_submit:
        mode_note = "Direct submit is enabled for this run."
        action_label = "Start Apply"
    else:
        mode_note = "Direct submit is disabled in .env, so this run will prepare forms only."
        action_label = "Start Prep Run"

    return {
        "automation_enabled": automation_enabled,
        "require_review": require_review,
        "env_allow_submit": env_allow_submit,
        "effective_allow_submit": effective_allow_submit,
        "can_execute": can_execute,
        "mode_note": mode_note,
        "action_label": action_label,
    }


def queue_auto_apply_run(settings):
    issues = validate_auto_apply_settings(settings)
    statuses = get_auto_apply_platform_statuses(settings)
    enabled_statuses = [item for item in statuses if item.get("enabled")]
    ready_platforms = [
        item["label"]
        for item in enabled_statuses
        if item["key"] in AUTO_APPLY_EXECUTION_KEYS and item["state"] == "connected"
    ]
    if not ready_platforms:
        issues.append("No enabled apply platform is ready yet. Add LinkedIn, Indeed, or Naukri credentials in .env first.")

    run_id = uuid.uuid4().hex[:10]
    automation = settings.get("automation", {})
    mode = "Preview only"
    if automation.get("enabled", True):
        mode = "Review-first" if automation.get("require_review", True) else "Direct submit"

    source_path = latest_master_quality_file()
    opportunities = []
    matched = []
    selected = []
    exports = {}

    if not source_path:
        issues.append("No master quality scan is available yet. Run a scan first.")
    else:
        opportunities = build_auto_apply_opportunities(source_path)
        for opportunity in opportunities:
            scored = score_auto_apply_opportunity(opportunity, settings)
            if scored:
                matched.append(scored)
        matched.sort(key=lambda item: (-item.get("fit_score", 0), -item.get("quality_score", 0), item.get("company", "")))
        selected = matched[: automation.get("max_applications_per_run", 20)]
        if not selected:
            issues.append("No jobs in the latest scan matched the current filters.")
        else:
            exports = export_auto_apply_matches(run_id, selected)

    if selected:
        if automation.get("enabled", True) and not automation.get("require_review", True) and ready_platforms:
            status = "ready"
            status_label = "Ready to automate"
        elif automation.get("require_review", True):
            status = "ready"
            status_label = "Ready to review"
        else:
            status = "ready"
            status_label = "Matches found"
    else:
        status = "attention"
        status_label = "Needs attention"

    run = {
        "id": run_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": status,
        "status_label": status_label,
        "target_summary": build_auto_apply_target_summary(settings),
        "job_boards": settings.get("search", {}).get("job_boards", []),
        "max_applications": automation.get("max_applications_per_run", 20),
        "mode": mode,
        "ready_platforms": ready_platforms,
        "issues": issues,
        "trigger_note": automation.get("trigger_note", ""),
        "automation_snapshot": {
            "enabled": bool(automation.get("enabled", True)),
            "require_review": bool(automation.get("require_review", True)),
            "max_applications_per_run": automation.get("max_applications_per_run", 20),
        },
        "source_file": source_path.name if source_path else "",
        "source_rows": len(opportunities),
        "matched_count": len(matched),
        "selected_count": len(selected),
        "exports": exports,
        "matches": selected,
        "search_snapshot": settings.get("search", {}),
        "profile_snapshot": {
            "full_name": settings.get("profile", {}).get("full_name", ""),
            "email": settings.get("profile", {}).get("email", ""),
            "current_location": settings.get("profile", {}).get("current_location", ""),
            "years_experience": settings.get("profile", {}).get("years_experience", ""),
        },
    }

    save_auto_apply_run(run)
    history = load_auto_apply_history()
    history.insert(0, build_auto_apply_history_item(run))
    save_auto_apply_history(history)
    return run


def get_auto_apply_connector_credentials():
    resume_path = resolve_app_path(os.getenv("AUTO_APPLY_RESUME_PATH", ""))
    return {
        "linkedin": {
            "username": os.getenv("LINKEDIN_USERNAME", "").strip(),
            "password": os.getenv("LINKEDIN_PASSWORD", "").strip(),
        },
        "indeed": {
            "username": os.getenv("INDEED_EMAIL", "").strip() or os.getenv("INDEED_USERNAME", "").strip(),
            "password": os.getenv("INDEED_PASSWORD", "").strip(),
        },
        "naukri": {
            "username": os.getenv("NAUKRI_EMAIL", "").strip() or os.getenv("NAUKRI_USERNAME", "").strip(),
            "password": os.getenv("NAUKRI_PASSWORD", "").strip(),
        },
        "headless": os.getenv("AUTO_APPLY_HEADLESS", os.getenv("DEFAULT_HEADLESS", "0")).strip().lower() in {"1", "true", "yes", "on"},
        "allow_submit": os.getenv("AUTO_APPLY_ALLOW_SUBMIT", "0").strip().lower() in {"1", "true", "yes", "on"},
        "resume_path": str(resume_path) if resume_path and resume_path.exists() else "",
        "max_steps": parse_int_field(os.getenv("AUTO_APPLY_MAX_STEPS", "6"), 6, min_value=1, max_value=12),
    }


def detect_apply_platform(url):
    host = urllib.parse.urlparse(url or "").netloc.lower()
    if "linkedin.com" in host:
        return "linkedin"
    if "indeed." in host:
        return "indeed"
    if "naukri.com" in host:
        return "naukri"
    if "greenhouse.io" in host:
        return "greenhouse"
    if "lever.co" in host:
        return "lever"
    if "workday" in host or "myworkdayjobs" in host:
        return "workday"
    if "workable.com" in host:
        return "workable"
    if "icims.com" in host:
        return "icims"
    if "smartrecruiters.com" in host:
        return "smartrecruiters"
    if "successfactors." in host:
        return "successfactors"
    if "taleo.net" in host:
        return "taleo"
    if "oraclecloud.com" in host:
        return "oraclecloud"
    return "generic"


def save_auto_apply_execution(job):
    path = AUTO_APPLY_EXEC_DIR / f"{job['id']}.json"
    write_json_file(path, job)
    return path


def load_auto_apply_execution(exec_id):
    if exec_id in AUTO_APPLY_EXECUTIONS:
        return AUTO_APPLY_EXECUTIONS[exec_id]
    path = AUTO_APPLY_EXEC_DIR / f"{exec_id}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def wait_for_any_visible(driver, selectors, timeout=8):
    deadline = time.time() + timeout
    while time.time() < deadline:
        for by, selector in selectors:
            try:
                elements = driver.find_elements(by, selector)
                for element in elements:
                    if element.is_displayed():
                        return element
            except Exception:
                continue
        time.sleep(0.4)
    return None


def read_element_context(driver, element):
    try:
        return driver.execute_script(
            """
            const el = arguments[0];
            const directLabel = el.id ? document.querySelector(`label[for="${el.id.replace(/"/g, '\\"')}"]`) : null;
            const parentLabel = el.closest('label');
            const text = (node) => ((node && (node.innerText || node.textContent)) || '').trim();
            return {
              id: el.getAttribute('id') || '',
              name: el.getAttribute('name') || '',
              type: el.getAttribute('type') || '',
              tag: (el.tagName || '').toLowerCase(),
              placeholder: el.getAttribute('placeholder') || '',
              aria: el.getAttribute('aria-label') || '',
              label: text(directLabel) || text(parentLabel),
              dataAutomation: el.getAttribute('data-automation-id') || '',
              dataTestId: el.getAttribute('data-testid') || '',
              value: el.value || '',
              disabled: !!el.disabled,
            };
            """,
            element,
        )
    except Exception:
        return {
            "id": element.get_attribute("id") or "",
            "name": element.get_attribute("name") or "",
            "type": element.get_attribute("type") or "",
            "tag": (element.tag_name or "").lower(),
            "placeholder": element.get_attribute("placeholder") or "",
            "aria": element.get_attribute("aria-label") or "",
            "label": "",
            "dataAutomation": "",
            "dataTestId": "",
            "value": element.get_attribute("value") or "",
            "disabled": False,
        }


def guess_autofill_value_key(context):
    blob = normalize_match_text(
        " ".join(
            [
                context.get("label", ""),
                context.get("placeholder", ""),
                context.get("aria", ""),
                context.get("name", ""),
                context.get("id", ""),
                context.get("dataAutomation", ""),
                context.get("dataTestId", ""),
            ]
        )
    )
    if not blob:
        return ""
    checks = [
        ("first_name", ["first name", "given name"]),
        ("last_name", ["last name", "surname", "family name"]),
        ("email", ["email"]),
        ("phone", ["phone", "mobile", "contact number", "whatsapp"]),
        ("current_location", ["current location", "location", "city", "current city"]),
        ("linkedin_url", ["linkedin"]),
        ("portfolio_url", ["portfolio", "website", "personal site", "github"]),
        ("notice_period", ["notice period", "joining date", "available from"]),
        ("work_authorization", ["work authorization", "authorized", "sponsorship", "visa"]),
        ("years_experience", ["years of experience", "experience", "total experience"]),
        ("summary", ["cover letter", "summary", "about you", "why should we hire you", "motivation"]),
        ("resume_path", ["resume", "cv", "upload"]),
        ("full_name", ["full name", "name"]),
    ]
    for key, phrases in checks:
        if any(phrase in blob for phrase in phrases):
            return key
    return ""


def build_candidate_autofill_values(settings):
    profile = settings.get("profile", {})
    full_name = profile.get("full_name", "").strip()
    name_parts = full_name.split()
    first_name = name_parts[0] if name_parts else ""
    last_name = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""
    return {
        "full_name": full_name,
        "first_name": first_name,
        "last_name": last_name,
        "email": profile.get("email", "").strip(),
        "phone": profile.get("phone", "").strip(),
        "current_location": profile.get("current_location", "").strip(),
        "linkedin_url": profile.get("linkedin_url", "").strip(),
        "portfolio_url": profile.get("portfolio_url", "").strip(),
        "notice_period": profile.get("notice_period", "").strip(),
        "work_authorization": profile.get("work_authorization", "").strip(),
        "years_experience": profile.get("years_experience", "").strip(),
        "summary": profile.get("summary", "").strip(),
    }


def fill_text_like_input(element, value):
    try:
        current = (element.get_attribute("value") or "").strip()
        if current:
            return False
        element.click()
        element.clear()
        element.send_keys(value)
        return True
    except Exception:
        return False


def fill_select_input(element, value):
    try:
        select = Select(element)
        value_norm = normalize_match_text(value)
        options = [(opt.text or "", opt.get_attribute("value") or "") for opt in select.options]
        for idx, (text, raw_value) in enumerate(options):
            blob = normalize_match_text(f"{text} {raw_value}")
            if value_norm and value_norm in blob:
                select.select_by_index(idx)
                return True
        return False
    except Exception:
        return False


def autofill_application_fields(driver, settings, resume_path=""):
    values = build_candidate_autofill_values(settings)
    filled = 0
    uploaded_resume = False
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "input, textarea, select")
    except Exception:
        elements = []

    for element in elements:
        try:
            if not element.is_displayed():
                continue
        except Exception:
            continue

        context = read_element_context(driver, element)
        if context.get("disabled"):
            continue

        tag = context.get("tag", "")
        input_type = (context.get("type") or "").lower()
        field_key = guess_autofill_value_key(context)

        if input_type == "file" and resume_path:
            try:
                element.send_keys(resume_path)
                uploaded_resume = True
            except Exception:
                pass
            continue

        value = values.get(field_key, "")
        if not value:
            continue

        if tag == "select":
            if fill_select_input(element, value):
                filled += 1
            continue

        if input_type in {"hidden", "checkbox", "radio", "submit", "button"}:
            continue
        if input_type == "file":
            continue

        if fill_text_like_input(element, value):
            filled += 1

    return filled, uploaded_resume


def button_matches_terms(text, terms):
    normalized = normalize_match_text(text)
    return any(term in normalized for term in terms)


def click_first_button_by_terms(driver, terms):
    xpath = "//button[not(@disabled)] | //input[(translate(@type,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='submit' or translate(@type,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='button') and not(@disabled)] | //a[@role='button']"
    try:
        elements = driver.find_elements(By.XPATH, xpath)
    except Exception:
        elements = []
    for element in elements:
        try:
            if not element.is_displayed():
                continue
            label = " ".join(
                [
                    element.text or "",
                    element.get_attribute("value") or "",
                    element.get_attribute("aria-label") or "",
                ]
            )
            if button_matches_terms(label, terms):
                driver.execute_script("arguments[0].click();", element)
                return True
        except Exception:
            continue
    return False


def has_button_by_terms(driver, terms):
    xpath = "//button[not(@disabled)] | //input[(translate(@type,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='submit' or translate(@type,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='button') and not(@disabled)] | //a[@role='button']"
    try:
        elements = driver.find_elements(By.XPATH, xpath)
    except Exception:
        elements = []
    for element in elements:
        try:
            if not element.is_displayed():
                continue
            label = " ".join(
                [
                    element.text or "",
                    element.get_attribute("value") or "",
                    element.get_attribute("aria-label") or "",
                ]
            )
            if button_matches_terms(label, terms):
                return True
        except Exception:
            continue
    return False


def ensure_indeed_logged_in(driver, username, password, timeout=180, status_cb=None):
    if not username or not password:
        return False
    driver.get("https://secure.indeed.com/auth?continue=%2F")
    email_input = wait_for_any_visible(driver, [(By.CSS_SELECTOR, "input[type='email']"), (By.NAME, "__email"), (By.NAME, "email")], timeout=10)
    if email_input:
        fill_text_like_input(email_input, username)
        click_first_button_by_terms(driver, ["continue", "next", "sign in"])
        time.sleep(1.5)
    password_input = wait_for_any_visible(driver, [(By.CSS_SELECTOR, "input[type='password']"), (By.NAME, "password")], timeout=12)
    if password_input:
        fill_text_like_input(password_input, password)
        click_first_button_by_terms(driver, ["sign in", "log in", "continue"])
    start = time.time()
    while time.time() - start < timeout:
        if "auth" not in driver.current_url.lower():
            return True
        time.sleep(1)
    if status_cb:
        status_cb("Indeed login may require manual verification in the browser window.")
    return False


def ensure_naukri_logged_in(driver, username, password, timeout=180, status_cb=None):
    if not username or not password:
        return False
    driver.get("https://www.naukri.com/nlogin/login")
    username_input = wait_for_any_visible(
        driver,
        [
            (By.CSS_SELECTOR, "input[type='text']"),
            (By.CSS_SELECTOR, "input[type='email']"),
            (By.NAME, "email"),
            (By.NAME, "username"),
        ],
        timeout=10,
    )
    password_input = wait_for_any_visible(driver, [(By.CSS_SELECTOR, "input[type='password']"), (By.NAME, "password")], timeout=10)
    if username_input and password_input:
        fill_text_like_input(username_input, username)
        fill_text_like_input(password_input, password)
        click_first_button_by_terms(driver, ["login", "sign in"])
    start = time.time()
    while time.time() - start < timeout:
        if "/nlogin/login" not in driver.current_url.lower():
            return True
        time.sleep(1)
    if status_cb:
        status_cb("Naukri login may require manual verification in the browser window.")
    return False


def ensure_platform_session(driver, platform, creds, status_cb=None):
    if platform == "linkedin":
        return ensure_logged_in(driver, creds["linkedin"]["username"], creds["linkedin"]["password"], status_cb=status_cb)
    if platform == "indeed":
        return ensure_indeed_logged_in(driver, creds["indeed"]["username"], creds["indeed"]["password"], status_cb=status_cb)
    if platform == "naukri":
        return ensure_naukri_logged_in(driver, creds["naukri"]["username"], creds["naukri"]["password"], status_cb=status_cb)
    return True


def execute_auto_apply_link(driver, match, settings, creds):
    apply_links = match.get("apply_links") or []
    target_url = apply_links[0] if apply_links else (match.get("post_link") or "")
    if not target_url:
        return {
            "company": match.get("company", ""),
            "role": match.get("role", ""),
            "platform": "none",
            "status": "skipped",
            "message": "No actionable application URL was available for this opportunity.",
            "url": "",
        }

    platform = detect_apply_platform(target_url)
    ensure_platform_session(driver, platform, creds)
    driver.get(target_url)
    time.sleep(2)

    # Enter the application surface if the first page requires an explicit click.
    click_first_button_by_terms(driver, ["easy apply", "apply now", "apply", "start application", "continue application"])
    time.sleep(1)

    filled_total = 0
    uploaded_resume = False
    prepared_for_submit = False
    submitted = False
    for _ in range(creds["max_steps"]):
        filled_now, uploaded_now = autofill_application_fields(driver, settings, resume_path=creds.get("resume_path", ""))
        filled_total += filled_now
        uploaded_resume = uploaded_resume or uploaded_now

        if creds.get("allow_submit") and click_first_button_by_terms(driver, ["submit application", "submit", "finish", "send application"]):
            submitted = True
            time.sleep(2)
            break

        if click_first_button_by_terms(driver, ["next", "continue", "review", "save and continue", "continue to apply"]):
            time.sleep(2)
            continue

        prepared_for_submit = has_button_by_terms(driver, ["submit application", "submit", "finish", "send application"])
        if prepared_for_submit and not creds.get("allow_submit"):
            break
        if prepared_for_submit and creds.get("allow_submit") and click_first_button_by_terms(driver, ["submit application", "submit", "finish", "send application"]):
            submitted = True
        break

    if submitted:
        status = "submitted"
        message = "Application was submitted by the automation runner."
    elif prepared_for_submit or filled_total or uploaded_resume:
        status = "prepared"
        message = "Application flow was opened and fields were filled, but final submission was not confirmed."
    else:
        status = "opened"
        message = "Application page was opened, but no form fields were confidently filled."

    return {
        "company": match.get("company", ""),
        "role": match.get("role", ""),
        "fit_score": match.get("fit_score", 0),
        "platform": platform,
        "status": status,
        "message": message,
        "url": target_url,
        "filled_fields": filled_total,
        "uploaded_resume": uploaded_resume,
        "submitted": submitted,
    }


def auto_apply_execution_worker(exec_id, run_id):
    job = AUTO_APPLY_EXECUTIONS[exec_id]
    run = load_auto_apply_run(run_id)
    settings = load_auto_apply_settings()
    creds = get_auto_apply_connector_credentials()
    creds["allow_submit"] = bool(job.get("allow_submit", False))

    def update(status):
        job["status"] = status
        job["updated_at"] = datetime.now().strftime("%H:%M:%S")
        save_auto_apply_execution(job)

    driver = None
    try:
        if not run:
            raise RuntimeError("Auto-apply run not found.")
        if not run.get("matches"):
            raise RuntimeError("This run has no shortlisted opportunities to automate.")

        update("Launching browser automation.")
        driver = get_driver(headless=bool(creds.get("headless", False)))
        results = []
        submitted = 0
        prepared = 0
        failed = 0
        skipped = 0

        for idx, match in enumerate(run.get("matches", []), start=1):
            job["current_company"] = match.get("company", "")
            job["current_role"] = match.get("role", "")
            job["completed"] = idx - 1
            update(f"Processing {idx}/{job['total']} for {job['current_company'] or 'target company'}.")
            try:
                if match.get("action") == "email_followup" and not match.get("apply_links"):
                    result = {
                        "company": match.get("company", ""),
                        "role": match.get("role", ""),
                        "fit_score": match.get("fit_score", 0),
                        "platform": "email",
                        "status": "skipped",
                        "message": "Recruiter email only; no direct application form was available.",
                        "url": "",
                        "filled_fields": 0,
                        "uploaded_resume": False,
                        "submitted": False,
                    }
                else:
                    result = execute_auto_apply_link(driver, match, settings, creds)
            except Exception as exc:
                result = {
                    "company": match.get("company", ""),
                    "role": match.get("role", ""),
                    "fit_score": match.get("fit_score", 0),
                    "platform": detect_apply_platform((match.get("apply_links") or [""])[0] if match.get("apply_links") else match.get("post_link") or ""),
                    "status": "failed",
                    "message": str(exc),
                    "url": (match.get("apply_links") or [""])[0] if match.get("apply_links") else (match.get("post_link") or ""),
                    "filled_fields": 0,
                    "uploaded_resume": False,
                    "submitted": False,
                }

            results.append(result)
            if result["status"] == "submitted":
                submitted += 1
            elif result["status"] == "prepared":
                prepared += 1
            elif result["status"] == "skipped":
                skipped += 1
            else:
                failed += 1

            job["results"] = results
            job["submitted"] = submitted
            job["prepared"] = prepared
            job["failed"] = failed
            job["skipped"] = skipped
            job["completed"] = idx
            save_auto_apply_execution(job)

        log_df = pd.DataFrame(results)
        log_path = AUTO_APPLY_EXEC_DIR / f"execution_{exec_id}.csv"
        log_df.to_csv(log_path, index=False, encoding="utf-8")
        job["log_file"] = log_path.relative_to(OUTPUT_DIR).as_posix()
        job["done"] = True
        update("Execution complete.")

        run["last_execution"] = {
            "id": exec_id,
            "timestamp": job.get("timestamp"),
            "status": job.get("status"),
            "submitted": submitted,
            "prepared": prepared,
            "failed": failed,
            "skipped": skipped,
            "log_file": job.get("log_file", ""),
        }
        save_auto_apply_run(run)
    except Exception as exc:
        job["error"] = str(exc)
        job["done"] = True
        update("Execution failed.")
    finally:
        save_auto_apply_execution(job)
        if driver:
            try:
                driver.quit()
            except Exception:
                pass


def save_resume_review(text, analysis):
    review_id = uuid.uuid4().hex
    payload = {
        "id": review_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "text": text,
        **analysis,
    }
    path = RESUME_DIR / f"{review_id}.json"
    path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")
    return review_id


def list_resume_reviews(limit=None):
    files = sorted(RESUME_DIR.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if isinstance(limit, int):
        files = files[:limit]
    items = []
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            items.append(
                {
                    "id": data.get("id"),
                    "timestamp": data.get("timestamp"),
                    "overall_score": data.get("overall_score", 0),
                    "issues_count": len(data.get("issues", [])),
                    "ats_readiness_score": data.get("ats_readiness_score", data.get("overall_score", 0)),
                    "predicted_role_family": data.get("predicted_role_family", ""),
                    "candidate_level": data.get("candidate_level", ""),
                    "missing_skills": data.get("missing_skills", []),
                    "recommended_courses": data.get("recommended_courses", []),
                }
            )
        except Exception:
            continue
    return items


def load_resume_review(review_id):
    path = RESUME_DIR / f"{review_id}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))

def load_latest_resume_review():
    files = sorted(RESUME_DIR.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        return None
    try:
        return json.loads(files[0].read_text(encoding="utf-8"))
    except Exception:
        return None


def build_resume_top_fixes(review):
    if not isinstance(review, dict):
        return []
    fixes = []
    missing_skills = review.get("missing_skills") or []
    if missing_skills:
        fixes.append(f"Add missing skills: {', '.join(missing_skills[:3])}.")

    line_reviews = [item for item in (review.get("line_reviews") or []) if item.get("status") == "needs"]
    if line_reviews:
        fixes.append(f"Rewrite {min(len(line_reviews), 4)} weak experience bullets.")

    breakdown = review.get("breakdown") or {}
    summary_score = int(pd.to_numeric(breakdown.get("Summary", 0), errors="coerce") or 0)
    if summary_score and summary_score < 70:
        fixes.append("Improve summary (too generic).")

    if len(fixes) < 3:
        for issue in review.get("issues") or []:
            text = clean_bullet_text(str(issue)).strip()
            if text and text not in fixes:
                fixes.append(text)
            if len(fixes) >= 3:
                break
    return fixes[:3]


def _score_to_level(score_10):
    if score_10 >= 8:
        return "good"
    if score_10 >= 6:
        return "warn"
    return "bad"


def build_resume_section_cards(review):
    if not isinstance(review, dict):
        return []
    breakdown = review.get("breakdown") or {}
    sections = review.get("sections") or {}
    formatting_score = int(pd.to_numeric(breakdown.get("Formatting", 0), errors="coerce") or 0)
    summary_score = int(pd.to_numeric(breakdown.get("Summary", 0), errors="coerce") or 0)
    exp_score = int(pd.to_numeric(breakdown.get("Experience", 0), errors="coerce") or 0)
    skills_score = int(pd.to_numeric(breakdown.get("Skills", 0), errors="coerce") or 0)
    projects_text = (sections.get("projects") or "").strip()
    projects_score = 70 if projects_text else 45
    cards = [
        {
            "label": "Summary",
            "score": summary_score // 10,
            "status": _score_to_level(summary_score // 10),
            "insight": "Needs clarity" if summary_score < 70 else "Clear and targeted",
        },
        {
            "label": "Experience",
            "score": exp_score // 10,
            "status": _score_to_level(exp_score // 10),
            "insight": "Add metrics" if exp_score < 80 else "Impact is visible",
        },
        {
            "label": "Skills",
            "score": skills_score // 10,
            "status": _score_to_level(skills_score // 10),
            "insight": "Missing keywords" if skills_score < 70 else "Solid coverage",
        },
        {
            "label": "Projects",
            "score": projects_score // 10,
            "status": _score_to_level(projects_score // 10),
            "insight": "Add metrics" if projects_score < 70 else "Good proof",
        },
        {
            "label": "ATS / Format",
            "score": formatting_score // 10,
            "status": _score_to_level(formatting_score // 10),
            "insight": "Keep it tight" if formatting_score < 70 else "ATS-friendly",
        },
    ]
    return cards


def build_resume_ats_snapshot(review):
    if not isinstance(review, dict):
        return {}
    text = review.get("text", "") or ""
    emails = extract_emails(text)
    phones = extract_phones(text)
    skills_list = review.get("skills_list") or []
    recommended_skills = review.get("recommended_skills") or []
    target_count = max(len(recommended_skills), 10)
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    name_guess = lines[0] if lines else ""
    if emails and name_guess and emails[0] in name_guess:
        name_guess = ""
    return {
        "name": name_guess,
        "email_found": bool(emails),
        "phone_found": bool(phones),
        "skills_detected": len(skills_list),
        "skills_target": target_count,
    }


def build_recruiter_view(review):
    if not isinstance(review, dict):
        return []
    role = review.get("predicted_role_family") or "Target role"
    level = review.get("candidate_level") or ""
    skills = review.get("skills_list") or []
    bullets = []
    if level:
        bullets.append(f"{role} candidate ({level}).")
    else:
        bullets.append(f"{role} candidate.")
    if skills:
        bullets.append(f"Key skills: {', '.join(skills[:5])}.")
    impact_line = ""
    for item in review.get("improved_bullets") or []:
        impact_line = item.get("suggestion") or ""
        if impact_line:
            break
    if impact_line:
        bullets.append(impact_line)
    return bullets[:3]


def save_linkedin_review(text, analysis):
    review_id = uuid.uuid4().hex
    payload = {
        "id": review_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "text": text,
        **analysis,
    }
    path = LINKEDIN_DIR / f"{review_id}.json"
    path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")
    return review_id


def list_linkedin_reviews(limit=None):
    files = sorted(LINKEDIN_DIR.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if isinstance(limit, int):
        files = files[:limit]
    items = []
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            items.append(
                {
                    "id": data.get("id"),
                    "timestamp": data.get("timestamp"),
                    "overall_score": data.get("overall_score", 0),
                    "issues_count": len(data.get("issues", [])),
                }
            )
        except Exception:
            continue
    return items


def load_linkedin_review(review_id):
    path = LINKEDIN_DIR / f"{review_id}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def update_linkedin_review(review_id, patch):
    path = LINKEDIN_DIR / f"{review_id}.json"
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    data.update(patch or {})
    path.write_text(json.dumps(data, ensure_ascii=True, indent=2), encoding="utf-8")
    return data


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "_", text.strip())
    cleaned = cleaned.strip("_")
    return cleaned or "search"


def paginate_items(items, page=1, per_page=20, view_all=False):
    total = len(items)
    if view_all:
        return items, 1, 1, total
    total_pages = max(1, (total + per_page - 1) // per_page)
    page = max(1, min(int(page or 1), total_pages))
    start = (page - 1) * per_page
    end = start + per_page
    return items[start:end], page, total_pages, total


def get_actual_date(date):
    today = datetime.today().strftime("%Y-%m-%d")
    current_year = datetime.today().strftime("%Y")

    def get_past_date(days=0, weeks=0, months=0, years=0):
        date_format = "%Y-%m-%d"
        dt_obj = datetime.strptime(today, date_format)
        past_date = dt_obj - relativedelta(days=days, weeks=weeks, months=months, years=years)
        return past_date.strftime(date_format)

    past_date = date or ""

    if "hour" in past_date:
        past_date = today
    elif "day" in past_date:
        past_date = get_past_date(days=int(past_date.split(" ")[0]))
    elif "week" in past_date:
        past_date = get_past_date(weeks=int(past_date.split(" ")[0]))
    elif "month" in past_date:
        past_date = get_past_date(months=int(past_date.split(" ")[0]))
    elif "year" in past_date:
        past_date = get_past_date(years=int(past_date.split(" ")[0]))
    else:
        split_date = past_date.split("-")
        if len(split_date) == 2:
            past_month, past_day = split_date
            if len(past_month) < 2:
                past_month = "0" + past_month
            if len(past_day) < 2:
                past_day = "0" + past_day
            past_date = f"{current_year}-{past_month}-{past_day}"
        elif len(split_date) == 3:
            past_month, past_day, past_year = split_date
            if len(past_month) < 2:
                past_month = "0" + past_month
            if len(past_day) < 2:
                past_day = "0" + past_day
            past_date = f"{past_year}-{past_month}-{past_day}"

    return past_date


def get_text(container, selector, attributes):
    try:
        element = container.find(selector, attributes)
        if element:
            return element.text.strip()
    except Exception:
        pass
    return ""


def get_post_text(container):
    selectors = [
        ("div", {"class": "feed-shared-update-v2__description-wrapper"}),
        ("div", {"class": "update-components-text"}),
        ("div", {"class": "feed-shared-update-v2__commentary"}),
        ("span", {"class": "break-words"}),
    ]
    for sel, attrs in selectors:
        txt = get_text(container, sel, attrs)
        if txt:
            return txt
    try:
        return container.get_text(" ", strip=True)
    except Exception:
        return ""


def get_author_name(container):
    def normalize_name(text):
        if not text:
            return ""
        name = re.sub(r"\s+", " ", text).strip()
        if not name:
            return ""
        # Drop obvious non-names
        if re.search(r"\b(follow|connect|message|view profile|linkedin)\b", name, re.I):
            return ""
        # If duplicated without separator
        if len(name) % 2 == 0:
            half = name[: len(name) // 2]
            if half == name[len(name) // 2 :]:
                name = half
        # If duplicated with spaces
        parts = name.split(" ")
        if len(parts) % 2 == 0:
            half = parts[: len(parts) // 2]
            if half == parts[len(parts) // 2 :]:
                name = " ".join(half)
        return name.strip()

    selectors = [
        ("span", {"class": "update-components-actor__name"}),
        ("span", {"class": "feed-shared-actor__name"}),
        ("span", {"class": "update-components-actor__title--link"}),
        ("span", {"class": "update-components-actor__single-line-truncate"}),
    ]
    for sel, attrs in selectors:
        try:
            el = container.find(sel, attrs)
            if el:
                text = normalize_name(el.get_text(strip=True))
                if text and len(text.split()) <= 6:
                    return text
        except Exception:
            continue
    try:
        for a in container.find_all("a", href=True):
            href = a.get("href") or ""
            if "/in/" in href or "/company/" in href:
                text = normalize_name(a.get_text(strip=True))
                if text and len(text.split()) <= 6:
                    return text
    except Exception:
        pass
    return ""


def extract_links(container):
    links = []
    try:
        for a in container.find_all("a", href=True):
            href = a["href"]
            if href and href.startswith("http"):
                links.append(href)
    except Exception:
        pass
    return list(dict.fromkeys(links))


def extract_urls_from_text(text):
    if not text:
        return []
    urls = re.findall(r"https?://[^\s)]+", text)
    return list(dict.fromkeys(urls))


def _is_valid_email(email):
    if not re.fullmatch(EMAIL_REGEX_STRICT, email, flags=re.IGNORECASE):
        return False
    domain = email.split("@", 1)[1].lower()
    labels = domain.split(".")
    if len(labels) < 2:
        return False
    tld = labels[-1]
    last_two = ".".join(labels[-2:])
    if tld in COMMON_TLDS or tld in LONG_TLDS:
        return True
    if last_two in {"co.in","org.in","gov.in","ac.in","net.in","bank.in"}:
        return True
    return False


def _clean_email_token(token):
    token = token.strip("()[]{}<>.,;:\"'!?")
    token = re.sub(r"^mailto:", "", token, flags=re.IGNORECASE)
    token = token.rstrip(").,;:!?")
    # Try trimming from end
    t = token
    while t:
        if _is_valid_email(t):
            return t
        t = t[:-1]
    # Try trimming from start
    t = token
    while t:
        if _is_valid_email(t):
            return t
        t = t[1:]
    return None


def extract_emails(text):
    if not text:
        return []
    candidates = re.findall(r"[^\s]+@[^\s]+", text)
    cleaned = []
    for cand in candidates:
        email = _clean_email_token(cand)
        if email:
            cleaned.append(email.lower())
    # de-dup while preserving order
    seen = set()
    out = []
    for e in cleaned:
        if e not in seen:
            seen.add(e)
            out.append(e)
    return out


PHONE_CANDIDATE_RE = re.compile(r"(?:\\+?\\d[\\d\\s().-]{7,}\\d)")


def extract_phones(text):
    if not text:
        return []
    candidates = PHONE_CANDIDATE_RE.findall(text)
    out = []
    for cand in candidates:
        digits = re.sub(r"\\D", "", cand)
        if len(digits) < 8 or len(digits) > 15:
            continue
        if digits.startswith("000"):
            continue
        prefix = "+" if cand.strip().startswith("+") else ""
        phone = f"{prefix}{digits}"
        if phone not in out:
            out.append(phone)
    return out


def extract_apply_links(links):
    out = []
    for link in links:
        l = link.lower()
        if any(h in l for h in APPLY_HINTS):
            out.append(link)
    return list(dict.fromkeys(out))


def normalize_export_text(text):
    return re.sub(r"\s+", " ", str(text or "")).strip()


def choose_primary_link(links):
    values = [link.strip() for link in links if str(link or "").strip()]
    return values[0] if values else ""


def infer_location_from_text(text):
    blob = normalize_export_text(text)
    if not blob:
        return ""

    patterns = [
        r"(?i)\blocations?\b\s*[:\-]\s*([A-Za-z ,/&()-]{2,80})",
        r"(?i)\bjob location\b\s*[:\-]\s*([A-Za-z ,/&()-]{2,80})",
        r"(?i)\bbased in\b\s*([A-Za-z ,/&()-]{2,80})",
    ]
    for pattern in patterns:
        match = re.search(pattern, blob)
        if match:
            candidate = normalize_export_text(match.group(1))
            candidate = re.split(r"(?i)\b(?:experience|notice period|apply|email|role|position|skills?)\b", candidate)[0].strip(" ,;-")
            if candidate:
                return candidate

    lowered = blob.lower()
    hits = []
    for location in COMMON_JOB_LOCATIONS:
        if re.search(rf"\b{re.escape(location)}\b", lowered):
            label = "work from home" if location == "work from home" else location.title()
            if label == "Bangalore":
                label = "Bengaluru"
            if label not in hits:
                hits.append(label)
    return ", ".join(hits[:4])


def infer_job_description(text):
    return normalize_export_text(text)


def humanize_platform_name(value):
    mapping = {
        "linkedin": "LinkedIn",
        "indeed": "Indeed",
        "naukri": "Naukri",
        "greenhouse": "Greenhouse",
        "lever": "Lever",
        "workday": "Workday",
        "workable": "Workable",
        "icims": "iCIMS",
        "smartrecruiters": "SmartRecruiters",
        "successfactors": "SuccessFactors",
        "taleo": "Taleo",
        "oraclecloud": "Oracle Cloud",
        "generic": "Generic ATS",
    }
    key = str(value or "").strip().lower()
    return mapping.get(key, key.replace("_", " ").title() if key else "Unknown")


def infer_platform_label(apply_links, all_links=None, post_link=""):
    links = []
    links.extend(apply_links or [])
    links.extend(all_links or [])
    if post_link:
        links.append(post_link)
    target = choose_primary_link(links)
    if not target:
        return "Unknown"
    return humanize_platform_name(detect_apply_platform(target))


def get_post_link(container):
    for attr in ["data-urn", "data-entity-urn", "data-entity-result-urn", "data-chameleon-result-urn"]:
        urn = container.get(attr, "")
        m = re.search(r"urn:li:(activity|share):(\\d+)", urn)
        if m:
            return f"https://www.linkedin.com/feed/update/urn:li:activity:{m.group(2)}/"
    try:
        for a in container.find_all("a", href=True):
            href = a["href"]
            if any(x in href for x in ["/feed/update/", "/posts/", "/activity/"]):
                return href if href.startswith("http") else f"https://www.linkedin.com{href}"
    except Exception:
        pass
    return ""


def matches_keywords(text, keywords):
    if not text:
        return False
    t = text.lower()
    return any(k in t for k in keywords)


def has_li_at_cookie(driver):
    try:
        for c in driver.get_cookies():
            if c.get("name") == "li_at" and c.get("value"):
                return True
    except Exception:
        pass
    return False


def is_linkedin_logged_in(driver):
    if has_li_at_cookie(driver):
        return True
    try:
        if driver.find_elements(By.CSS_SELECTOR, "input.search-global-typeahead__input"):
            return True
        if driver.find_elements(By.CSS_SELECTOR, "header.global-nav, nav.global-nav__nav"):
            return True
        if driver.find_elements(By.CSS_SELECTOR, ".global-nav__primary-items, a.global-nav__primary-link, button[aria-label='Search']"):
            return True
        if driver.find_elements(By.CSS_SELECTOR, "img.global-nav__me-photo, button.global-nav__me"):
            return True
        if driver.find_elements(By.CSS_SELECTOR, "input[placeholder*='Search']"):
            return True
    except Exception:
        pass
    return False


def ensure_logged_in(driver, username, password, timeout=300, status_cb=None):
    login_url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    driver.get("https://www.linkedin.com/feed/")
    if is_linkedin_logged_in(driver):
        return True

    driver.get(login_url)
    try:
        username_input = None
        password_input = None
        for sel in [(By.ID, "username"), (By.NAME, "session_key"), (By.CSS_SELECTOR, "input[name='session_key']")]:
            try:
                username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(sel))
                break
            except Exception:
                continue
        for sel in [(By.ID, "password"), (By.NAME, "session_password"), (By.CSS_SELECTOR, "input[name='session_password']")]:
            try:
                password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located(sel))
                break
            except Exception:
                continue

        if username_input and password_input:
            username_input.clear()
            username_input.send_keys(username)
            password_input.clear()
            password_input.send_keys(password)
            password_input.submit()
    except Exception:
        pass

    notified = False
    start = time.time()
    while time.time() - start < timeout:
        if is_linkedin_logged_in(driver):
            return True
        cur = driver.current_url
        if any(x in cur for x in ["/checkpoint", "/authwall", "/login"]):
            if status_cb and not notified:
                status_cb("Waiting for LinkedIn verification/2FA in the browser. Complete login in the Chrome window.")
                notified = True
        else:
            # If we're not on a login-related page and still not logged in, force login page.
            try:
                driver.get(login_url)
            except Exception:
                pass
        time.sleep(2)

    return False


def open_content_results(driver, query):
    search_url = f"https://www.linkedin.com/search/results/content/?keywords={urllib.parse.quote(query)}&origin=GLOBAL_SEARCH_HEADER"
    for _ in range(3):
        driver.get(search_url)
        time.sleep(2)
        if "/search/results/content/" in driver.current_url:
            break
        if any(x in driver.current_url for x in ["/checkpoint", "/authwall", "/login"]):
            start = time.time()
            while time.time() - start < 120:
                if is_linkedin_logged_in(driver):
                    break
                time.sleep(2)

    if "/search/results/content/" not in driver.current_url:
        driver.get("https://www.linkedin.com/feed/")
        search_box = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-global-typeahead__input, input[placeholder*='Search']"))
        )
        try:
            search_box.click()
        except Exception:
            driver.execute_script("arguments[0].focus();", search_box)
        search_box.send_keys(Keys.CONTROL, "a")
        search_box.send_keys(Keys.BACKSPACE)
        try:
            search_box.send_keys(query)
        except Exception:
            driver.execute_script(
                "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input', {bubbles:true}));",
                search_box,
                query,
            )
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)

        try:
            posts_filter = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(., 'Posts') or contains(., 'Content')] | //a[contains(@href, '/search/results/content/')]")
                )
            )
            posts_filter.click()
        except Exception:
            pass

        if "/search/results/content/" not in driver.current_url:
            driver.get(search_url)


def normalize_linkedin_url(raw_url):
    if not raw_url:
        return ""
    url = raw_url.strip()
    if not url:
        return ""

    if "linkedin.com" not in url:
        slug = url.strip("/").replace("in/", "").replace("company/", "")
        if not slug:
            return ""
        return f"https://www.linkedin.com/in/{slug}/"

    if not url.startswith("http"):
        url = "https://" + url

    try:
        parts = urllib.parse.urlparse(url)
        path = parts.path or "/"
        # Normalize to base profile/company URL
        m = re.match(r"^/(in|company)/([^/]+)", path)
        if m:
            path = f"/{m.group(1)}/{m.group(2)}/"
        clean = parts._replace(path=path, params="", query="", fragment="")
        return clean.geturl()
    except Exception:
        return url


def get_linkedin_slug(url):
    try:
        parts = urllib.parse.urlparse(url)
        path = parts.path.strip("/")
        if path.startswith("in/") or path.startswith("company/"):
            return path.split("/", 2)[1]
    except Exception:
        pass
    return ""


def open_people_results(driver, query):
    driver.get("https://www.linkedin.com/feed/")
    search_box = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-global-typeahead__input"))
    )
    try:
        search_box.click()
    except Exception:
        driver.execute_script("arguments[0].focus();", search_box)
    search_box.send_keys(Keys.CONTROL, "a")
    search_box.send_keys(Keys.BACKSPACE)
    try:
        search_box.send_keys(query)
    except Exception:
        driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input', {bubbles:true}));",
            search_box,
            query,
        )
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)

    try:
        people_filter = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'People')] | //a[contains(@href, '/search/results/people/')]")
            )
        )
        people_filter.click()
    except Exception:
        pass

    if "/search/results/people/" not in driver.current_url:
        search_url = "https://www.linkedin.com/search/results/people/?keywords=" + urllib.parse.quote(query)
        driver.get(search_url)

    try:
        link_el = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.app-aware-link[href*='/in/']"))
        )
        return link_el.get_attribute("href") or ""
    except Exception:
        return ""


def scroll_until(driver, min_posts=100, max_scrolls=None, pause_time=1.5):
    scroll_command = "window.scrollTo(0, document.documentElement.scrollHeight);"
    get_height = "return document.documentElement.scrollHeight"
    scroll_container_js = (
        "var el=document.querySelector('.scaffold-finite-scroll__content, .scaffold-finite-scroll, .search-results-container');"
        "if(el){el.scrollTop=el.scrollHeight; return el.scrollHeight;} return 0;"
    )

    def count_results():
        selectors = [
            "div[data-urn*='urn:li:activity:']",
            "div[data-entity-urn*='urn:li:activity:']",
            "li.reusable-search__result-container",
            "div.reusable-search__result-container",
        ]
        for sel in selectors:
            try:
                n = len(driver.find_elements(By.CSS_SELECTOR, sel))
                if n:
                    return n
            except Exception:
                continue
        return 0

    last_height = max(driver.execute_script(get_height) or 0, driver.execute_script(scroll_container_js) or 0)
    scrolls = 0
    no_change_count = 0

    while True:
        driver.execute_script(scroll_command)
        driver.execute_script(scroll_container_js)
        time.sleep(pause_time)
        new_height = max(driver.execute_script(get_height) or 0, driver.execute_script(scroll_container_js) or 0)
        no_change_count = no_change_count + 1 if new_height == last_height else 0
        if no_change_count >= 3 or (max_scrolls and scrolls >= max_scrolls):
            break
        last_height = new_height
        scrolls += 1

        if count_results() >= min_posts:
            break


def extract_posts_from_soup(linkedin_soup, keywords, seen):
    containers = []
    containers += linkedin_soup.find_all(attrs={"data-urn": re.compile(r"urn:li:(activity|share):")})
    containers += linkedin_soup.find_all(attrs={"data-entity-urn": re.compile(r"urn:li:(activity|share):")})
    containers += linkedin_soup.find_all(attrs={"data-entity-result-urn": re.compile(r"urn:li:(activity|share):")})
    containers += linkedin_soup.find_all(attrs={"data-chameleon-result-urn": re.compile(r"urn:li:(activity|share):")})
    if not containers:
        containers = linkedin_soup.find_all("div", {"class": "feed-shared-update-v2"})
        containers = [c for c in containers if "activity" in c.get("data-urn", "")]
    if not containers:
        containers = linkedin_soup.select("li.reusable-search__result-container, div.reusable-search__result-container, li.search-results__result-item, div.search-results__result-item")

    posts = []
    for container in containers:
        post_text = get_post_text(container)
        if not matches_keywords(post_text, keywords):
            continue
        links = extract_links(container)
        links += extract_urls_from_text(post_text)
        links = list(dict.fromkeys(links))
        emails = extract_emails(post_text)
        phones = extract_phones(post_text)
        if not links and not emails and not phones:
            continue

        author_name = get_author_name(container)
        post_date = get_text(container, "div", {"class": "ml4 mt2 text-body-xsmall t-black--light"})
        post_date = get_actual_date(post_date)
        apply_links = extract_apply_links(links)
        primary_apply_link = choose_primary_link(apply_links)
        post_link = get_post_link(container)
        role = extract_role_from_post(post_text)
        location = infer_location_from_text(post_text)
        job_description = infer_job_description(post_text)
        platform = infer_platform_label(apply_links, links, post_link)

        key = post_link or container.get("data-urn") or f"{author_name}:{post_text[:80]}"
        if key in seen:
            continue
        seen.add(key)

        posts.append(
            {
                "Date": post_date,
                "Platform": platform,
                "Role": role,
                "Location": location,
                "Primary Apply Link": primary_apply_link,
                "Job Description": job_description,
                "Post Text": post_text,
                "Post Link": post_link,
                "Apply Links": ";".join(apply_links),
                "Emails": ";".join(emails),
                "Phone Numbers": ";".join(phones),
                "Author Name": author_name,
                "All Links": ";".join(links),
            }
        )

    return posts


def scan_posts(query, username, password, min_posts, headless, keywords, max_scrolls=None, status_cb=None):
    driver = get_driver(headless=headless)
    try:
        if status_cb:
            status_cb("Logging in to LinkedIn (complete 2FA if prompted).")
        if not ensure_logged_in(driver, username, password, status_cb=status_cb):
            raise RuntimeError("LinkedIn login not completed. Please finish verification in the Chrome window and retry.")
        if status_cb:
            status_cb("Searching posts.")
        open_content_results(driver, query)
        try:
            WebDriverWait(driver, 30).until(
                lambda d: len(
                    d.find_elements(By.CSS_SELECTOR, "li.reusable-search__result-container, div.reusable-search__result-container, div.search-results-container, div.feed-shared-update-v2, div[data-urn*='urn:li:activity:']")
                ) > 0
            )
        except Exception:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        if status_cb:
            status_cb("Scrolling and collecting posts.")
        posts_data = []
        seen = set()
        scrolls = 0
        no_change_count = 0
        get_height = "return document.documentElement.scrollHeight"
        scroll_container_js = (
            "var el=document.querySelector('.scaffold-finite-scroll__content, .scaffold-finite-scroll, .search-results-container');"
            "if(el){el.scrollTop=el.scrollHeight; return el.scrollHeight;} return 0;"
        )
        last_height = max(driver.execute_script(get_height) or 0, driver.execute_script(scroll_container_js) or 0)

        while True:
            company_page = driver.page_source
            linkedin_soup = bs(company_page.encode("utf-8"), "html.parser")
            new_posts = extract_posts_from_soup(linkedin_soup, keywords, seen)
            posts_data.extend(new_posts)
            if status_cb:
                status_cb(f"Collected {len(posts_data)} posts for this company.")
            if min_posts and len(posts_data) >= min_posts:
                break

            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            driver.execute_script(scroll_container_js)
            time.sleep(1.5)
            new_height = max(driver.execute_script(get_height) or 0, driver.execute_script(scroll_container_js) or 0)
            no_change_count = no_change_count + 1 if new_height == last_height else 0
            if no_change_count >= 3 or (max_scrolls and scrolls >= max_scrolls):
                break
            last_height = new_height
            scrolls += 1

        if not posts_data:
            raise RuntimeError("No posts found. LinkedIn may have changed markup or blocked access.")

        df = pd.DataFrame(posts_data)
        return df
    finally:
        driver.quit()


def filter_quality(df, keywords):
    if df.empty:
        return df

    df = df.copy()
    for column in ["Post Text", "Post Link", "All Links", "Apply Links", "Emails", "Phone Numbers"]:
        if column not in df.columns:
            df[column] = ""

    spam_terms = [
        "giveaway", "free", "sale", "discount", "webinar", "event",
        "congratulations", "anniversary", "promo", "subscribe", "airdrop",
        "crypto", "nft", "like and share", "follow me", "dm me",
    ]

    def score_row(row):
        text = (row.get("Post Text") or "").strip()
        links = [x for x in (row.get("All Links") or "").split(";") if x]
        apply_links = [x for x in (row.get("Apply Links") or "").split(";") if x]
        emails = [x for x in (row.get("Emails") or "").split(";") if x]
        phones = [x for x in (row.get("Phone Numbers") or "").split(";") if x]

        score = 0
        reasons = []

        if apply_links:
            score += 3
            reasons.append("apply_link")
        if emails:
            score += 3
            reasons.append("email")
        if phones:
            score += 2
            reasons.append("phone")
        if matches_keywords(text, keywords):
            score += 1
            reasons.append("keyword_match")
        if len(text) < 40:
            score -= 2
            reasons.append("too_short")
        if any(term in text.lower() for term in spam_terms):
            score -= 3
            reasons.append("spam_terms")
        if len(links) > 6:
            score -= 1
            reasons.append("too_many_links")

        return score, ",".join(reasons)

    scores = df.apply(lambda r: score_row(r), axis=1, result_type="expand")
    df["Quality Score"] = scores[0]
    df["Quality Reasons"] = scores[1]
    minimum_quality_score = 4 if keywords else 3
    df["Quality"] = df["Quality Score"] >= minimum_quality_score

    # Deduplicate by Post Link or Post Text
    df = df.sort_values(by="Quality Score", ascending=False)
    df = df.drop_duplicates(subset=["Post Link", "Post Text"], keep="first")

    return df[df["Quality"]]


def _normalize_text(value):
    text = str(value or "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _normalize_terms(values):
    items = []
    seen = set()
    for value in values or []:
        text = _normalize_text(value).lower()
        if not text or text in seen:
            continue
        seen.add(text)
        items.append(text)
    return items


def _column_or_empty(df, column):
    if column in df.columns:
        return df[column].astype(str)
    return pd.Series([""] * len(df), index=df.index, dtype="object")


def _build_contains_mask(df, columns, terms):
    if df.empty:
        return pd.Series([], dtype=bool, index=df.index)
    if not terms:
        return pd.Series([True] * len(df), index=df.index)
    pattern = "|".join(re.escape(term) for term in terms if term)
    if not pattern:
        return pd.Series([True] * len(df), index=df.index)
    combined = pd.Series([""] * len(df), index=df.index, dtype="object")
    for column in columns:
        combined = combined.str.cat(_column_or_empty(df, column), sep=" ")
    return combined.str.contains(pattern, case=False, na=False)


def compiler_filter_dataframe(df, query, keywords, companies, locations):
    if df.empty:
        return df
    term_filters = _normalize_terms([query] + list(keywords or []))
    company_filters = _normalize_terms(companies)
    location_filters = _normalize_terms(locations)
    mask = pd.Series([True] * len(df), index=df.index)
    if term_filters:
        mask &= _build_contains_mask(
            df,
            ["Role", "Company", "Location", "Job Description", "Post Text"],
            term_filters,
        )
    if company_filters:
        mask &= _build_contains_mask(df, ["Company"], company_filters)
    if location_filters:
        mask &= _build_contains_mask(df, ["Location"], location_filters)
    return df[mask]


def load_public_ats_jobs(status_cb=None):
    cache_path = PUBLIC_ATS_CACHE_PATH
    cache_fresh = False
    if cache_path.exists():
        age_seconds = time.time() - cache_path.stat().st_mtime
        cache_fresh = age_seconds <= PUBLIC_ATS_CACHE_TTL_SECONDS

    if not cache_fresh:
        if callable(status_cb):
            status_cb("Downloading public ATS feed...")
        try:
            request_obj = urllib.request.Request(
                PUBLIC_ATS_FEED_URL,
                headers={"User-Agent": "Mozilla/5.0"},
            )
            with urllib.request.urlopen(request_obj, timeout=40) as response:
                data = response.read()
            cache_path.write_bytes(data)
        except Exception as exc:
            if cache_path.exists():
                if callable(status_cb):
                    status_cb("Using cached public ATS feed.")
            else:
                raise exc
    else:
        if callable(status_cb):
            status_cb("Using cached public ATS feed.")

    return pd.read_csv(cache_path)


def normalize_public_ats_dataframe(df):
    if df is None or df.empty:
        return pd.DataFrame(columns=SCAN_EXPORT_COLUMNS)
    columns = {str(col).strip().lower(): col for col in df.columns}

    def pick(*names):
        for name in names:
            if name in columns:
                return columns[name]
        return None

    title_col = pick("title", "role", "job_title", "position")
    company_col = pick("company", "organization", "employer")
    location_col = pick("location", "locations", "location_raw", "city")
    url_col = pick("url", "job_url", "apply_url", "link")
    date_col = pick("date_posted", "posted_at", "date", "published_at")

    out = pd.DataFrame()
    out["Role"] = df[title_col] if title_col else ""
    out["Company"] = df[company_col] if company_col else ""
    out["Location"] = df[location_col] if location_col else ""
    out["Date"] = df[date_col] if date_col else ""
    out["Primary Apply Link"] = df[url_col] if url_col else ""
    out["Apply Links"] = out["Primary Apply Link"]
    out["Post Link"] = out["Primary Apply Link"]
    out["Platform"] = "Public ATS"
    out["Author Name"] = out["Company"]
    out["Job Description"] = ""
    out["Post Text"] = (
        out["Role"].fillna("").astype(str)
        + " at "
        + out["Company"].fillna("").astype(str)
    ).str.strip()
    out["Emails"] = ""
    out["Phone Numbers"] = ""
    out["All Links"] = out["Primary Apply Link"]

    for col in SCAN_EXPORT_COLUMNS:
        if col not in out.columns:
            out[col] = ""

    out = out.drop_duplicates(
        subset=["Company", "Role", "Location", "Primary Apply Link"],
        keep="first",
    )
    return out


def infer_work_arrangement(text):
    value = _normalize_text(text).lower()
    if "remote" in value or "work from home" in value:
        return "Remote"
    if "hybrid" in value:
        return "Hybrid"
    if "onsite" in value or "on-site" in value or "on site" in value:
        return "On-site"
    return ""


def infer_employment_type(title):
    text = _normalize_text(title).lower()
    types = []
    if "intern" in text:
        types.append("INTERN")
    if "new grad" in text or "new graduate" in text:
        types.append("NEW_GRAD")
    if not types:
        types.append("FULL_TIME")
    return types


def build_career_feed_records(df, generated_at, keywords=None):
    records = []
    for _, row in df.iterrows():
        title = _normalize_text(row.get("Role"))
        company = _normalize_text(row.get("Company"))
        location = _normalize_text(row.get("Location"))
        apply_url = _normalize_text(row.get("Primary Apply Link") or row.get("Post Link"))
        post_link = _normalize_text(row.get("Post Link") or row.get("Primary Apply Link"))
        description = _normalize_text(row.get("Job Description") or row.get("Post Text"))
        source = _normalize_text(row.get("Platform"))
        job_id_seed = "|".join([company, title, apply_url or post_link])
        job_id = hashlib.sha256(job_id_seed.encode("utf-8")).hexdigest()[:16]

        locations_derived = []
        if location:
            parts = [part.strip() for part in location.split(",") if part.strip()]
            derived = {"raw": location}
            if parts:
                derived["city"] = parts[0]
            if len(parts) > 1:
                derived["admin"] = parts[1]
            if len(parts) > 2:
                derived["country"] = parts[-1]
            locations_derived.append(derived)

        record = {
            "id": job_id,
            "title": title,
            "organization": company,
            "organization_url": post_link or apply_url,
            "date_posted": _normalize_text(row.get("Date")),
            "date_created": generated_at,
            "locations_raw": location,
            "locations_derived": locations_derived,
            "employment_type": infer_employment_type(title),
            "url": apply_url or post_link,
            "source": source,
            "description_text": description,
            "description_html": "",
            "salary_raw": "",
            "ai_salary_minvalue": "",
            "ai_salary_maxvalue": "",
            "ai_experience_level": "",
            "ai_work_arrangement": infer_work_arrangement(" ".join([location, description])),
            "ai_key_skills": _normalize_terms(keywords),
            "linkedin_org_employees": "",
            "linkedin_org_industry": "",
        }
        records.append(record)
    return records


def build_atlas_payload(df, generated_at, query, keywords, companies, locations, source_counts):
    jobs = []
    locations_index = {}
    companies_index = {}
    platform_index = {}

    for _, row in df.iterrows():
        title = _normalize_text(row.get("Role"))
        company = _normalize_text(row.get("Company"))
        location = _normalize_text(row.get("Location")) or "Unknown"
        platform = _normalize_text(row.get("Platform")) or "Unknown"
        apply_url = _normalize_text(row.get("Primary Apply Link") or row.get("Post Link"))
        post_link = _normalize_text(row.get("Post Link") or row.get("Primary Apply Link"))
        job_id_seed = "|".join([company, title, apply_url or post_link])
        job_id = hashlib.sha256(job_id_seed.encode("utf-8")).hexdigest()[:16]

        job = {
            "id": job_id,
            "title": title,
            "company": company,
            "location": location,
            "platform": platform,
            "apply_url": apply_url,
            "post_link": post_link,
            "date_posted": _normalize_text(row.get("Date")),
            "work_arrangement": infer_work_arrangement(" ".join([location, title])),
            "employment_type": infer_employment_type(title),
        }
        jobs.append(job)
        locations_index.setdefault(location, []).append(job_id)
        companies_index.setdefault(company or "Unknown", []).append(job_id)
        platform_index.setdefault(platform, []).append(job_id)

    stats = {
        "total_jobs": len(jobs),
        "platform_counts": {k: len(v) for k, v in platform_index.items()},
        "location_counts": {k: len(v) for k, v in locations_index.items()},
        "company_counts": {k: len(v) for k, v in companies_index.items()},
    }

    return {
        "generated_at": generated_at,
        "query": query,
        "keywords": keywords or [],
        "companies": companies or [],
        "locations": locations or [],
        "source_counts": source_counts or {},
        "stats": stats,
        "jobs": jobs,
        "locations": locations_index,
        "companies": companies_index,
        "platforms": platform_index,
    }


def save_outputs(df, query, suffix, timestamp=None):
    safe_name = slugify(query)
    ts = timestamp or datetime.now().strftime("%Y%m%d_%H%M%S")
    xlsx_path = OUTPUT_DIR / f"{safe_name}_{suffix}_{ts}.xlsx"
    csv_path = OUTPUT_DIR / f"{safe_name}_{suffix}_{ts}.csv"
    df_clean = df.copy()
    ordered_cols = [col for col in SCAN_EXPORT_COLUMNS if col in df_clean.columns]
    remaining_cols = [col for col in df_clean.columns if col not in ordered_cols]
    if ordered_cols:
        df_clean = df_clean[ordered_cols + remaining_cols]
    illegal_chars = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]")
    for col in df_clean.columns:
        if df_clean[col].dtype == object:
            df_clean[col] = df_clean[col].astype(str).apply(lambda v: illegal_chars.sub("", v))
    df_clean.to_excel(xlsx_path, index=False)
    df_clean.to_csv(csv_path, index=False, encoding="utf-8")
    return xlsx_path, csv_path


def save_scan_issue_outputs(df, query, timestamp=None):
    safe_name = slugify(query)
    ts = timestamp or datetime.now().strftime("%Y%m%d_%H%M%S")
    xlsx_path = OUTPUT_DIR / f"{safe_name}_unsupported_urls_{ts}.xlsx"
    csv_path = OUTPUT_DIR / f"{safe_name}_unsupported_urls_{ts}.csv"
    df_clean = df.copy()
    ordered_cols = [
        col for col in [
            "Status",
            "Reason",
            "Input URL",
            "URL",
            "Platform",
        ] if col in df_clean.columns
    ]
    remaining_cols = [col for col in df_clean.columns if col not in ordered_cols]
    if ordered_cols:
        df_clean = df_clean[ordered_cols + remaining_cols]
    df_clean.to_excel(xlsx_path, index=False)
    df_clean.to_csv(csv_path, index=False, encoding="utf-8")
    return xlsx_path, csv_path


def latest_master_quality_file():
    return latest_output_file("*_master_quality_*.*", suffixes={".xlsx", ".csv"})


def humanize_scan_query(value):
    text = (value or "").replace("_", " ").strip()
    if not text:
        return "LinkedIn scan"
    return text.title()


def humanize_company_slug(value):
    text = (value or "").replace("_", " ").strip()
    if not text:
        return ""
    return text.title()


def list_scan_history(limit=12):
    pattern = re.compile(r"^(?P<query>.+)_master_(?P<kind>quality|raw)_(?P<ts>\d{8}_\d{6})$")
    runs = {}
    output_files = list_output_files("*.*", suffixes={".xlsx", ".csv"})

    for file_path in output_files:
        match = pattern.match(file_path.stem)
        if not match:
            continue

        query = match.group("query")
        kind = match.group("kind")
        ts = match.group("ts")
        run_id = f"{query}_{ts}"
        entry = runs.setdefault(
            run_id,
            {
                "id": run_id,
                "query": query,
                "label": humanize_scan_query(query),
                "timestamp_key": ts,
                "timestamp": datetime.strptime(ts, "%Y%m%d_%H%M%S").strftime("%Y-%m-%d %H:%M:%S"),
                "files": [],
            },
        )
        entry["files"].append(
            {
                "name": file_path.name,
                "label": f"{'Master Preferred Jobs' if kind == 'quality' else 'Master Raw'} {file_path.suffix[1:].upper()}",
                "size_kb": max(1, round(file_path.stat().st_size / 1024)),
            }
        )
        entry.setdefault("companies", set())

    for file_path in output_files:
        stem = file_path.stem
        for run_id, entry in runs.items():
            query = entry["query"]
            ts = entry["timestamp_key"]
            raw_suffix = f"_raw_{ts}"
            quality_suffix = f"_quality_{ts}"
            company = ""
            if stem.endswith(raw_suffix):
                company = stem[: -len(raw_suffix)]
            elif stem.endswith(quality_suffix):
                company = stem[: -len(quality_suffix)]
            else:
                continue
            if not company.startswith(query + "_"):
                continue
            company = company[len(query) + 1 :].strip("_")
            if company and company.lower() not in {"master", "emails_only"}:
                entry.setdefault("companies", set()).add(humanize_company_slug(company))
                entry["files"].append(
                    {
                        "name": file_path.name,
                        "label": f"{humanize_company_slug(company)} {'Preferred Jobs' if stem.endswith(quality_suffix) else 'Raw Scan'} {file_path.suffix[1:].upper()}",
                        "size_kb": max(1, round(file_path.stat().st_size / 1024)),
                    }
                )

    for entry in runs.values():
        email_prefix = f"{entry['query']}_emails_only_{entry['timestamp_key']}_"
        related_files = sorted(
            OUTPUT_DIR.glob(f"{email_prefix}*.xlsx"),
            key=lambda path: path.stat().st_mtime,
            reverse=True,
        )
        for idx, file_path in enumerate(related_files, start=1):
            entry["files"].append(
                {
                    "name": file_path.name,
                    "label": "Email-only XLSX" if idx == 1 else f"Email-only XLSX {idx}",
                    "size_kb": max(1, round(file_path.stat().st_size / 1024)),
                }
            )
        entry["files"].sort(
            key=lambda file: (
                0 if file["label"].startswith("Master Raw") else 1 if file["label"].startswith("Master Preferred Jobs") else 2 if "Preferred Jobs" in file["label"] else 3 if "Raw Scan" in file["label"] else 4,
                file["label"],
            )
        )
        entry["file_count"] = len(entry["files"])
        companies = sorted(entry.get("companies") or [])
        entry["company_count"] = len(companies)
        entry["companies"] = companies
        entry["company_text"] = summarize_display_list(companies, empty_text="No company tags found")

    items = sorted(runs.values(), key=lambda item: item["timestamp_key"], reverse=True)
    if isinstance(limit, int):
        items = items[:limit]
    return items


def build_email_only_file(file_path: Path):
    if file_path.suffix.lower() == ".csv":
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    def clean_emails(row):
        combined = f"{row.get('Emails','')} {row.get('Post Text','')} {row.get('All Links','')}"
        emails = extract_emails(str(combined))
        return ";".join(emails)

    df = df.copy()
    df["Emails"] = df.apply(clean_emails, axis=1)
    df = df[df["Emails"].astype(str).str.strip() != ""]

    safe_name = file_path.stem.replace("_master_quality", "_emails_only")
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = OUTPUT_DIR / f"{safe_name}_{ts}.xlsx"
    df.to_excel(out_path, index=False)
    return out_path


def get_or_build_email_only_file(file_path: Path):
    safe_name = file_path.stem.replace("_master_quality", "_emails_only")
    existing = latest_output_file(f"{safe_name}_*.xlsx", suffixes={".xlsx"})
    if existing:
        try:
            if existing.stat().st_mtime >= file_path.stat().st_mtime:
                return existing
        except Exception:
            pass
    return build_email_only_file(file_path)


def load_quality_rows(file_path: Path):
    if file_path.suffix.lower() == ".csv":
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)
    rows = []
    for _, row in df.iterrows():
        raw_emails = str(row.get("Emails", "") or "")
        post_text = str(row.get("Post Text", "") or "")
        all_links = str(row.get("All Links", "") or "")

        combined = f"{raw_emails} {post_text} {all_links}"
        emails = extract_emails(combined)
        if not emails:
            continue

        post_link = str(row.get("Post Link", "") or "")
        if not post_link and all_links:
            for link in re.split(r"[;,\\s]+", all_links):
                if "linkedin.com/feed/update" in link or "/posts/" in link or "/activity/" in link:
                    post_link = link
                    break

        for email in emails:
            rows.append(
                {
                    "email": email,
                    "company": str(row.get("Company", "") or ""),
                    "post_text": post_text,
                    "post_link": post_link,
                    "apply_links": str(row.get("Apply Links", "") or ""),
                    "all_links": all_links,
                }
            )
    return rows


def render_scan_file_email_page(file_name, label="", error="", success=False, back_href="/scan", back_label="Back to past scans"):
    return render_template(
        "scan_email.html",
        file_name=file_name,
        label=label,
        error=error,
        success=success,
        back_href=back_href,
        back_label=back_label,
    )


def render_template_safe(text, data):
    out = text
    for k, v in data.items():
        out = out.replace(f"{{{k}}}", v or "")
    return out


def attach_file(message, attachment_path):
    mime_type, _ = mimetypes.guess_type(attachment_path)
    if not mime_type:
        mime_type = "application/octet-stream"
    maintype, subtype = mime_type.split("/", 1)
    with open(attachment_path, "rb") as f:
        data_bytes = f.read()
    message.add_attachment(data_bytes, maintype=maintype, subtype=subtype, filename=Path(attachment_path).name)


def build_tracking_token():
    return uuid.uuid4().hex


def build_tracking_pixel_url(token):
    if not TRACKING_BASE_URL or not token:
        return ""
    return f"{TRACKING_BASE_URL}/open/{token}.png"


def build_email_html(body_txt, tracking_url):
    safe_body = html.escape(body_txt or "")
    html_body = (
        "<html><body>"
        "<div style=\"font-family:Arial, sans-serif;font-size:14px;line-height:1.5;white-space:pre-wrap;\">"
        f"{safe_body}"
        "</div>"
    )
    if tracking_url:
        html_body += f"<img src=\"{tracking_url}\" width=\"1\" height=\"1\" style=\"display:none;\" alt=\"\" />"
    html_body += "</body></html>"
    return html_body


def log_email_tracking(token, to_email, subject, source):
    if not token:
        return
    log_path = TRACKING_LOG_DIR / f"email_open_tokens_{datetime.now().strftime('%Y%m%d')}.csv"
    exists = log_path.exists()
    fields = ["timestamp", "token", "email", "subject", "source", "tracking_url"]
    row = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "token": token,
        "email": to_email,
        "subject": subject or "",
        "source": source or "",
        "tracking_url": build_tracking_pixel_url(token),
    }
    with open(log_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if not exists:
            writer.writeheader()
        writer.writerow(row)


def list_tracking_rows():
    rows = []
    for log_path in sorted(TRACKING_LOG_DIR.glob("email_open_tokens_*.csv")):
        try:
            with open(log_path, "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    token = (row.get("token") or "").strip()
                    if token:
                        rows.append(row)
        except Exception:
            continue
    return rows


def fetch_open_count_for_token(token):
    if not TRACKING_BASE_URL or not token:
        return 0
    stats_url = f"{TRACKING_BASE_URL}/stats?token={urllib.parse.quote(token)}"
    try:
        req = urllib.request.Request(
            stats_url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "application/json",
            },
        )
        with urllib.request.urlopen(req, timeout=8) as response:
            payload = json.loads(response.read().decode("utf-8"))
            return int(payload.get("opens", 0) or 0)
    except Exception:
        return 0


def get_tracking_summary():
    if not TRACKING_BASE_URL:
        return {
            "tracking_enabled": False,
            "tracked_emails": 0,
            "opened_emails": 0,
            "open_rate": 0,
            "total_open_events": 0,
            "top_open_count": 0,
            "top_open_subject": "",
            "items": [],
            "note": "Tracking disabled. Add TRACKING_BASE_URL in .env.",
        }

    rows = list_tracking_rows()
    if not rows:
        return {
            "tracking_enabled": True,
            "tracked_emails": 0,
            "opened_emails": 0,
            "open_rate": 0,
            "total_open_events": 0,
            "top_open_count": 0,
            "top_open_subject": "",
            "items": [],
            "note": "Tracking enabled. Send a tracked email to start collecting opens.",
        }

    opened = 0
    total_open_events = 0
    items = []
    top_item = None
    for row in rows:
        token = (row.get("token") or "").strip()
        opens = fetch_open_count_for_token(token)
        if opens > 0:
            opened += 1
        total_open_events += opens
        item = {
            "timestamp": (row.get("timestamp") or "").strip(),
            "email": (row.get("email") or "").strip(),
            "subject": (row.get("subject") or "").strip(),
            "source": (row.get("source") or "").strip(),
            "tracking_url": (row.get("tracking_url") or "").strip(),
            "token": token,
            "opens": opens,
            "status": "Opened" if opens > 0 else "Not opened",
        }
        items.append(item)
        if top_item is None or opens > top_item["opens"]:
            top_item = item

    tracked = len(rows)
    open_rate = round((opened / tracked) * 100) if tracked else 0
    items.sort(key=lambda item: (-item["opens"], item["timestamp"]), reverse=False)
    return {
        "tracking_enabled": True,
        "tracked_emails": tracked,
        "opened_emails": opened,
        "open_rate": open_rate,
        "total_open_events": total_open_events,
        "top_open_count": top_item["opens"] if top_item else 0,
        "top_open_subject": top_item["subject"] if top_item else "",
        "items": items,
        "note": f"{opened} opened out of {tracked} tracked emails.",
    }

EMAIL_TEMPLATES = [
    {
        "id": "targeted",
        "label": "Targeted Intro",
        "description": "Balanced intro with highlights and clear CTA.",
        "subject": "Application for {role} — {skills}",
        "body": (
            "Hello {company} Hiring Team,\n\n"
            "I am reaching out about the {role} opportunity you shared. My background aligns with your needs, "
            "especially around {skills}.\n\n"
            "Highlights:\n"
            "- {summary}\n"
            "- Impact: {achievements}\n\n"
            "If helpful, I can apply via your preferred link.\n"
            "Apply link(s): {apply_links}\n"
            "Post link: {post_link}\n\n"
            "Thank you for your time and consideration.\n"
            "{sender_name}\n"
            "{sender_contact}"
        ),
    },
    {
        "id": "direct",
        "label": "Short and Direct",
        "description": "Concise note with the essentials.",
        "subject": "{role} candidate — {skills}",
        "body": (
            "Hello {company} Hiring Team,\n\n"
            "I would like to be considered for the {role} role you posted. "
            "My experience in {skills} is a strong fit.\n\n"
            "Quick snapshot:\n"
            "- {summary}\n"
            "- Impact: {achievements}\n\n"
            "Resume attached. Happy to apply through your link.\n"
            "Apply link(s): {apply_links}\n\n"
            "Regards,\n"
            "{sender_name}\n"
            "{sender_contact}"
        ),
    },
    {
        "id": "referral",
        "label": "Referral Ask",
        "description": "Polite ask for referral or the right contact.",
        "subject": "Referral for {role} — {skills}",
        "body": (
            "Hello {company} Hiring Team,\n\n"
            "I noticed the {role} opening and would appreciate a referral or the best contact to apply. "
            "My background in {skills} aligns well with the role.\n\n"
            "Proof points:\n"
            "- {summary}\n"
            "- Impact: {achievements}\n\n"
            "If there is a preferred process, I will apply there.\n"
            "Apply link(s): {apply_links}\n"
            "Post link: {post_link}\n\n"
            "Thanks in advance,\n"
            "{sender_name}\n"
            "{sender_contact}"
        ),
    },
]

EMAIL_TOKENS = [
    "{company}",
    "{role}",
    "{skills}",
    "{summary}",
    "{achievements}",
    "{apply_links}",
    "{post_link}",
    "{sender_name}",
    "{sender_contact}",
]

DEFAULT_EMAIL_TEMPLATE_ID = "targeted"


def get_email_template(template_id):
    for template in EMAIL_TEMPLATES:
        if template["id"] == template_id:
            return template
    return EMAIL_TEMPLATES[0]


def build_email_context(rec, resume_profile, sender_name, sender_contact):
    post_text = rec.get("post_text", "")
    role = extract_role_from_post(post_text) or "open roles"
    post_keywords = extract_keywords(post_text, limit=6)
    skills = resume_profile.get("skills") or []
    skill_overlap = [k for k in skills if k in post_keywords][:4]
    skills_line = ", ".join(skill_overlap or skills[:4])
    achievements = resume_profile.get("achievements") or []
    achievements_line = "; ".join(achievements[:2])
    summary_line = resume_profile.get("summary") or ""
    if not summary_line:
        summary_line = "Resume attached highlighting relevant experience."

    company = rec.get("company", "").strip() or "Hiring Team"
    context = {
        "company": company,
        "role": role,
        "skills": skills_line,
        "summary": summary_line,
        "achievements": achievements_line,
        "apply_links": rec.get("apply_links", "").strip(),
        "post_link": rec.get("post_link", "").strip(),
        "sender_name": sender_name or "Your Name",
        "sender_contact": sender_contact or "",
    }
    return context


def render_email_template(template, context):
    rendered = template or ""
    for key, value in context.items():
        rendered = rendered.replace("{" + key + "}", value or "")

    rendered = re.sub(r"{[a-zA-Z0-9_]+}", "", rendered)
    lines = []
    for line in rendered.splitlines():
        stripped = line.strip()
        if not stripped:
            if lines and lines[-1] == "":
                continue
            lines.append("")
            continue
        if stripped in ("-", "•"):
            continue
        if re.match(r"^[-•]\\s*$", stripped):
            continue
        if re.search(r":\\s*$", stripped):
            continue
        lines.append(line.rstrip())
    return "\n".join(lines).strip()


def normalize_delay(value):
    try:
        delay = float(value)
    except (TypeError, ValueError):
        return 0
    if delay < 0:
        return 0
    if delay > 60:
        return 60
    return delay


def dedupe_recipients(recipients):
    deduped = []
    seen = set()
    duplicates = 0
    for rec in recipients:
        email = (rec.get("email") or "").strip().lower()
        if not email:
            continue
        if email in seen:
            duplicates += 1
            continue
        seen.add(email)
        deduped.append(rec)
    return deduped, duplicates


def compute_recipient_stats(recipients):
    companies = set()
    missing_company = 0
    missing_role = 0
    missing_apply = 0
    for rec in recipients:
        company = (rec.get("company") or "").strip()
        if company:
            companies.add(company)
        else:
            missing_company += 1
        if not extract_role_from_post(rec.get("post_text", "")):
            missing_role += 1
        if not (rec.get("apply_links") or "").strip():
            missing_apply += 1
    return {
        "total": len(recipients),
        "companies": len(companies),
        "missing_company": missing_company,
        "missing_role": missing_role,
        "missing_apply": missing_apply,
    }


def send_bulk_gmail_api(
    recipients,
    attachment_path,
    email_cfg,
    resume_profile,
    sender_name,
    sender_contact,
    subject_template=None,
    body_template=None,
    include_links=True,
    include_achievements=True,
    send_delay=0,
    attach_resume=True,
    status_cb=None,
):
    service = get_gmail_service(
        email_cfg["credentials_path"],
        email_cfg["token_path"],
        client_id=email_cfg.get("client_id"),
        client_secret=email_cfg.get("client_secret"),
    )
    total = len(recipients)
    results = []

    for idx, rec in enumerate(recipients, start=1):
        if status_cb:
            status_cb(f"Sending {idx}/{total} to {rec['email']}")
        subj, body_txt = generate_email(
            rec,
            resume_profile,
            sender_name,
            sender_contact,
            subject_template=subject_template,
            body_template=body_template,
            include_links=include_links,
            include_achievements=include_achievements,
        )
        message = EmailMessage()
        message["To"] = rec["email"]
        message["Subject"] = subj
        message.set_content(body_txt)
        tracking_token = None
        tracking_url = ""
        if TRACKING_BASE_URL:
            tracking_token = build_tracking_token()
            tracking_url = build_tracking_pixel_url(tracking_token)
            message.add_alternative(build_email_html(body_txt, tracking_url), subtype="html")
        if attach_resume and attachment_path:
            attach_file(message, attachment_path)

        raw = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")
        try:
            service.users().messages().send(userId="me", body={"raw": raw}).execute()
            if tracking_token:
                log_email_tracking(tracking_token, rec["email"], subj, "bulk_gmail_api")
            results.append(
                {
                    **rec,
                    "status": "sent",
                    "tracking_token": tracking_token or "",
                    "tracking_url": tracking_url or "",
                }
            )
        except Exception as exc:
            results.append(
                {
                    **rec,
                    "status": f"failed: {exc}",
                    "tracking_token": "",
                    "tracking_url": "",
                }
            )
        if send_delay:
            time.sleep(send_delay)
    return results


STOPWORDS = {
    "the","and","for","with","from","that","this","you","your","are","our","was","were","will","have","has","had","into",
    "a","an","to","of","in","on","at","by","as","is","it","be","or","we","they","their","i","me","my","us","he","she",
    "him","her","them","not","but","if","so","than","then","there","here","about","over","under","more","less","most",
    "can","could","should","would","may","might","also","per","etc"
}


def tokenize(text):
    words = re.findall(r"[A-Za-z][A-Za-z0-9+#&._-]{2,}", text.lower())
    return [w for w in words if w not in STOPWORDS]


def extract_keywords(text, limit=10):
    tokens = tokenize(text)
    freq = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1
    ranked = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return [w for w, _ in ranked[:limit]]


def _first_col(cols, candidates):
    for name in candidates:
        if name in cols:
            return name
    return None


def parse_posts_from_dataframe(df):
    if df is None or df.empty:
        return []
    cols = {str(c).strip().lower(): c for c in df.columns}
    content_col = _first_col(cols, ["content", "post", "text", "body", "caption"])
    title_col = _first_col(cols, ["title", "headline", "subject"])
    likes_col = _first_col(cols, ["likes", "reactions", "like", "reaction"])
    comments_col = _first_col(cols, ["comments", "comment"])
    shares_col = _first_col(cols, ["shares", "reposts", "repost"])
    impressions_col = _first_col(cols, ["impressions", "views", "reach"])
    date_col = _first_col(cols, ["date", "posted", "timestamp", "created", "created_at"])

    posts = []
    for _, row in df.iterrows():
        content = ""
        if content_col:
            content = str(row.get(cols[content_col], "") or "")
        if not content and title_col:
            content = str(row.get(cols[title_col], "") or "")
        likes = row.get(cols[likes_col], 0) if likes_col else 0
        comments = row.get(cols[comments_col], 0) if comments_col else 0
        shares = row.get(cols[shares_col], 0) if shares_col else 0
        impressions = row.get(cols[impressions_col], 0) if impressions_col else 0
        date = str(row.get(cols[date_col], "") or "") if date_col else ""

        likes = int(pd.to_numeric(likes, errors="coerce") or 0)
        comments = int(pd.to_numeric(comments, errors="coerce") or 0)
        shares = int(pd.to_numeric(shares, errors="coerce") or 0)
        impressions = int(pd.to_numeric(impressions, errors="coerce") or 0)

        posts.append(
            {
                "date": date,
                "content": content.strip(),
                "likes": likes,
                "comments": comments,
                "shares": shares,
                "impressions": impressions,
            }
        )
    return posts


def analyze_posts(posts):
    if not posts:
        return {}
    for post in posts:
        likes = int(pd.to_numeric(post.get("likes", 0), errors="coerce") or 0)
        comments = int(pd.to_numeric(post.get("comments", 0), errors="coerce") or 0)
        shares = int(pd.to_numeric(post.get("shares", 0), errors="coerce") or 0)
        impressions = int(pd.to_numeric(post.get("impressions", 0), errors="coerce") or 0)
        post["likes"] = likes
        post["comments"] = comments
        post["shares"] = shares
        post["impressions"] = impressions
        engagement = likes + comments + shares
        if impressions > 0:
            rate = engagement / impressions
        else:
            rate = engagement
        post["engagement"] = engagement
        post["engagement_rate"] = rate
        post["length"] = len(post.get("content", ""))
        post["has_question"] = "?" in post.get("content", "")

    total_posts = len(posts)
    total_engagement = sum(p.get("engagement", 0) for p in posts)
    avg_engagement = round(total_engagement / total_posts, 2) if total_posts else 0
    has_impressions = any(p.get("impressions", 0) > 0 for p in posts)

    top_posts = sorted(posts, key=lambda x: x.get("engagement_rate", 0), reverse=True)[:3]
    bottom_posts = sorted(posts, key=lambda x: x.get("engagement_rate", 0))[:3]

    top_text = " ".join(p.get("content", "") for p in top_posts)
    bottom_text = " ".join(p.get("content", "") for p in bottom_posts)
    top_keywords = extract_keywords(top_text, limit=6)
    bottom_keywords = extract_keywords(bottom_text, limit=6)

    top_len = sum(p.get("length", 0) for p in top_posts) / max(len(top_posts), 1)
    bottom_len = sum(p.get("length", 0) for p in bottom_posts) / max(len(bottom_posts), 1)
    top_questions = sum(1 for p in top_posts if p.get("has_question")) / max(len(top_posts), 1)
    bottom_questions = sum(1 for p in bottom_posts if p.get("has_question")) / max(len(bottom_posts), 1)

    what_worked = []
    if top_keywords:
        what_worked.append(f"High-performing topics: {', '.join(top_keywords[:5])}.")
    if top_len + 20 < bottom_len:
        what_worked.append("Shorter posts performed better.")
    if top_questions > bottom_questions:
        what_worked.append("Questions in the hook improved engagement.")

    what_didnt = []
    if bottom_keywords:
        what_didnt.append(f"Low-performing topics: {', '.join(bottom_keywords[:5])}.")
    if bottom_len + 20 < top_len:
        what_didnt.append("Longer posts underperformed.")
    if bottom_questions > top_questions:
        what_didnt.append("Question-heavy posts underperformed.")

    if not has_impressions:
        what_worked.append("Engagement rate uses raw reactions because impressions are missing.")
        what_didnt.append("Add impressions/views for more accurate benchmarking.")

    return {
        "total_posts": total_posts,
        "avg_engagement": avg_engagement,
        "has_impressions": has_impressions,
        "top_posts": top_posts,
        "bottom_posts": bottom_posts,
        "what_worked": what_worked,
        "what_didnt": what_didnt,
        "top_keywords": top_keywords,
        "bottom_keywords": bottom_keywords,
    }


def extract_achievements(text, limit=3):
    lines = [l.strip() for l in re.split(r"[\\n\\.]+", text) if l.strip()]
    hits = []
    for l in lines:
        if re.search(r"\\d|%|\\b(increased|improved|reduced|led|built|launched|saved|grew|achieved|delivered)\\b", l, re.I):
            hits.append(l)
    return hits[:limit]


def extract_resume_text(path: Path):
    ext = path.suffix.lower()
    if ext == ".pdf":
        reader = PdfReader(str(path))
        return "\\n".join(page.extract_text() or "" for page in reader.pages)
    if ext in [".docx", ".doc"]:
        doc = docx_lib.Document(str(path))
        return "\\n".join(p.text for p in doc.paragraphs)
    if ext in [".txt"]:
        return path.read_text(encoding="utf-8", errors="ignore")
    return ""


SECTION_HEADERS = {
    "summary": ["summary", "professional summary", "profile", "objective"],
    "experience": ["experience", "work experience", "employment", "professional experience"],
    "skills": ["skills", "technical skills", "core skills"],
    "education": ["education", "academic", "academics"],
}

RESUME_SECTION_LABELS = {
    "contact": "Header & Contact",
    "summary": "Summary",
    "experience": "Experience",
    "projects": "Projects",
    "leadership": "Leadership",
    "skills": "Skills",
    "education": "Education",
    "achievements": "Achievements",
    "other": "Other",
}

RESUME_SECTION_ALIASES = {
    "summary": "summary",
    "professional summary": "summary",
    "profile": "summary",
    "objective": "summary",
    "experience": "experience",
    "work experience": "experience",
    "employment": "experience",
    "professional experience": "experience",
    "skills": "skills",
    "technical skills": "skills",
    "core skills": "skills",
    "education": "education",
    "academic": "education",
    "academics": "education",
    "projects": "projects",
    "project": "projects",
    "key projects": "projects",
    "leadership": "leadership",
    "leadership experience": "leadership",
    "positions of responsibility": "leadership",
    "achievements": "achievements",
    "awards": "achievements",
    "certifications": "skills",
}

RESUME_SECTION_ORDER = [
    "contact",
    "summary",
    "experience",
    "projects",
    "leadership",
    "skills",
    "education",
    "achievements",
    "other",
]

ROLE_FAMILY_PROFILES = {
    "Product Management": {
        "keywords": [
            "product manager", "product management", "roadmap", "roadmaps", "go to market",
            "gtm", "backlog", "stakeholder", "user research", "product launch", "retention",
            "experimentation", "a/b testing", "growth", "kpi", "okr", "scrum", "agile",
        ],
        "recommended_skills": [
            "Roadmapping", "Stakeholder Management", "SQL", "A/B Testing",
            "User Research", "Product Analytics", "PRDs", "Agile Delivery",
        ],
        "role_hints": ["Product Manager", "Associate Product Manager", "Program Manager"],
        "learning_recommendations": [
            "Build case studies that show roadmap tradeoffs, launch decisions, and KPI movement.",
            "Add one quantified product analytics example using SQL, dashboards, or experiment results.",
            "Tighten bullets around user problem, decision, action, and impact.",
        ],
    },
    "Software Engineering": {
        "keywords": [
            "software engineer", "developer", "backend", "frontend", "full stack", "fullstack",
            "api", "microservices", "python", "java", "javascript", "react", "node", "django",
            "spring", "rest", "system design", "aws", "azure", "gcp", "docker", "kubernetes",
        ],
        "recommended_skills": [
            "Data Structures", "System Design", "REST APIs", "Cloud",
            "Testing", "CI/CD", "SQL", "Observability",
        ],
        "role_hints": ["Software Engineer", "Backend Engineer", "Full Stack Engineer"],
        "learning_recommendations": [
            "Add project bullets that show architecture, scale, reliability, and measurable outcomes.",
            "Include testing, deployment, and monitoring work, not just feature delivery.",
            "Show one backend and one frontend or data example to improve role coverage.",
        ],
    },
    "Data / Analytics": {
        "keywords": [
            "data analyst", "business analyst", "analytics", "sql", "tableau", "power bi",
            "python", "statistics", "forecasting", "dashboard", "etl", "data pipeline",
            "cohort", "segmentation", "experimentation", "regression", "machine learning",
        ],
        "recommended_skills": [
            "SQL", "Python", "Dashboarding", "Statistics",
            "Experiment Design", "Data Modeling", "Storytelling", "ETL",
        ],
        "role_hints": ["Data Analyst", "Business Analyst", "Analytics Associate"],
        "learning_recommendations": [
            "Add one project showing data cleaning, analysis, recommendation, and business outcome.",
            "Quantify dashboard adoption, reporting accuracy, or time saved through automation.",
            "Show stronger evidence of SQL depth, experimentation, or statistical reasoning.",
        ],
    },
    "Marketing / Growth": {
        "keywords": [
            "marketing", "growth", "campaign", "performance marketing", "seo", "sem", "content",
            "brand", "acquisition", "crm", "email marketing", "funnel", "conversion", "retention",
            "paid media", "social media", "google analytics", "meta ads",
        ],
        "recommended_skills": [
            "Campaign Analytics", "Funnel Optimization", "SEO/SEM", "CRM",
            "Lifecycle Marketing", "Copywriting", "Experimentation", "Attribution",
        ],
        "role_hints": ["Growth Associate", "Marketing Analyst", "Performance Marketer"],
        "learning_recommendations": [
            "Rewrite bullets to show channel, campaign goal, budget or volume, and conversion impact.",
            "Add funnel metrics and retention or revenue outcomes instead of task-only wording.",
            "Show at least one lifecycle, SEO/SEM, or paid acquisition example.",
        ],
    },
    "Operations / Program Management": {
        "keywords": [
            "operations", "program manager", "program management", "process improvement",
            "cross functional", "vendor management", "sop", "sla", "planning", "execution",
            "supply chain", "logistics", "risk", "governance", "automation",
        ],
        "recommended_skills": [
            "Process Design", "Stakeholder Management", "Program Tracking", "Automation",
            "SOPs", "Risk Management", "Data Analysis", "Vendor Coordination",
        ],
        "role_hints": ["Program Manager", "Operations Analyst", "Business Operations Associate"],
        "learning_recommendations": [
            "Add examples showing operating cadence, process changes, and measurable efficiency gains.",
            "Highlight cross-functional coordination, SLA ownership, and execution rigor.",
            "Use stronger metrics such as turnaround time, throughput, defect rate, or cost saved.",
        ],
    },
    "Design / UX": {
        "keywords": [
            "designer", "ux", "ui", "figma", "wireframe", "prototype", "design system",
            "usability", "interaction design", "visual design", "user journey", "research",
        ],
        "recommended_skills": [
            "Figma", "Wireframing", "Prototyping", "User Research",
            "Usability Testing", "Design Systems", "Information Architecture", "Interaction Design",
        ],
        "role_hints": ["UX Designer", "Product Designer", "UI/UX Designer"],
        "learning_recommendations": [
            "Show end-to-end case studies with problem framing, design iterations, and impact.",
            "Add usability or research insights, not just design tools used.",
            "Tie design decisions to conversion, adoption, or task success metrics where possible.",
        ],
    },
}

ROLE_FAMILY_COURSES = {
    "Data / Analytics": [
        {"title": "Machine Learning Crash Course by Google", "url": "https://developers.google.com/machine-learning/crash-course"},
        {"title": "Machine Learning by Andrew Ng", "url": "https://www.coursera.org/learn/machine-learning"},
        {"title": "Data Science Foundations by LinkedIn", "url": "https://www.linkedin.com/learning/data-science-foundations-fundamentals-5"},
        {"title": "Data Scientist with Python", "url": "https://www.datacamp.com/tracks/data-scientist-with-python"},
        {"title": "Programming for Data Science with Python", "url": "https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104"},
        {"title": "Intro to ML with TensorFlow", "url": "https://www.udacity.com/course/intro-to-machine-learning-with-tensorflow-nanodegree--nd230"},
    ],
    "Software Engineering": [
        {"title": "Node.js and Express.js Crash Course", "url": "https://youtu.be/Oe421EPjeBE"},
        {"title": "React Crash Course", "url": "https://youtu.be/Dorf8i6lCuk"},
        {"title": "Django Crash Course", "url": "https://youtu.be/e1IyzVyrLSU"},
        {"title": "Full Stack Web Developer Nanodegree", "url": "https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044"},
        {"title": "Front End Web Developer Nanodegree", "url": "https://www.udacity.com/course/front-end-web-developer-nanodegree--nd0011"},
        {"title": "Flask Web Applications", "url": "https://www.educative.io/courses/flask-develop-web-applications-in-python"},
    ],
    "Design / UX": [
        {"title": "Google UX Design Professional Certificate", "url": "https://www.coursera.org/professional-certificates/google-ux-design"},
        {"title": "UI / UX Design Specialization", "url": "https://www.coursera.org/specializations/ui-ux-design"},
        {"title": "UX Designer Nanodegree", "url": "https://www.udacity.com/course/ux-designer-nanodegree--nd578"},
        {"title": "Adobe XD Tutorial", "url": "https://youtu.be/68w2VwalD5w"},
        {"title": "Adobe XD for Beginners", "url": "https://youtu.be/WEljsc2jorI"},
        {"title": "Design Rules: Great UI Design", "url": "https://www.udemy.com/course/design-rules/"},
    ],
    "Product Management": [
        {"title": "Google Project Management Certificate", "url": "https://www.coursera.org/professional-certificates/google-project-management"},
        {"title": "Product Strategy by Kellogg", "url": "https://www.coursera.org/learn/product-strategy"},
        {"title": "SQL for Data Analysis", "url": "https://mode.com/sql-tutorial/"},
        {"title": "A/B Testing Foundations", "url": "https://www.udacity.com/course/ab-testing--ud257"},
        {"title": "Design Thinking for Innovation", "url": "https://www.coursera.org/learn/uva-darden-design-thinking-innovation"},
        {"title": "Product Analytics Micro-Course", "url": "https://www.productschool.com/product-management-courses/"},
    ],
    "Marketing / Growth": [
        {"title": "Google Digital Marketing and E-commerce", "url": "https://www.coursera.org/professional-certificates/google-digital-marketing-ecommerce"},
        {"title": "Content Marketing Certification", "url": "https://academy.hubspot.com/courses/content-marketing"},
        {"title": "SEO Fundamentals", "url": "https://learningseo.io/"},
        {"title": "Google Analytics Certification", "url": "https://skillshop.withgoogle.com/"},
        {"title": "Meta Social Media Marketing", "url": "https://www.coursera.org/professional-certificates/meta-social-media-marketing"},
        {"title": "Performance Marketing Basics", "url": "https://www.udemy.com/course/learn-digital-marketing-course/"},
    ],
    "Operations / Program Management": [
        {"title": "Google Project Management Certificate", "url": "https://www.coursera.org/professional-certificates/google-project-management"},
        {"title": "Agile with Atlassian Jira", "url": "https://www.coursera.org/learn/agile-atlassian-jira"},
        {"title": "Operations Analytics", "url": "https://www.coursera.org/learn/wharton-operations-analytics"},
        {"title": "Process Mining and Optimization", "url": "https://www.coursera.org/learn/process-mining"},
        {"title": "Excel to MySQL: Analytics", "url": "https://www.coursera.org/specializations/excel-mysql"},
        {"title": "Business Process Improvement", "url": "https://www.udemy.com/course/business-process-improvement/"},
    ],
}

RESUME_RESOURCE_VIDEOS = [
    "https://youtu.be/Tt08KmFfIYQ",
    "https://youtu.be/y8YH0Qbu5h4",
    "https://youtu.be/u75hUSShvnc",
    "https://youtu.be/BYUy1yvjHxE",
    "https://youtu.be/KFaugkGVeNQ",
    "https://youtu.be/3agP4x8LYFM",
]

INTERVIEW_RESOURCE_VIDEOS = [
    "https://youtu.be/HG68Ymazo18",
    "https://youtu.be/BOvAAoxM4vg",
    "https://youtu.be/KukmClH1KoA",
    "https://youtu.be/7_aAicmPB3A",
    "https://youtu.be/1mHjMNZZvFo",
    "https://youtu.be/WfdtKbAJOmE",
]


def split_sections(text):
    sections = {k: [] for k in SECTION_HEADERS.keys()}
    current = None
    for line in text.splitlines():
        raw = line.strip()
        if not raw:
            continue
        lowered = raw.lower().strip(":")
        matched = None
        for key, headers in SECTION_HEADERS.items():
            if any(lowered == h or lowered.startswith(h + " ") for h in headers):
                matched = key
                break
        if matched:
            current = matched
            continue
        if current:
            sections[current].append(raw)
    return {k: "\n".join(v) for k, v in sections.items()}


def normalize_resume_section_name(value):
    cleaned = re.sub(r"[^a-z]+", " ", (value or "").lower()).strip()
    return RESUME_SECTION_ALIASES.get(cleaned)


def is_resume_heading_line(text):
    raw = (text or "").strip()
    if not raw:
        return False
    if normalize_resume_section_name(raw):
        return True
    alpha = re.sub(r"[^A-Za-z ]+", "", raw).strip()
    if not alpha:
        return False
    words = [w for w in alpha.split() if w]
    return len(words) <= 4 and alpha.upper() == alpha


def is_resume_contact_line(text):
    raw = (text or "").strip()
    if not raw:
        return False
    if extract_emails(raw):
        return True
    if re.search(r"(linkedin\.com|portfolio|github\.com)", raw, re.I):
        return True
    if "|" in raw and re.search(r"\b\+?\d[\d\s\-()]{7,}\b", raw):
        return True
    alpha = re.sub(r"[^A-Za-z ]+", "", raw).strip()
    words = [w for w in alpha.split() if w]
    return len(words) <= 4 and alpha.upper() == alpha and not normalize_resume_section_name(raw)


def infer_resume_section_from_line(text, current="contact"):
    raw = (text or "").strip()
    if not raw:
        return current or "other"
    normalized = normalize_resume_section_name(raw)
    if normalized:
        return normalized
    if current and current not in {"contact", "other"}:
        return current
    if is_resume_contact_line(raw):
        return "contact"
    lowered = raw.lower()
    if re.search(r"\b(university|college|institute|school|bachelor|master|mba|bms|graduation)\b", lowered):
        return "education"
    if re.search(r"\b(project|case competition|chatbot|prototype|figma)\b", lowered):
        return "projects"
    if re.search(r"\b(head|president|lead|club|committee|captain)\b", lowered):
        return "leadership"
    if re.search(r"\b(winner|award|finals|recognized|top voice|runner up)\b", lowered):
        return "achievements"
    if re.search(r"\b(product|research|go to market|agile|scrum|jira|design|figma|sql|python|marketing)\b", lowered):
        return current if current in {"summary", "experience", "projects", "leadership"} else "skills"
    return current or "other"


def build_resume_section_report(review):
    grouped = {
        key: {
            "key": key,
            "label": RESUME_SECTION_LABELS.get(key, key.title()),
            "raw_text": "",
            "recommendations": [],
            "line_reviews": [],
            "improved_bullets": [],
        }
        for key in RESUME_SECTION_ORDER
    }

    for key, text in (review.get("sections") or {}).items():
        normalized = normalize_resume_section_name(key) or key
        if normalized in grouped and isinstance(text, str) and text.strip():
            grouped[normalized]["raw_text"] = text.strip()

    for key, recs in (review.get("recommendations") or {}).items():
        normalized = normalize_resume_section_name(key) or key
        if normalized in grouped and isinstance(recs, list):
            grouped[normalized]["recommendations"] = [r for r in recs if str(r).strip()]

    current = "contact"
    for item in review.get("line_reviews") or []:
        line = (item.get("line") or "").strip()
        if not line:
            continue
        next_section = infer_resume_section_from_line(line, current=current)
        if is_resume_heading_line(line):
            current = next_section
            continue
        current = next_section
        if current == "contact" and is_resume_contact_line(line):
            continue
        if item.get("status") == "neutral":
            continue
        grouped[current]["line_reviews"].append(item)

    current = "contact"
    for item in review.get("improved_bullets") or []:
        original = (item.get("original") or "").strip()
        if not original:
            continue
        next_section = infer_resume_section_from_line(original, current=current)
        if is_resume_heading_line(original):
            current = next_section
            continue
        current = next_section
        if current == "contact" and is_resume_contact_line(original):
            continue
        grouped[current]["improved_bullets"].append(item)

    output = []
    for key in RESUME_SECTION_ORDER:
        section = grouped[key]
        if section["raw_text"] or section["recommendations"] or section["line_reviews"] or section["improved_bullets"]:
            output.append(section)
    return output


LINKEDIN_SECTION_HEADERS = {
    "about": ["about", "summary", "professional summary", "profile"],
    "experience": ["experience", "work experience", "employment", "professional experience"],
    "skills": ["skills", "top skills", "core skills"],
    "education": ["education", "academics", "academic"],
    "certifications": ["certifications", "certification", "licenses", "licenses & certifications"],
    "projects": ["projects", "project"],
    "recommendations": ["recommendations", "recommendation"],
}


def split_linkedin_sections(text):
    sections = {k: [] for k in LINKEDIN_SECTION_HEADERS.keys()}
    current = None
    for line in text.splitlines():
        raw = line.strip()
        if not raw:
            continue
        lowered = raw.lower().strip(":")
        matched = None
        for key, headers in LINKEDIN_SECTION_HEADERS.items():
            if any(lowered == h or lowered.startswith(h + " ") for h in headers):
                matched = key
                break
        if matched:
            current = matched
            continue
        if current:
            sections[current].append(raw)
    return {k: "\n".join(v) for k, v in sections.items()}


def analyze_linkedin_profile(text):
    cleaned = (text or '').strip()
    lines = [l.strip() for l in cleaned.splitlines() if l.strip()]
    sections = split_linkedin_sections(cleaned)
    issues = []
    recs = {k: [] for k in LINKEDIN_SECTION_HEADERS.keys()}

    headline = lines[0] if lines else ''
    headline_len = len(headline)
    headline_score = 35
    if 40 <= headline_len <= 120:
        headline_score = 85
    elif 25 <= headline_len < 40:
        headline_score = 70
    elif headline_len > 120:
        headline_score = 65
    if headline_len < 25:
        issues.append('Headline is too short. Add role, specialty, and impact.')
        recs['about'].append('Mirror your target role in the headline.')
    if headline_len > 140:
        issues.append('Headline is too long. Keep it under 120 characters.')

    about_text = sections.get('about', '').strip()
    about_len = len(about_text)
    about_score = 35
    if about_len >= 300:
        about_score = 90
    elif about_len >= 150:
        about_score = 75
    elif about_len > 0:
        about_score = 55
    if about_len < 120:
        issues.append('About section is missing or too short. Add 3-5 concise lines.')
        recs['about'].append('Cover your role, impact, and focus areas in 3-5 lines.')

    exp_text = sections.get('experience', '').strip()
    exp_lines = [l for l in exp_text.splitlines() if l.strip()]
    has_metrics = any(re.search(r"\d|%", l) for l in exp_lines)
    exp_score = 40
    if exp_lines and has_metrics and len(exp_lines) >= 3:
        exp_score = 90
    elif exp_lines:
        exp_score = 70
    if not exp_lines:
        issues.append('Experience section is missing or thin. Add role details with metrics.')
        recs['experience'].append('Use bullet points with scope and quantified results.')

    skills_text = sections.get('skills', '')
    skills_text = skills_text.replace('\u2022', ',').replace('\u2023', ',')
    raw_skills = [s.strip() for s in re.split(r"[,\n;/|]+", skills_text) if s.strip()]
    skills_list = []
    seen_skills = set()
    for skill in raw_skills:
        key = skill.lower()
        if key not in seen_skills:
            seen_skills.add(key)
            skills_list.append(skill)
    skills_count = len(skills_list)
    skills_score = 40
    if skills_count >= 12:
        skills_score = 90
    elif skills_count >= 8:
        skills_score = 75
    elif skills_count >= 4:
        skills_score = 60
    if skills_count < 8:
        issues.append('Skills section is light. Add 10-15 role specific skills.')
        recs['skills'].append('Include tools, platforms, and domain keywords.')

    edu_text = sections.get('education', '')
    edu_score = 55
    if re.search(r"\b(bachelor|master|b\.?tech|b\.?e|mba|bsc|msc|phd)\b", edu_text, re.I):
        edu_score = 85
    else:
        issues.append('Education section is missing degree or institution details.')
        recs['education'].append('Add degree, institution, and graduation year.')

    cert_text = sections.get('certifications', '').strip()
    cert_score = 70 if cert_text else 50
    if not cert_text:
        recs['certifications'].append('Add certifications that support your target role.')

    projects_text = sections.get('projects', '').strip()
    proj_score = 70 if projects_text else 50
    if not projects_text:
        recs['projects'].append('Add 1-3 projects or case studies with impact.')

    rec_text = sections.get('recommendations', '').strip()
    rec_score = 65 if rec_text else 50
    if not rec_text:
        recs['recommendations'].append('Request 1-2 recommendations to add credibility.')

    word_count = len(re.findall(r"\b\w+\b", cleaned))
    formatting_score = 85
    if word_count < 200:
        formatting_score = 55
        issues.append('Profile text is short. Expand About and Experience sections.')
    if word_count > 2000:
        formatting_score = 60
        issues.append('Profile text is long. Tighten and remove repetition.')

    breakdown = {
        'Headline': headline_score,
        'About': about_score,
        'Experience': exp_score,
        'Skills': skills_score,
        'Education': edu_score,
        'Certifications': cert_score,
        'Projects': proj_score,
        'Recommendations': rec_score,
        'Formatting': formatting_score,
    }
    radar_labels = list(breakdown.keys())
    radar_values = [breakdown.get(k, 0) for k in radar_labels]
    overall = int(sum(breakdown.values()) / len(breakdown))

    keyword_top = extract_keywords(cleaned, limit=12)
    exp_bullets = len([l for l in exp_lines if re.match(r"^[-*]", l.strip())])
    has_numbers = bool(re.search(r"\d", exp_text))

    strengths = [k for k, v in breakdown.items() if v >= 85]
    focus_areas = []
    key_map = {
        'Headline': 'headline',
        'About': 'about',
        'Experience': 'experience',
        'Skills': 'skills',
        'Education': 'education',
        'Certifications': 'certifications',
        'Projects': 'projects',
        'Recommendations': 'recommendations',
        'Formatting': 'formatting',
    }
    for category, score in sorted(breakdown.items(), key=lambda x: x[1]):
        if score >= 85:
            continue
        priority = 'High' if score < 60 else 'Medium' if score < 80 else 'Low'
        rec_key = key_map.get(category, '')
        actions = recs.get(rec_key, []) if rec_key in recs else []
        note = ''
        for issue in issues:
            if category.lower() in issue.lower():
                note = issue
                break
        if not note and actions:
            note = actions[0]
        focus_areas.append(
            {
                'category': category,
                'score': score,
                'priority': priority,
                'note': note,
                'actions': actions[:3],
            }
        )

    return {
        'overall_score': overall,
        'breakdown': breakdown,
        'issues': issues,
        'quick_wins': issues[:4],
        'recommendations': recs,
        'sections': sections,
        'headline': headline,
        'keyword_top': keyword_top,
        'skills_list': skills_list,
        'focus_areas': focus_areas,
        'strengths': strengths,
        'stats': {
            'word_count': word_count,
            'skills_count': skills_count,
            'experience_bullets': exp_bullets,
            'has_numbers': has_numbers,
            'sections_present': sum(1 for v in sections.values() if v.strip()),
        },
        'radar_labels': radar_labels,
        'radar_values': radar_values,
    }


def parse_gemini_payload(raw_text):
    if not raw_text:
        return {}
    text = raw_text.strip()
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", text, re.I)
    if fence:
        text = fence.group(1).strip()
    # Try strict JSON
    try:
        data = json.loads(text)
        if isinstance(data, dict):
            return data
    except Exception:
        pass
    # Try to extract JSON block
    try:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            data = json.loads(text[start : end + 1])
            if isinstance(data, dict):
                return data
    except Exception:
        pass
    return {}


def parse_gemini_json(raw_text):
    if not raw_text:
        return None
    text = raw_text.strip()
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", text, re.I)
    if fence:
        text = fence.group(1).strip()
    try:
        data = json.loads(text)
        if isinstance(data, (dict, list)):
            return data
    except Exception:
        pass
    try:
        obj_start = text.find("{")
        obj_end = text.rfind("}")
        if obj_start != -1 and obj_end != -1 and obj_end > obj_start:
            data = json.loads(text[obj_start : obj_end + 1])
            if isinstance(data, (dict, list)):
                return data
    except Exception:
        pass
    try:
        arr_start = text.find("[")
        arr_end = text.rfind("]")
        if arr_start != -1 and arr_end != -1 and arr_end > arr_start:
            data = json.loads(text[arr_start : arr_end + 1])
            if isinstance(data, (dict, list)):
                return data
    except Exception:
        pass
    return None


def extract_first_metric(text):
    if not text:
        return None, True
    match = re.search(r"(\\$?\\d+(?:\\.\\d+)?\\s?(?:k|m|b)?|\\d+(?:\\.\\d+)?%|\\d+\\s?(?:users|customers|leads|signups|installs|days|weeks|months|years))", text, re.I)
    if match:
        return match.group(1).strip(), False
    return "15% growth", True


def infer_role_label(text):
    lowered = (text or "").lower()
    if "product marketing" in lowered or "pmm" in lowered:
        return "Product Marketing"
    if "growth" in lowered:
        return "Growth"
    if "strategy" in lowered:
        return "Strategy"
    if "marketing" in lowered:
        return "Marketing"
    return "Product"


def build_fallback_ai(text, analysis):
    keyword_top = analysis.get("keyword_top", []) or []
    skills_list = analysis.get("skills_list", []) or []
    sections = analysis.get("sections", {}) or {}
    headline = analysis.get("headline", "") or ""
    issues = analysis.get("issues", []) or []
    strengths = analysis.get("strengths", []) or []
    focus_areas = analysis.get("focus_areas", []) or []
    role_label = infer_role_label(text)
    metric, inferred = extract_first_metric(text)
    metric_text = metric + (" [inferred]" if inferred else "")

    top_kw = keyword_top[:3]
    keyword_block = " | ".join(top_kw) if top_kw else "GTM | Growth"
    suggested_headline = f"{role_label} | {keyword_block} | {metric_text}"

    about_original = sections.get("about", "")
    about_suggested = (
        f"{role_label} leader focused on {', '.join(top_kw) if top_kw else 'GTM and growth'}. "
        f"Delivered {metric_text} by partnering cross-functionally across product, marketing, and sales."
    )

    exp_lines = [l.strip() for l in sections.get("experience", "").splitlines() if l.strip()]
    exp_bullets = []
    for line in exp_lines[:3]:
        exp_bullets.append({
            "original": line,
            "suggested": f"{line} resulting in {metric_text}.",
            "reason": "Add quantified impact and outcome.",
        })
    if not exp_bullets:
        exp_bullets = [{
            "original": "Owned GTM execution",
            "suggested": f"Owned GTM execution delivering {metric_text}.",
            "reason": "Add scope and measurable impact.",
        }]

    missing_keywords = [
        "Market Intelligence",
        "Competitive Analysis",
        "Customer Acquisition Cost",
    ]

    comparison_current = [f"{kw.title()} exposure" for kw in top_kw] if top_kw else ["Current role keywords missing"]
    comparison_target = missing_keywords[:3]

    return {
        "summary": f"Strengths in {', '.join(strengths) if strengths else 'core sections'}. Focus on closing gaps around metrics and role keywords.",
        "positioning": {
            "current": headline or (top_kw[0] if top_kw else "Current positioning"),
            "target": role_label,
            "seniority": "",
            "industry": "",
            "differentiators": strengths or top_kw,
            "proof_gaps": issues[:3],
        },
        "headline": {
            "original": headline,
            "suggested": suggested_headline,
            "variants": [suggested_headline],
        },
        "about": {
            "original": about_original,
            "suggested": about_suggested,
            "structure": ["Role", "Impact", "Collaboration"],
        },
        "experience_bullets": exp_bullets,
        "comparison": {
            "current": comparison_current,
            "target": comparison_target,
            "gap": issues[:3],
        },
        "keyword_analysis": {
            "top_keywords": keyword_top[:10],
            "missing_keywords": missing_keywords,
            "role_keywords": keyword_top[:6],
        },
        "focus_areas": focus_areas,
        "action_plan": [
            {
                "timeframe": "Week 1",
                "goal": "Optimize Core Identity",
                "actions": [
                    "Update headline with role + impact.",
                    "Refresh About section with metrics.",
                ],
                "deliverable": "SEO-optimized Profile Header",
            },
            {
                "timeframe": "Week 2",
                "goal": "Quantify Impact",
                "actions": [
                    "Add 2-3 metrics to experience bullets.",
                    "Add missing role keywords.",
                ],
                "deliverable": "Metric-rich Experience Section",
            },
        ],
        "suggestions": issues[:6],
    }


def sanitize_ai_payload(data):
    if isinstance(data, dict):
        return {k: sanitize_ai_payload(v) for k, v in data.items()}
    if isinstance(data, list):
        return [sanitize_ai_payload(v) for v in data]
    if isinstance(data, str):
        return clean_bullet_text(data)
    return data


def format_gemini_error_message(
    raw_error,
    default_message="Gemini analysis was unavailable.",
    fallback_label="Rule-based fallback was used.",
):
    text = (raw_error or "").strip()
    if not text:
        return default_message
    try:
        payload = json.loads(text)
        error = payload.get("error") if isinstance(payload, dict) else None
        if isinstance(error, dict):
            status = str(error.get("status", "")).strip()
            message = str(error.get("message", "")).strip()
            retry_delay = ""
            details = error.get("details") or []
            if isinstance(details, list):
                for item in details:
                    if isinstance(item, dict) and item.get("@type", "").endswith("RetryInfo"):
                        retry_delay = str(item.get("retryDelay", "")).strip()
                        break
            if status == "RESOURCE_EXHAUSTED":
                if retry_delay:
                    return f"Gemini quota reached. Retry after {retry_delay} or use a different API key / paid plan. {fallback_label}"
                return f"Gemini quota reached. Wait for quota reset or use a different API key / paid plan. {fallback_label}"
            if status == "NOT_FOUND":
                return "Configured Gemini model is not available for this API key. Update GEMINI_MODEL or GEMINI_RESUME_MODEL."
            if message:
                first_line = message.splitlines()[0].strip()
                return first_line
    except Exception:
        pass
    if len(text) > 220:
        return text[:217] + "..."
    return text


def gemini_generate_content(prompt, temperature=0.3, max_output_tokens=1200, extra_generation_config=None, model_override=None):
    global LAST_GEMINI_ERROR
    api_key = os.getenv('GEMINI_API_KEY', '').strip()
    if not api_key:
        LAST_GEMINI_ERROR = "Missing GEMINI_API_KEY."
        return ''
    model = (model_override or os.getenv('GEMINI_MODEL', 'gemini-1.5-flash')).strip()
    if model.startswith('models/'):
        model = model.split('/', 1)[1]
    url = (
        'https://generativelanguage.googleapis.com/v1beta/models/'
        f"{model}:generateContent?key={api_key}"
    )
    generation_config = {
        'temperature': temperature,
        'maxOutputTokens': max_output_tokens,
        'topP': 0.9,
    }
    if isinstance(extra_generation_config, dict):
        generation_config.update(extra_generation_config)
    payload = {
        'contents': [
            {
                'role': 'user',
                'parts': [{'text': prompt}],
            }
        ],
        'generationConfig': generation_config,
    }
    try:
        import urllib.request

        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json'},
        )
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        LAST_GEMINI_ERROR = ""
        candidates = data.get('candidates') or []
        if not candidates:
            LAST_GEMINI_ERROR = "Gemini returned no candidates."
            return ''
        content = candidates[0].get('content') or {}
        parts = content.get('parts') or []
        if parts:
            texts = []
            for part in parts:
                if isinstance(part, dict) and part.get('text') is not None:
                    texts.append(str(part.get('text', '')))
            return ''.join(texts).strip()
        LAST_GEMINI_ERROR = "Gemini returned empty content parts."
        return ''
    except Exception as exc:
        try:
            body = exc.read().decode('utf-8', errors='ignore') if hasattr(exc, 'read') else ''
        except Exception:
            body = ''
        LAST_GEMINI_ERROR = body or str(exc)
        return ''


def is_ollama_configured():
    return bool(os.getenv("OLLAMA_MODEL", "").strip())


def get_resume_ai_provider_label():
    has_gemini = bool(os.getenv("GEMINI_API_KEY", "").strip())
    has_ollama = is_ollama_configured()
    if has_gemini and has_ollama:
        return "Gemini + Ollama"
    if has_gemini:
        return "Gemini"
    if has_ollama:
        return "Ollama"
    return ""


def ollama_generate_content(prompt, temperature=0.2, max_output_tokens=1100, model_override=None):
    model = (model_override or os.getenv("OLLAMA_MODEL", "")).strip()
    if not model:
        return ""
    base_url = os.getenv("OLLAMA_BASE_URL", "").strip().rstrip("/")
    if not base_url:
        return ""
    url = f"{base_url}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature,
            "num_predict": max_output_tokens,
        },
    }
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        if isinstance(data, dict):
            return clean_bullet_text(str(data.get("response", ""))).strip()
    except Exception:
        return ""
    return ""


def gemini_linkedin_analysis(text):
    api_key = os.getenv('GEMINI_API_KEY', '').strip()
    if not api_key:
        return {}
    snippet = (text or '')[:9000]
    schema = (
        '{'
        '"summary": string, '
        '"headline": {"original": string, "suggested": string, "variants": [string]}, '
        '"about": {"original": string, "suggested": string}, '
        '"experience_bullets": [{"original": string, "suggested": string, "reason": string}], '
        '"keyword_analysis": {"top_keywords": [string], "missing_keywords": [string], "role_keywords": [string]}, '
        '"focus_areas": [{"section": string, "priority": "High"|"Medium"|"Low", "reason": string, "actions": [string]}], '
        '"action_plan": [{"timeframe": string, "goal": string, "actions": [string], "deliverable": string}], '
        '"suggestions": [string]'
        '}'
    )
    prompt = (
        'You are a LinkedIn profile strategist. Return ONLY valid JSON matching this schema:\n'
        f"{schema}\n"
        'Rules: Provide ready-to-paste copy. No placeholders. '
        'Keep the headline under 120 characters. '
        'About section should be 3-5 short lines. '
        'Experience bullets must start with a strong verb and include a metric when possible.\n\n'
        f"PROFILE TEXT:\n{snippet}"
    )
    output = gemini_generate_content(prompt, temperature=0.25, max_output_tokens=1600)
    data = parse_gemini_payload(output)
    if not isinstance(data, dict):
        return {}
    return sanitize_ai_payload(data)


def normalize_score(value, default=0):
    try:
        return max(0, min(100, int(float(value))))
    except Exception:
        return default


def coerce_int(value, default=0):
    try:
        parsed = pd.to_numeric(value, errors="coerce")
        if pd.isna(parsed):
            return default
        return int(parsed)
    except Exception:
        return default


def clean_string_list(values, limit=None):
    items = []
    if not isinstance(values, list):
        return items
    for value in values:
        text = clean_bullet_text(str(value)).strip()
        if text:
            items.append(text)
    if isinstance(limit, int):
        return items[:limit]
    return items


def normalize_resume_line_reviews(values, fallback):
    items = []
    source = values if isinstance(values, list) and values else fallback
    for value in source or []:
        if not isinstance(value, dict):
            continue
        line = clean_bullet_text(str(value.get("line", ""))).strip()
        if not line or is_resume_heading_line(line) or is_resume_contact_line(line):
            continue
        status = str(value.get("status", "needs")).strip().lower()
        if status not in {"good", "needs", "neutral"}:
            status = "needs"
        items.append(
            {
                "line": line,
                "status": status,
                "reason": clean_bullet_text(str(value.get("reason", ""))).strip() or "Needs refinement.",
                "suggestion": clean_bullet_text(str(value.get("suggestion", ""))).strip(),
            }
        )
    return items[:40]


def normalize_resume_bullets(values, fallback):
    items = []
    source = values if isinstance(values, list) and values else fallback
    for value in source or []:
        if not isinstance(value, dict):
            continue
        original = clean_bullet_text(str(value.get("original", ""))).strip()
        suggestion = clean_bullet_text(str(value.get("suggestion", ""))).strip()
        if not original or not suggestion:
            continue
        if is_resume_heading_line(original) or is_resume_contact_line(original):
            continue
        items.append({"original": original, "suggestion": suggestion})
    return items[:16]


def dedupe_text_items(values, limit=None):
    items = []
    seen = set()
    for value in values or []:
        text = clean_bullet_text(str(value or "")).strip(" ,.;")
        if not text:
            continue
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        items.append(text)
        if isinstance(limit, int) and len(items) >= limit:
            break
    return items


def normalize_resume_level(value, fallback="Early Career"):
    raw = clean_bullet_text(str(value or "")).strip().lower()
    mapping = {
        "student": "Student / Entry-Level",
        "entry level": "Student / Entry-Level",
        "student / entry-level": "Student / Entry-Level",
        "early career": "Early Career",
        "mid level": "Mid-Level",
        "mid-level": "Mid-Level",
        "senior": "Senior",
        "senior individual contributor": "Senior",
        "lead": "Lead / Manager",
        "manager": "Lead / Manager",
        "lead / manager": "Lead / Manager",
    }
    return mapping.get(raw, clean_bullet_text(str(value or "")).strip() or fallback)


def normalize_resume_checklist(values, fallback):
    items = []
    source = values if isinstance(values, list) and values else fallback
    for value in source or []:
        if not isinstance(value, dict):
            continue
        label = clean_bullet_text(str(value.get("label", ""))).strip()
        detail = clean_bullet_text(str(value.get("detail", ""))).strip()
        status = str(value.get("status", "needs")).strip().lower()
        if not label:
            continue
        if status not in {"good", "needs"}:
            status = "needs"
        items.append({"label": label, "status": status, "detail": detail})
    return items[:10]


def normalize_course_items(values, fallback):
    items = []
    source = values if isinstance(values, list) and values else fallback
    seen = set()
    for value in source or []:
        title = ""
        url = ""
        if isinstance(value, dict):
            title = clean_bullet_text(str(value.get("title", ""))).strip()
            url = clean_bullet_text(str(value.get("url", ""))).strip()
        elif isinstance(value, str):
            text = clean_bullet_text(value).strip()
            title = text
        if not title:
            continue
        key = (title.lower(), url.lower())
        if key in seen:
            continue
        seen.add(key)
        items.append({"title": title, "url": url})
    return items[:8]


def normalize_skill_token(value):
    cleaned = re.sub(r"[^a-z0-9+#./& ]+", " ", (value or "").lower()).strip()
    cleaned = re.sub(r"\s{2,}", " ", cleaned)
    return cleaned


def format_skill_label(value):
    raw = clean_bullet_text(str(value or "")).strip()
    lowered = raw.lower()
    special = {
        "sql": "SQL",
        "python": "Python",
        "java": "Java",
        "javascript": "JavaScript",
        "typescript": "TypeScript",
        "node.js": "Node.js",
        "node": "Node.js",
        "react": "React",
        "next.js": "Next.js",
        "aws": "AWS",
        "gcp": "GCP",
        "api": "API",
        "rest": "REST",
        "ci/cd": "CI/CD",
        "seo/sem": "SEO/SEM",
        "power bi": "Power BI",
        "figma": "Figma",
        "ui/ux": "UI/UX",
        "a/b testing": "A/B Testing",
    }
    if lowered in special:
        return special[lowered]
    if raw.isupper() and len(raw) <= 6:
        return raw
    return raw.title()


def extract_resume_skills_list(sections, text):
    explicit = []
    skills_text = sections.get("skills", "") if isinstance(sections, dict) else ""
    if skills_text:
        for piece in re.split(r"[,;\n|]+", skills_text):
            cleaned = clean_bullet_text(piece).strip(" -:")
            if not cleaned:
                continue
            if len(cleaned) < 2 or len(cleaned) > 40:
                continue
            explicit.append(cleaned)

    keywords = extract_keywords(text, limit=24)
    inferred = []
    for keyword in keywords:
        if keyword in {"experience", "education", "summary", "skills", "project", "projects"}:
            continue
        if len(keyword) < 3:
            continue
        inferred.append(keyword)

    merged = []
    seen = set()
    for value in explicit + inferred:
        token = normalize_skill_token(value)
        if not token or token in seen:
            continue
        seen.add(token)
        merged.append(format_skill_label(value))
    return merged[:24]


def estimate_years_experience(text):
    years = []
    for match in re.finditer(r"(\d{1,2})\s*\+?\s*(?:years|yrs)", text or "", re.I):
        try:
            years.append(int(match.group(1)))
        except Exception:
            continue
    return max(years) if years else 0


def infer_candidate_level(text, years_experience, sections):
    if years_experience >= 9:
        return "Lead / Manager"
    if years_experience >= 5:
        return "Senior"
    if years_experience >= 2:
        return "Mid-Level"
    education_text = sections.get("education", "") if isinstance(sections, dict) else ""
    lowered = (text or "").lower()
    if re.search(r"\b(intern|internship|graduate|student|campus|fresher)\b", lowered) or education_text:
        return "Student / Entry-Level"
    return "Early Career"


def infer_role_family(text, skills_list):
    haystack = " ".join([text or ""] + list(skills_list or [])).lower()
    best_family = "Operations / Program Management"
    best_score = 0
    best_matches = []
    best_hints = ROLE_FAMILY_PROFILES[best_family]["role_hints"]
    for family, profile in ROLE_FAMILY_PROFILES.items():
        score = 0
        matches = []
        for keyword in profile.get("keywords", []):
            if keyword in haystack:
                score += 2 if " " in keyword else 1
                matches.append(keyword)
        if score > best_score:
            best_score = score
            best_family = family
            best_matches = matches
            best_hints = profile.get("role_hints", [])
    return best_family, dedupe_text_items(best_matches, limit=6), dedupe_text_items(best_hints, limit=4)


def build_resume_checklist(contact_score, summary_text, exp_lines, has_numbers, skills_list, edu_text, fmt_score, sections):
    projects_present = bool((sections.get("projects", "") or "").strip())
    leadership_present = bool((sections.get("leadership", "") or "").strip())
    return [
        {
            "label": "Contact block is complete",
            "status": "good" if contact_score >= 80 else "needs",
            "detail": "Email, phone, and LinkedIn or portfolio should appear near the top.",
        },
        {
            "label": "Summary is role-specific",
            "status": "good" if len(summary_text or "") >= 60 else "needs",
            "detail": "Use a concise 2-3 line summary aligned to the target role.",
        },
        {
            "label": "Experience shows quantified impact",
            "status": "good" if exp_lines and has_numbers else "needs",
            "detail": "Bullets should show action, context, and measurable outcome.",
        },
        {
            "label": "Skills section supports ATS matching",
            "status": "good" if len(skills_list or []) >= 8 else "needs",
            "detail": "Group core tools, platforms, and domain skills instead of a short list.",
        },
        {
            "label": "Education details are explicit",
            "status": "good" if bool(edu_text and edu_text.strip()) else "needs",
            "detail": "Include degree, institution, and graduation year where possible.",
        },
        {
            "label": "Proof sections strengthen credibility",
            "status": "good" if projects_present or leadership_present else "needs",
            "detail": "Projects, leadership, or achievements sections help validate depth.",
        },
        {
            "label": "Formatting is ATS-friendly",
            "status": "good" if fmt_score >= 75 else "needs",
            "detail": "Keep the resume concise, text-first, and easy to parse.",
        },
    ]


def build_resume_strengths(sections, breakdown, skills_list, has_numbers):
    strengths = []
    if breakdown.get("Summary", 0) >= 75:
        strengths.append("The summary gives the reviewer a usable high-level profile.")
    if breakdown.get("Experience", 0) >= 80 and has_numbers:
        strengths.append("Experience bullets already show quantified impact, which improves ATS and recruiter fit.")
    if len(skills_list or []) >= 8:
        strengths.append("Skills coverage is broad enough to support keyword matching across multiple roles.")
    if (sections.get("projects", "") or "").strip():
        strengths.append("Projects provide additional evidence of execution beyond core work history.")
    if (sections.get("leadership", "") or "").strip():
        strengths.append("Leadership signals help show ownership and cross-functional credibility.")
    if breakdown.get("Contact Info", 0) >= 90:
        strengths.append("The contact block is ATS-friendly and easy for recruiters to use.")
    return dedupe_text_items(strengths, limit=5)


def build_learning_recommendations(role_family, missing_skills, candidate_level):
    profile = ROLE_FAMILY_PROFILES.get(role_family, {})
    recommendations = []
    if missing_skills:
        recommendations.append(
            f"Close the highest-signal skill gaps first: {', '.join(missing_skills[:4])}."
        )
    if candidate_level in {"Student / Entry-Level", "Early Career"}:
        recommendations.append("Add one portfolio-quality case study or project that mirrors the target role.")
    elif candidate_level in {"Mid-Level", "Senior"}:
        recommendations.append("Rewrite experience to emphasize ownership, decision-making, and business impact.")
    recommendations.extend(profile.get("learning_recommendations", []))
    return dedupe_text_items(recommendations, limit=4)


def select_seeded_items(items, seed_text, limit=4):
    pool = list(items or [])
    if not pool:
        return []
    if len(pool) <= limit:
        return pool
    digest = hashlib.sha256((seed_text or "").encode("utf-8", errors="ignore")).hexdigest()
    offset = int(digest[:8], 16) % len(pool)
    ordered = pool[offset:] + pool[:offset]
    return ordered[:limit]


def build_role_recommendation_pack(role_family, seed_text):
    course_pool = ROLE_FAMILY_COURSES.get(role_family) or []
    if not course_pool:
        default_pool = []
        for value in ROLE_FAMILY_COURSES.values():
            default_pool.extend(value[:2])
        course_pool = default_pool
    courses = select_seeded_items(course_pool, f"{seed_text}-courses", limit=5)
    resume_videos = select_seeded_items(RESUME_RESOURCE_VIDEOS, f"{seed_text}-resume-videos", limit=3)
    interview_videos = select_seeded_items(INTERVIEW_RESOURCE_VIDEOS, f"{seed_text}-interview-videos", limit=3)
    return {
        "recommended_courses": courses,
        "resume_resources": resume_videos,
        "interview_resources": interview_videos,
    }


def merge_resume_analysis(fallback, ai_data):
    base = fallback or {}
    if not isinstance(ai_data, dict) or not ai_data:
        merged = dict(base)
        merged["analysis_engine"] = "rule_based"
        return merged
    analysis_engine = str(ai_data.get("_analysis_engine", "gemini")).strip().lower()
    if analysis_engine not in {"gemini", "ollama"}:
        analysis_engine = "gemini"

    breakdown_source = ai_data.get("breakdown") if isinstance(ai_data.get("breakdown"), dict) else {}
    fallback_breakdown = base.get("breakdown", {}) or {}
    breakdown = {}
    for key in ["Contact Info", "Summary", "Experience", "Skills", "Education", "Formatting"]:
        breakdown[key] = normalize_score(breakdown_source.get(key), fallback_breakdown.get(key, 0))

    recs = {}
    ai_recs = ai_data.get("recommendations") if isinstance(ai_data.get("recommendations"), dict) else {}
    fallback_recs = base.get("recommendations", {}) or {}
    for key in SECTION_HEADERS.keys():
        recs[key] = clean_string_list(ai_recs.get(key), limit=5) or clean_string_list(fallback_recs.get(key), limit=5)

    ai_sections = ai_data.get("sections") if isinstance(ai_data.get("sections"), dict) else {}
    fallback_sections = base.get("sections", {}) or {}
    sections = {}
    for key in SECTION_HEADERS.keys():
        text = clean_bullet_text(str(ai_sections.get(key, ""))).strip()
        sections[key] = text or clean_bullet_text(str(fallback_sections.get(key, ""))).strip()

    merged = {
        "overall_score": normalize_score(
            ai_data.get("overall_score"),
            int(sum(breakdown.values()) / len(breakdown)) if breakdown else base.get("overall_score", 0),
        ),
        "breakdown": breakdown,
        "issues": clean_string_list(ai_data.get("issues"), limit=10) or clean_string_list(base.get("issues"), limit=10),
        "recommendations": recs,
        "sections": sections,
        "line_reviews": normalize_resume_line_reviews(ai_data.get("line_reviews"), base.get("line_reviews")),
        "improved_bullets": normalize_resume_bullets(ai_data.get("improved_bullets"), base.get("improved_bullets")),
        "predicted_role_family": clean_bullet_text(str(ai_data.get("predicted_role_family", ""))).strip() or base.get("predicted_role_family", ""),
        "candidate_level": normalize_resume_level(ai_data.get("candidate_level"), fallback=base.get("candidate_level", "Early Career")),
        "estimated_years_experience": max(
            0,
            coerce_int(ai_data.get("estimated_years_experience"), default=0),
            coerce_int(base.get("estimated_years_experience"), default=0),
        ),
        "ats_readiness_score": normalize_score(ai_data.get("ats_readiness_score"), base.get("ats_readiness_score", base.get("overall_score", 0))),
        "skills_list": dedupe_text_items(ai_data.get("skills_list"), limit=24) or dedupe_text_items(base.get("skills_list"), limit=24),
        "recommended_skills": dedupe_text_items(ai_data.get("recommended_skills"), limit=12) or dedupe_text_items(base.get("recommended_skills"), limit=12),
        "missing_skills": dedupe_text_items(ai_data.get("missing_skills"), limit=12) or dedupe_text_items(base.get("missing_skills"), limit=12),
        "strengths": dedupe_text_items(ai_data.get("strengths"), limit=6) or dedupe_text_items(base.get("strengths"), limit=6),
        "learning_recommendations": dedupe_text_items(ai_data.get("learning_recommendations"), limit=6) or dedupe_text_items(base.get("learning_recommendations"), limit=6),
        "target_role_hints": dedupe_text_items(ai_data.get("target_role_hints"), limit=6) or dedupe_text_items(base.get("target_role_hints"), limit=6),
        "resume_checklist": normalize_resume_checklist(ai_data.get("resume_checklist"), base.get("resume_checklist")),
        "recommended_courses": normalize_course_items(ai_data.get("recommended_courses"), base.get("recommended_courses")),
        "resume_resources": dedupe_text_items(ai_data.get("resume_resources"), limit=4) or dedupe_text_items(base.get("resume_resources"), limit=4),
        "interview_resources": dedupe_text_items(ai_data.get("interview_resources"), limit=4) or dedupe_text_items(base.get("interview_resources"), limit=4),
        "analysis_engine": analysis_engine,
    }
    return merged


def gemini_resume_analysis(text):
    global LAST_GEMINI_ERROR
    cache_key = hashlib.sha256((text or "").encode("utf-8", errors="ignore")).hexdigest()
    cached = RESUME_AI_CACHE.get(cache_key)
    if isinstance(cached, dict) and cached:
        return cached
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    has_gemini = bool(api_key)
    has_ollama = is_ollama_configured()
    if not has_gemini:
        LAST_GEMINI_ERROR = "Missing GEMINI_API_KEY."
    resume_model = os.getenv("GEMINI_RESUME_MODEL", "").strip()
    if not resume_model:
        configured_model = os.getenv("GEMINI_MODEL", "gemini-1.5-flash").strip()
        resume_model = "gemini-2.0-flash" if "preview" in configured_model.lower() else configured_model
    ollama_model = os.getenv("OLLAMA_MODEL", "").strip()
    snippet = (text or "")[:15000]
    schema = (
        "{"
        '"overall_score": integer 0-100, '
        '"ats_readiness_score": integer 0-100, '
        '"breakdown": {"Contact Info": integer 0-100, "Summary": integer 0-100, "Experience": integer 0-100, "Skills": integer 0-100, "Education": integer 0-100, "Formatting": integer 0-100}, '
        '"predicted_role_family": string, '
        '"candidate_level": string, '
        '"estimated_years_experience": integer, '
        '"skills_list": [string], '
        '"recommended_skills": [string], '
        '"missing_skills": [string], '
        '"strengths": [string], '
        '"learning_recommendations": [string], '
        '"target_role_hints": [string], '
        '"recommended_courses": [{"title": string, "url": string}], '
        '"resume_resources": [string], '
        '"interview_resources": [string], '
        '"issues": [string], '
        '"recommendations": {"summary": [string], "experience": [string], "skills": [string], "education": [string]}, '
        '"resume_checklist": [{"label": string, "status": "good"|"needs", "detail": string}], '
        '"line_reviews": [{"line": string, "status": "good"|"needs"|"neutral", "reason": string, "suggestion": string}]'
        "}"
    )
    prompt = (
        "You are an expert ATS and resume reviewer. Analyze the resume text semantically, not mechanically.\n"
        "Important rules:\n"
        "- Resume text may come from PDF extraction with broken line breaks.\n"
        "- Reconstruct sections logically.\n"
        "- Do NOT treat section headers, the candidate name, phone numbers, emails, LinkedIn URLs, or portfolio URLs as bullets.\n"
        "- Keep line_reviews focused on real content lines only.\n"
        "- Improved bullets should only be for substantive summary/experience/project/leadership bullets.\n"
        "- Limit issues to 6 items maximum.\n"
        "- Limit recommendations to 3 per section maximum.\n"
        "- Limit strengths, missing_skills, recommended_skills, learning_recommendations, and target_role_hints to 5 items each maximum.\n"
        "- Limit recommended_courses to 5 items and provide valid direct URLs.\n"
        "- Limit resume_resources and interview_resources to 3 links each.\n"
        "- Keep predicted_role_family concrete, such as Product Management, Software Engineering, Data / Analytics, Marketing / Growth, Operations / Program Management, or Design / UX.\n"
        "- Keep candidate_level concrete, such as Student / Entry-Level, Early Career, Mid-Level, Senior, or Lead / Manager.\n"
        "- Limit line_reviews to the 8 highest-signal items maximum.\n"
        "- Use 0-100 integers for all scores.\n"
        "- Return ONLY valid JSON matching this schema:\n"
        f"{schema}\n\n"
        f"RESUME TEXT:\n{snippet}"
    )
    if has_gemini:
        output = gemini_generate_content(
            prompt,
            temperature=0.2,
            max_output_tokens=1100,
            extra_generation_config={
                "responseMimeType": "application/json",
                "thinkingConfig": {"thinkingBudget": 0},
            },
            model_override=resume_model,
        )
        data = parse_gemini_payload(output)
        if isinstance(data, dict) and data:
            cleaned = sanitize_ai_payload(data)
            if cleaned:
                cleaned["_analysis_engine"] = "gemini"
                RESUME_AI_CACHE[cache_key] = cleaned
                return cleaned

    if has_ollama:
        output = ollama_generate_content(
            prompt,
            temperature=0.2,
            max_output_tokens=1100,
            model_override=ollama_model,
        )
        data = parse_gemini_payload(output)
        if isinstance(data, dict) and data:
            cleaned = sanitize_ai_payload(data)
            if cleaned:
                cleaned["_analysis_engine"] = "ollama"
                RESUME_AI_CACHE[cache_key] = cleaned
                return cleaned

    return {}


def detect_company_context(text):
    if not text:
        return 'most recent employer'
    lowered = text.lower()
    if 'kotak' in lowered:
        return 'Kotak Mahindra Bank'
    if 'jio' in lowered:
        return 'Jio'
    sections = split_linkedin_sections(text)
    exp_text = sections.get('experience', '')
    for line in exp_text.splitlines():
        cleaned = re.sub(r"[^A-Za-z0-9& ]+", ' ', line).strip()
        if len(cleaned.split()) >= 2:
            return cleaned[:60]
    return 'most recent employer'


def gemini_keyword_bullets(text, keyword, company_hint):
    api_key = os.getenv('GEMINI_API_KEY', '').strip()
    if not api_key or not keyword:
        return []
    snippet = (text or '')[:6000]
    prompt = (
        'Generate EXACTLY 3 bullet points for the user\'s experience at '
        f"{company_hint}. Each bullet must:\n"
        f"- include the keyword: {keyword}\n"
        '- be 1 sentence, 18-28 words\n'
        '- include a metric; if inferred, append [inferred]\n'
        '- be paste-ready and action-focused\n'
        'Return ONLY valid JSON as an array of strings.\n\n'
        f"PROFILE CONTEXT:\n{snippet}"
    )
    output = gemini_generate_content(prompt, temperature=0.4, max_output_tokens=260)
    data = parse_gemini_json(output)
    bullets = []
    if isinstance(data, dict) and isinstance(data.get('bullets'), list):
        bullets = data.get('bullets')
    elif isinstance(data, list):
        bullets = data
    cleaned = [clean_bullet_text(str(b)) for b in bullets if str(b).strip()]
    return cleaned[:3]


def fallback_keyword_bullets(text, keyword, company_hint):
    metric, inferred = extract_first_metric(text)
    metric_text = metric + (' [inferred]' if inferred else '')
    return [
        f"Integrated {keyword} into {company_hint} GTM strategy, improving funnel performance by {metric_text}.",
        f"Led {keyword} initiatives for {company_hint} to accelerate adoption, delivering {metric_text}.",
        f"Built a {keyword} playbook at {company_hint}, driving measurable impact of {metric_text}.",
    ]


def fetch_profile_text_from_url(url):
    raw = (url or "").strip()
    if not raw:
        return ""

    # Allow direct name search if user doesn't paste a URL.
    search_query = ""
    if "linkedin.com" not in raw and " " in raw:
        search_query = raw
        target_url = ""
    else:
        target_url = normalize_linkedin_url(raw)

    # For non-LinkedIn URLs, attempt a public fetch.
    if target_url and "linkedin.com" not in target_url:
        try:
            import urllib.request
            req = urllib.request.Request(target_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
            soup = bs(html, "html.parser")
            text = soup.get_text("\n", strip=True)
            if len(text) > 400:
                return text
        except Exception:
            pass

    # Use Selenium for LinkedIn
    username = os.getenv("LINKEDIN_USERNAME", "")
    password = os.getenv("LINKEDIN_PASSWORD", "")
    if not username or not password:
        return ""

    driver = get_driver(headless=os.getenv("DEFAULT_HEADLESS", "0") == "1")
    try:
        if not ensure_logged_in(driver, username, password):
            raise RuntimeError("LinkedIn login not completed. Please login in the Chrome window and retry.")

        if search_query:
            target = open_people_results(driver, search_query)
            if target:
                driver.get(target)
        elif target_url:
            driver.get(target_url)

        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # If redirected to feed/authwall, try a people search using slug
        current = driver.current_url
        if any(x in current for x in ["/feed", "/checkpoint", "/authwall", "/login"]):
            slug = get_linkedin_slug(target_url) if target_url else ""
            name_guess = slug.replace("-", " ").strip() if slug else search_query
            if name_guess:
                target = open_people_results(driver, name_guess)
                if target:
                    driver.get(target)
                    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Expand "see more" sections if present
        try:
            for btn in driver.find_elements(By.XPATH, "//button[contains(., 'See more') or contains(., 'see more')]"):
                try:
                    driver.execute_script("arguments[0].click();", btn)
                except Exception:
                    pass
        except Exception:
            pass

        # Scroll to load sections
        for _ in range(6):
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(1)

        html = driver.page_source
        soup = bs(html, "html.parser")
        main = soup.find("main")
        text = main.get_text("\n", strip=True) if main else soup.get_text("\n", strip=True)
        return text
    except RuntimeError:
        raise
    except Exception:
        return ""
    finally:
        driver.quit()


def analyze_resume(text):
    sections = split_sections(text)
    issues = []
    recs = {k: [] for k in SECTION_HEADERS.keys()}
    line_reviews = []
    improved_bullets = []

    # Contact info
    top_lines = [l.strip() for l in text.splitlines() if l.strip()][:6]
    has_email = bool(extract_emails(" ".join(top_lines)))
    has_phone = bool(re.search(r"\b\+?\d[\d\s\-()]{7,}\b", " ".join(top_lines)))
    has_link = bool(re.search(r"(linkedin\.com|portfolio|github\.com)", " ".join(top_lines), re.I))

    contact_score = 40
    if has_email and has_phone:
        contact_score = 80
    if has_email and has_phone and has_link:
        contact_score = 100
    if not has_email:
        issues.append("Missing email in contact section.")
    if not has_phone:
        issues.append("Missing phone number in contact section.")
    if not has_link:
        issues.append("Consider adding LinkedIn or portfolio link.")

    # Summary
    summary_text = sections.get("summary", "")
    summary_len = len(summary_text)
    summary_score = 40
    if summary_len >= 60:
        summary_score = 75
    if summary_len >= 120:
        summary_score = 90
    if not summary_text:
        issues.append("Add a short professional summary.")
        recs["summary"].append("Include a 2-3 line summary tailored to the role.")

    # Experience
    exp_text = sections.get("experience", "")
    exp_lines = [l for l in exp_text.splitlines() if l.strip()]
    exp_score = 50
    bullet_lines = [l for l in exp_lines if l.strip().startswith(("-", "•", "*"))]
    has_numbers = any(re.search(r"\d|%", l) for l in exp_lines)
    if exp_lines and bullet_lines and has_numbers:
        exp_score = 90
    elif exp_lines:
        exp_score = 70
    else:
        issues.append("Add an Experience section with quantified bullets.")
        recs["experience"].append("Use bullets with metrics (impact, %, time saved).")

    # Skills
    skills_text = sections.get("skills", "")
    skills = [s.strip() for s in re.split(r"[,\n•-]+", skills_text) if s.strip()]
    skills_score = 50
    if len(skills) >= 8:
        skills_score = 90
    elif len(skills) >= 4:
        skills_score = 70
    else:
        issues.append("Expand the Skills section with core tools and domains.")
        recs["skills"].append("List 8-12 relevant skills, grouped by category.")

    # Education
    edu_text = sections.get("education", "")
    edu_score = 50
    if re.search(r"\b(bachelor|master|b\.?tech|b\.?e|mba|bsc|msc|phd)\b", edu_text, re.I):
        edu_score = 85
    else:
        issues.append("Add Education details (degree, year, institution).")
        recs["education"].append("Mention degree, university, and graduation year.")

    # Formatting
    word_count = len(tokenize(text))
    fmt_score = 80
    if word_count < 200:
        fmt_score = 60
        issues.append("Resume is too short; add key projects or impact.")
    if word_count > 1200:
        fmt_score = 60
        issues.append("Resume is too long; tighten bullets and remove noise.")

    breakdown = {
        "Contact Info": contact_score,
        "Summary": summary_score,
        "Experience": exp_score,
        "Skills": skills_score,
        "Education": edu_score,
        "Formatting": fmt_score,
    }
    overall = int(sum(breakdown.values()) / len(breakdown))
    skills_list = extract_resume_skills_list(sections, text)
    years_experience = estimate_years_experience(text)
    candidate_level = infer_candidate_level(text, years_experience, sections)
    predicted_role_family, role_signals, target_role_hints = infer_role_family(text, skills_list)
    role_profile = ROLE_FAMILY_PROFILES.get(predicted_role_family, {})
    recommended_skills = dedupe_text_items(role_profile.get("recommended_skills"), limit=10)
    existing_skill_tokens = {normalize_skill_token(item) for item in skills_list}
    missing_skills = [
        skill for skill in recommended_skills
        if normalize_skill_token(skill) not in existing_skill_tokens
    ][:8]
    ats_readiness_score = int(round(
        (contact_score * 0.18) +
        (summary_score * 0.12) +
        (exp_score * 0.30) +
        (skills_score * 0.18) +
        (edu_score * 0.10) +
        (fmt_score * 0.12)
    ))

    if role_signals and not summary_text:
        recs["summary"].append(
            f"Name the target role explicitly, for example {target_role_hints[0] if target_role_hints else predicted_role_family}."
        )
    if missing_skills:
        issues.append(f"Key skills for {predicted_role_family} are missing or not clearly stated: {', '.join(missing_skills[:4])}.")
        recs["skills"].append(f"Surface core role skills explicitly: {', '.join(missing_skills[:4])}.")

    strengths = build_resume_strengths(sections, breakdown, skills_list, has_numbers)
    learning_recommendations = build_learning_recommendations(predicted_role_family, missing_skills, candidate_level)
    resource_pack = build_role_recommendation_pack(predicted_role_family, text)
    resume_checklist = build_resume_checklist(
        contact_score=contact_score,
        summary_text=summary_text,
        exp_lines=exp_lines,
        has_numbers=has_numbers,
        skills_list=skills_list,
        edu_text=edu_text,
        fmt_score=fmt_score,
        sections=sections,
    )

    # Line-by-line analysis (focus on Experience and Summary)
    action_verbs = [
        "led","built","created","developed","launched","improved","increased","reduced",
        "optimized","managed","delivered","designed","implemented","automated","analyzed",
        "drove","scaled","owned","spearheaded","streamlined",
    ]
    for line in text.splitlines():
        raw = line.strip()
        if not raw:
            continue
        if is_resume_heading_line(raw):
            line_reviews.append(
                {"line": raw, "status": "neutral", "reason": "Section heading.", "suggestion": ""}
            )
            continue
        if is_resume_contact_line(raw):
            line_reviews.append(
                {"line": raw, "status": "neutral", "reason": "Header or contact information.", "suggestion": ""}
            )
            continue
        lowered = raw.lower()
        has_metric = bool(re.search(r"\d|%", raw))
        has_action = any(lowered.startswith(v) or f" {v} " in lowered for v in action_verbs)
        status = "neutral"
        reason = "Looks fine."
        suggestion = ""

        if len(raw) < 8:
            status = "needs"
            reason = "Too short; lacks clarity."
            suggestion = "Expand into a complete bullet with action + impact."
        elif has_action and has_metric:
            status = "good"
            reason = "Strong action + quantified impact."
        elif has_action and not has_metric:
            status = "needs"
            reason = "Good action, but missing measurable impact."
            suggestion = "Add a metric (%, $, time saved, scale)."
        elif not has_action and has_metric:
            status = "needs"
            reason = "Has metrics but missing clear action."
            suggestion = "Start with an action verb (Led, Built, Improved)."
        else:
            status = "needs"
            reason = "Generic statement without action or impact."
            suggestion = "Rewrite with action + result."

        line_reviews.append(
            {"line": raw, "status": status, "reason": reason, "suggestion": suggestion}
        )

        if status == "needs" and len(raw) >= 12:
            improved_bullets.append(
                {
                    "original": raw,
                    "suggestion": f"{raw.rstrip('.')} - quantify impact (e.g., +X%, -Y hrs, $Z).",
                }
            )

    return {
        "overall_score": overall,
        "ats_readiness_score": ats_readiness_score,
        "breakdown": breakdown,
        "issues": dedupe_text_items(issues, limit=10),
        "recommendations": recs,
        "sections": sections,
        "line_reviews": line_reviews,
        "improved_bullets": improved_bullets[:12],
        "predicted_role_family": predicted_role_family,
        "candidate_level": candidate_level,
        "estimated_years_experience": years_experience,
        "skills_list": skills_list,
        "recommended_skills": recommended_skills,
        "missing_skills": missing_skills,
        "strengths": strengths,
        "learning_recommendations": learning_recommendations,
        "target_role_hints": target_role_hints,
        "resume_checklist": resume_checklist,
        "recommended_courses": resource_pack.get("recommended_courses", []),
        "resume_resources": resource_pack.get("resume_resources", []),
        "interview_resources": resource_pack.get("interview_resources", []),
    }


def summarize_resume(text):
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    # Drop lines that look like contact info
    clean_lines = []
    for l in lines:
        if re.search(r"@|linkedin\.com|github\.com|portfolio|\\b\\+?\\d[\\d\\s-]{6,}\\b", l, re.I):
            continue
        clean_lines.append(l)
    summary = " ".join(clean_lines[:2]) if clean_lines else (" ".join(lines[:2]) if lines else "")
    skills = extract_keywords(text, limit=12)
    achievements = extract_achievements(text, limit=3)
    return {
        "summary": summary,
        "skills": skills,
        "achievements": achievements,
    }


def extract_role_from_post(text):
    if not text:
        return ""
    m = re.search(r"(hiring|looking for|seeking)\\s+([A-Za-z0-9/ &-]{3,40})", text, re.I)
    if m:
        return m.group(2).strip()
    m = re.search(r"(role|position)\\s*[:\\-]\\s*([A-Za-z0-9/ &-]{3,40})", text, re.I)
    if m:
        return m.group(2).strip()
    return ""


def _clean_sentence(text, max_len=180):
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > max_len:
        text = text[: max_len].rsplit(" ", 1)[0] + "…"
    return text


def generate_email(
    rec,
    resume_profile,
    sender_name,
    sender_contact,
    subject_template=None,
    body_template=None,
    include_links=True,
    include_achievements=True,
):
    template = get_email_template(DEFAULT_EMAIL_TEMPLATE_ID)
    if not subject_template:
        subject_template = template["subject"]
    if not body_template:
        body_template = template["body"]

    context = build_email_context(rec, resume_profile, sender_name, sender_contact)
    if not include_links:
        context["apply_links"] = ""
        context["post_link"] = ""
    if not include_achievements:
        context["achievements"] = ""

    subject = render_email_template(subject_template, context)
    body = render_email_template(body_template, context)

    if not subject:
        subject = f"Application for {context.get('role') or 'open roles'}"
    if not body:
        body = "Hello Hiring Team\n\nResume attached.\n\nThank you,\n" + (sender_name or "Your Name")

    return subject, body


def send_email_with_attachment(
    smtp_host,
    smtp_port,
    smtp_user,
    smtp_pass,
    to_email,
    subject,
    body,
    attachment_path,
):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = to_email
    msg.set_content(body)
    if TRACKING_BASE_URL:
        tracking_token = build_tracking_token()
        tracking_url = build_tracking_pixel_url(tracking_token)
        msg.add_alternative(build_email_html(body, tracking_url), subtype="html")
    else:
        tracking_token = None
        tracking_url = ""

    if attachment_path:
        attach_file(msg, attachment_path)

    with smtplib.SMTP(smtp_host, smtp_port, timeout=30) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
    if tracking_token:
        log_email_tracking(tracking_token, to_email, subject, "smtp")


def build_client_config(client_id, client_secret):
    return {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": ["http://localhost", "http://127.0.0.1"],
        }
    }


def get_gmail_service(credentials_path, token_path, client_id=None, client_secret=None):
    scopes = ["https://www.googleapis.com/auth/gmail.send"]
    creds = None

    if Path(token_path).exists():
        creds = Credentials.from_authorized_user_file(token_path, scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if client_id and client_secret:
                client_config = build_client_config(client_id, client_secret)
                flow = InstalledAppFlow.from_client_config(client_config, scopes)
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_path, scopes)
            creds = flow.run_local_server(port=0)
        with open(token_path, "w", encoding="utf-8") as f:
            f.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def send_email_gmail_api(credentials_path, token_path, to_email, subject, body, attachment_path, client_id=None, client_secret=None):
    service = get_gmail_service(credentials_path, token_path, client_id=client_id, client_secret=client_secret)

    message = EmailMessage()
    message["To"] = to_email
    message["Subject"] = subject
    message.set_content(body)
    tracking_token = None
    tracking_url = ""
    if TRACKING_BASE_URL:
        tracking_token = build_tracking_token()
        tracking_url = build_tracking_pixel_url(tracking_token)
        message.add_alternative(build_email_html(body, tracking_url), subtype="html")
    if attachment_path:
        attach_file(message, attachment_path)
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")
    service.users().messages().send(userId="me", body={"raw": raw}).execute()
    if tracking_token:
        log_email_tracking(tracking_token, to_email, subject, "gmail_api")


def job_worker(job_id, query, companies, username, password, min_posts, headless, keywords, max_scrolls, email_cfg):
    job = JOBS[job_id]
    run_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def update(status):
        job["status"] = status
        job["updated_at"] = datetime.now().strftime("%H:%M:%S")

    try:
        raw_master = []
        quality_master = []
        company_files = []
        total = len(companies)

        for idx, company in enumerate(companies, start=1):
            if company:
                if "{company}" in query.lower():
                    company_query = re.sub(r"\{company\}", company, query, flags=re.IGNORECASE)
                else:
                    company_query = f"{query} {company}".strip()
            else:
                company_query = query

            job["current_company"] = company or ""
            job["company_index"] = idx
            job["company_total"] = total

            update(f"Scanning posts for {company_query} ({idx}/{total}).")

            keywords_eff = keywords[:]
            if company:
                keywords_eff = list(dict.fromkeys(keywords_eff + [company.lower()]))

            df = scan_posts(
                query=company_query,
                username=username,
                password=password,
                min_posts=min_posts,
                headless=headless,
                keywords=keywords_eff,
                max_scrolls=max_scrolls,
                status_cb=update,
            )
            if not df.empty:
                df = df.copy()
                df["Company"] = company or company_query
                raw_master.append(df)

            job["raw_rows"] += len(df)
            update(f"Agent filtering quality posts for {company_query} ({idx}/{total}).")

            quality_df = filter_quality(df, keywords_eff)
            if not quality_df.empty:
                quality_master.append(quality_df)
            job["quality_rows"] += len(quality_df)

            raw_xlsx, raw_csv = save_outputs(df, company_query, "raw", timestamp=run_timestamp)
            quality_xlsx, quality_csv = save_outputs(quality_df, company_query, "quality", timestamp=run_timestamp)
            company_files.append(
                {
                    "company": company or company_query,
                    "raw_xlsx": raw_xlsx.name,
                    "raw_csv": raw_csv.name,
                    "quality_xlsx": quality_xlsx.name,
                    "quality_csv": quality_csv.name,
                }
            )

        update("Creating master scan files.")
        if raw_master:
            master_raw_df = pd.concat(raw_master, ignore_index=True)
        else:
            master_raw_df = pd.DataFrame(
                columns=[
                    "Platform",
                    "Role",
                    "Location",
                    "Date",
                    "Primary Apply Link",
                    "Job Description",
                    "Post Text",
                    "Post Link",
                    "Apply Links",
                    "Emails",
                    "Phone Numbers",
                    "Author Name",
                    "All Links",
                    "Company",
                ]
            )
        if quality_master:
            master_df = pd.concat(quality_master, ignore_index=True)
        else:
            master_df = pd.DataFrame(
                columns=[
                    "Platform",
                    "Role",
                    "Location",
                    "Date",
                    "Primary Apply Link",
                    "Job Description",
                    "Post Text",
                    "Post Link",
                    "Apply Links",
                    "Emails",
                    "Phone Numbers",
                    "Author Name",
                    "All Links",
                    "Company",
                ]
            )

        master_raw_xlsx, master_raw_csv = save_outputs(master_raw_df, query, "master_raw", timestamp=run_timestamp)
        master_xlsx, master_csv = save_outputs(master_df, query, "master_quality", timestamp=run_timestamp)

        job["files"] = {
            "master_raw_xlsx": master_raw_xlsx.name,
            "master_raw_csv": master_raw_csv.name,
            "master_quality_xlsx": master_xlsx.name,
            "master_quality_csv": master_csv.name,
            "company_files": company_files,
        }

        if email_cfg and email_cfg.get("enabled"):
            update("Sending email with master quality file.")
            if email_cfg["mode"] == "gmail_api":
                send_email_gmail_api(
                    credentials_path=email_cfg["credentials_path"],
                    token_path=email_cfg["token_path"],
                    to_email=email_cfg["to"],
                    subject=email_cfg["subject"],
                    body=email_cfg["body"],
                    attachment_path=master_xlsx,
                    client_id=email_cfg.get("client_id"),
                    client_secret=email_cfg.get("client_secret"),
                )
            else:
                send_email_with_attachment(
                    smtp_host=email_cfg["host"],
                    smtp_port=email_cfg["port"],
                    smtp_user=email_cfg["user"],
                    smtp_pass=email_cfg["pass"],
                    to_email=email_cfg["to"],
                    subject=email_cfg["subject"],
                    body=email_cfg["body"],
                    attachment_path=master_xlsx,
                )

        job["done"] = True
        update("Done.")
    except Exception as exc:
        job["error"] = str(exc)
        job["done"] = True
        update("Failed.")


def universal_job_worker(job_id, scan_label, query, keywords, companies, locations, career_urls, source_names, limit_per_source, max_pages, direct_urls_only=False):
    job = JOBS[job_id]
    run_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    source_lookup = {name.lower(): idx for idx, name in enumerate(source_names or [], start=1)}

    def update(status, current_source=""):
        job["status"] = status
        job["updated_at"] = datetime.now().strftime("%H:%M:%S")
        if current_source:
            job["current_company"] = current_source
            job["company_index"] = source_lookup.get(current_source.lower(), job.get("company_index", 0))

    def status_cb(message):
        current_source = ""
        text = str(message or "").strip()
        if text.startswith("URL_PROGRESS::"):
            try:
                payload = json.loads(text.split("::", 1)[1])
            except Exception:
                payload = {}
            current_label = str(payload.get("label") or payload.get("url") or "").strip()
            try:
                job["company_index"] = max(0, int(payload.get("index") or 0))
            except Exception:
                pass
            try:
                total = int(payload.get("total") or 0)
            except Exception:
                total = 0
            if total > 0:
                job["company_total"] = total
            if current_label:
                job["current_company"] = current_label
            update(f"Scanning URL {job.get('company_index', 0)} of {job.get('company_total', 0)}.", current_source=current_label)
            return
        lowered = text.lower()
        for source_name in source_names or []:
            if lowered.startswith(source_name.lower()):
                current_source = source_name.title()
                break
        update(text or "Scanning sources.", current_source=current_source)

    empty_columns = [
        "Company",
        "Platform",
        "Role",
        "Location",
        "Date",
        "Primary Apply Link",
        "Apply Links",
        "Job Description",
        "Post Text",
        "Post Link",
        "Author Name",
        "Emails",
        "Phone Numbers",
        "All Links",
    ]

    try:
        update("Preparing universal sources.")
        df, meta = scan_universal_jobs(
            query=query,
            keywords=keywords,
            companies=companies,
            locations=locations,
            career_urls=career_urls,
            source_names=source_names,
            limit_per_source=limit_per_source,
            max_pages=max_pages,
            status_cb=status_cb,
            direct_urls_only=direct_urls_only,
        )
        if df.empty:
            df = pd.DataFrame(columns=empty_columns)
        else:
            df = df.copy()
            for column in empty_columns:
                if column not in df.columns:
                    df[column] = ""

        job["source_counts"] = meta.get("source_counts", {})
        job["resolved_targets"] = meta.get("resolved_targets", [])
        job["blocked_urls"] = meta.get("blocked_urls", [])
        job["unsupported_urls"] = meta.get("unsupported_urls", [])
        job["unsupported_count"] = int(meta.get("unsupported_count", 0) or 0)
        job["resolved_url_count"] = int(meta.get("resolved_url_count", 0) or 0)
        job["raw_rows"] = len(df)
        job["no_results"] = df.empty
        source_error_messages = []
        for source_name, errors in (meta.get("source_errors") or {}).items():
            for error in errors or []:
                text = str(error or "").strip()
                if text:
                    source_error_messages.append(f"{source_name.title()}: {text}")

        issue_rows = []
        for item in job.get("blocked_urls", []) or []:
            issue_rows.append(
                {
                    "Status": "blocked",
                    "Reason": str(item.get("reason") or "").strip(),
                    "Input URL": str(item.get("input_url") or "").strip(),
                    "URL": str(item.get("url") or "").strip(),
                    "Platform": str(item.get("platform") or "").strip(),
                }
            )
        for item in job.get("unsupported_urls", []) or []:
            issue_rows.append(
                {
                    "Status": "unsupported",
                    "Reason": str(item.get("reason") or "").strip(),
                    "Input URL": str(item.get("input_url") or "").strip(),
                    "URL": str(item.get("url") or "").strip(),
                    "Platform": str(item.get("platform") or "").strip(),
                }
            )

        issue_files = {}
        settings = load_auto_apply_settings()
        scanner_settings = settings.get("scanner", {}) if isinstance(settings.get("scanner"), dict) else {}
        if issue_rows:
            issues_df = pd.DataFrame(issue_rows)
            unsupported_xlsx, unsupported_csv = save_scan_issue_outputs(issues_df, scan_label, timestamp=run_timestamp)
            issue_files["unsupported_report_xlsx"] = unsupported_xlsx.name
            issue_files["unsupported_report_csv"] = unsupported_csv.name
            scanner_settings["last_unsupported_report_xlsx"] = unsupported_xlsx.name
            scanner_settings["last_unsupported_report_csv"] = unsupported_csv.name
        else:
            scanner_settings["last_unsupported_report_xlsx"] = ""
            scanner_settings["last_unsupported_report_csv"] = ""
        settings["scanner"] = scanner_settings
        save_auto_apply_settings(settings)

        if df.empty and source_error_messages and not issue_rows and not direct_urls_only:
            job["error"] = "; ".join(source_error_messages[:6])
            job["quality_rows"] = 0
            job["files"] = issue_files
            job["no_results"] = False
            job["done"] = True
            update("Failed.")
            return

        if df.empty:
            job["quality_rows"] = 0
            job["files"] = issue_files
            job["done"] = True
            update("No jobs found.")
            return

        quality_terms = []
        for value in [query] + list(keywords or []) + list(companies or []) + list(locations or []):
            text = str(value or "").strip().lower()
            if text and text not in quality_terms:
                quality_terms.append(text)
        if not quality_terms:
            quality_terms = build_scan_keywords()

        update("Filtering preferred jobs.")
        quality_df = filter_quality(df, quality_terms)
        if quality_df.empty:
            quality_df = pd.DataFrame(columns=df.columns)
        job["quality_rows"] = len(quality_df)

        update("Creating export files.")
        df_with_key = df.copy()
        df_with_key["_CompanyKey"] = df_with_key["Company"].fillna("").astype(str).str.strip()
        df_with_key.loc[df_with_key["_CompanyKey"] == "", "_CompanyKey"] = "Unknown Company"

        quality_with_key = quality_df.copy()
        if "_CompanyKey" not in quality_with_key.columns:
            quality_with_key["_CompanyKey"] = quality_with_key["Company"].fillna("").astype(str).str.strip()
            quality_with_key.loc[quality_with_key["_CompanyKey"] == "", "_CompanyKey"] = "Unknown Company"

        company_files = []
        company_names = sorted(set(df_with_key["_CompanyKey"].tolist()) | set(quality_with_key["_CompanyKey"].tolist()))
        for company_name in company_names:
            raw_company_df = df_with_key[df_with_key["_CompanyKey"] == company_name].drop(columns=["_CompanyKey"], errors="ignore")
            quality_company_df = quality_with_key[quality_with_key["_CompanyKey"] == company_name].drop(columns=["_CompanyKey"], errors="ignore")
            company_query = f"{scan_label} {company_name}".strip()
            raw_xlsx, raw_csv = save_outputs(raw_company_df, company_query, "raw", timestamp=run_timestamp)
            quality_xlsx, quality_csv = save_outputs(quality_company_df, company_query, "quality", timestamp=run_timestamp)
            company_files.append(
                {
                    "company": company_name,
                    "raw_xlsx": raw_xlsx.name,
                    "raw_csv": raw_csv.name,
                    "quality_xlsx": quality_xlsx.name,
                    "quality_csv": quality_csv.name,
                }
            )

        master_raw_xlsx, master_raw_csv = save_outputs(df.drop(columns=["_CompanyKey"], errors="ignore"), scan_label, "master_raw", timestamp=run_timestamp)
        master_xlsx, master_csv = save_outputs(quality_df.drop(columns=["_CompanyKey"], errors="ignore"), scan_label, "master_quality", timestamp=run_timestamp)

        job["files"] = {
            "master_raw_xlsx": master_raw_xlsx.name,
            "master_raw_csv": master_raw_csv.name,
            "master_quality_xlsx": master_xlsx.name,
            "master_quality_csv": master_csv.name,
            "company_files": company_files,
        }
        job["files"].update(issue_files)
        job["done"] = True
        update("Done.")
    except Exception as exc:
        job["error"] = str(exc)
        job["done"] = True
        update("Failed.")


def email_worker(
    job_id,
    recipients,
    attachment_path,
    email_cfg,
    resume_profile,
    sender_name,
    sender_contact,
    subject_template,
    body_template,
    include_links,
    include_achievements,
    send_delay,
    attach_resume,
):
    job = EMAIL_JOBS[job_id]

    def update(status):
        job["status"] = status
        job["updated_at"] = datetime.now().strftime("%H:%M:%S")

    try:
        update("Sending emails.")
        results = send_bulk_gmail_api(
            recipients=recipients,
            attachment_path=attachment_path,
            email_cfg=email_cfg,
            resume_profile=resume_profile,
            sender_name=sender_name,
            sender_contact=sender_contact,
            subject_template=subject_template,
            body_template=body_template,
            include_links=include_links,
            include_achievements=include_achievements,
            send_delay=send_delay,
            attach_resume=attach_resume,
            status_cb=update,
        )
        sent = sum(1 for r in results if r.get("status") == "sent")
        failed = len(results) - sent
        job["sent"] = sent
        job["failed"] = failed
        log_df = pd.DataFrame(results)
        log_path = OUTPUT_DIR / f"email_log_{job_id}.csv"
        log_df.to_csv(log_path, index=False, encoding="utf-8")
        job["log_file"] = log_path.name
        job["done"] = True
        update("Done.")
    except Exception as exc:
        job["error"] = str(exc)
        job["done"] = True
        update("Failed.")


def compiler_job_worker(
    job_id,
    scan_label,
    query,
    keywords,
    companies,
    locations,
    source_names,
    limit_per_source,
    max_pages,
    data_sources=None,
    export_formats=None,
):
    job = JOBS[job_id]
    run_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    generated_at = datetime.now().isoformat()
    data_sources = data_sources or ["internal"]
    export_formats = export_formats or ["career_feed", "atlas"]

    def status_cb(message):
        text = str(message or "").strip()
        job["updated_at"] = datetime.now().strftime("%H:%M:%S")
        job["status"] = text

    try:
        frames = []
        source_counts = {}

        if "internal" in data_sources:
            status_cb("Scanning native ATS sources...")
            df, meta = scan_universal_jobs(
                query=query,
                keywords=keywords,
                companies=companies,
                locations=locations,
                career_urls=[],
                source_names=source_names,
                limit_per_source=limit_per_source,
                max_pages=max_pages,
                status_cb=status_cb,
                direct_urls_only=False,
            )
            if not df.empty:
                frames.append(df)
            source_counts.update(meta.get("source_counts", {}) if isinstance(meta, dict) else {})

        if "public_ats" in data_sources:
            status_cb("Loading public ATS dataset...")
            public_raw = load_public_ats_jobs(status_cb=status_cb)
            public_df = normalize_public_ats_dataframe(public_raw)
            public_df = compiler_filter_dataframe(public_df, query, keywords, companies, locations)
            if not public_df.empty:
                frames.append(public_df)
            source_counts["Public ATS"] = len(public_df)

        if not frames:
            job["no_results"] = True
            job["done"] = True
            status_cb("No jobs found.")
            return

        df = pd.concat(frames, ignore_index=True) if len(frames) > 1 else frames[0]
        df = df.reset_index(drop=True)

        if df.empty:
            job["no_results"] = True
            job["done"] = True
            status_cb("No jobs found.")
            return

        job["raw_rows"] = len(df)
        job["source_counts"] = source_counts
        status_cb("Filtering and compiling feeds...")

        quality_terms = []
        for value in [query] + list(keywords or []) + list(companies or []) + list(locations or []):
            text = str(value or "").strip().lower()
            if text and text not in quality_terms:
                quality_terms.append(text)
        if not quality_terms:
            quality_terms = build_scan_keywords()

        quality_df = filter_quality(df, quality_terms)
        if quality_df.empty:
            quality_df = pd.DataFrame(columns=df.columns)
        job["quality_rows"] = len(quality_df)

        # Standard exports
        master_raw_xlsx, master_raw_csv = save_outputs(df, scan_label, "compiler_raw", timestamp=run_timestamp)
        master_xlsx, master_csv = save_outputs(quality_df, scan_label, "compiler_quality", timestamp=run_timestamp)

        files = {
            "master_raw_xlsx": master_raw_xlsx.name,
            "master_raw_csv": master_raw_csv.name,
            "master_quality_xlsx": master_xlsx.name,
            "master_quality_csv": master_csv.name,
        }

        if "career_feed" in export_formats:
            feed_records = build_career_feed_records(quality_df.fillna(""), generated_at, keywords=keywords)
            feed_path = OUTPUT_DIR / f"{slugify(scan_label)}_feed_{run_timestamp}.json"
            with open(feed_path, "w", encoding="utf-8") as f:
                json.dump(feed_records, f, indent=2)
            files["feed_json"] = feed_path.name

        if "atlas" in export_formats:
            atlas_data = build_atlas_payload(
                quality_df.fillna(""),
                generated_at,
                query,
                keywords,
                companies,
                locations,
                source_counts,
            )
            atlas_path = OUTPUT_DIR / f"{slugify(scan_label)}_atlas_{run_timestamp}.json"
            with open(atlas_path, "w", encoding="utf-8") as f:
                json.dump(atlas_data, f, indent=2)
            files["atlas_json"] = atlas_path.name

        summary_path = OUTPUT_DIR / f"{slugify(scan_label)}_compiler_summary_{run_timestamp}.json"
        summary = {
            "generated_at": generated_at,
            "query": query,
            "keywords": keywords or [],
            "companies": companies or [],
            "locations": locations or [],
            "data_sources": data_sources,
            "source_counts": source_counts,
            "raw_rows": len(df),
            "quality_rows": len(quality_df),
            "exports": export_formats,
        }
        with open(summary_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2)
        files["compiler_summary_json"] = summary_path.name

        job["files"] = files
        job["done"] = True
        status_cb("Done. Job feed compiled.")

    except Exception as exc:
        job["error"] = str(exc)
        job["done"] = True
        status_cb(f"Failed: {str(exc)}")


def render_auto_apply_page(settings=None, message="", error="", history=None, scan_defaults=None, status_code=200):
    settings = settings or load_auto_apply_settings()
    history = history if history is not None else load_auto_apply_history(limit=8)
    scan_history = list_scan_history(limit=8)
    resolved_scan_defaults = scan_defaults or build_auto_apply_scan_defaults(settings)
    context = {
        "settings": settings,
        "summary": get_auto_apply_summary(settings=settings, history=history),
        "workspace_metrics": get_auto_apply_workspace_metrics(history=history),
        "history": history,
        "message": message,
        "error": error,
        "scan_defaults": resolved_scan_defaults,
        "saved_scan_url_count": len(split_url_text((resolved_scan_defaults or {}).get("urls", ""))),
        "scan_history": scan_history,
    }
    rendered = render_template("auto_apply.html", **context)
    if status_code != 200:
        return rendered, status_code
    return rendered


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", metrics=get_dashboard_metrics())


@app.route("/scan", methods=["GET"])
def index():
    return render_template("index.html", defaults=get_defaults(), scan_history=list_scan_history())


@app.route("/auto-apply", methods=["GET", "POST"])
def auto_apply():
    settings = load_auto_apply_settings()
    message = ""
    error = ""

    if request.method == "POST":
        settings = save_auto_apply_settings(normalize_auto_apply_form(request.form, current_settings=settings))
        action = (request.form.get("action") or "save").strip().lower()
        if action == "trigger":
            run = queue_auto_apply_run(settings)
            return redirect(url_for("auto_apply_run_detail", run_id=run["id"]))
        else:
            message = "Auto-apply workspace saved."

    return render_auto_apply_page(
        settings=settings,
        message=message,
        error=error,
        history=load_auto_apply_history(limit=8),
    )


@app.route("/auto-apply/scan", methods=["POST"])
def auto_apply_scan_start():
    settings = load_auto_apply_settings()
    scan_defaults = build_auto_apply_scan_defaults(settings=settings, form=request.form)
    settings = save_auto_apply_scan_defaults(settings, scan_defaults)
    limit_per_source = parse_int_field(scan_defaults["limit_per_source"], 40, min_value=5, max_value=250)
    max_pages = parse_int_field(scan_defaults["max_pages"], 2, min_value=1, max_value=10)
    result = queue_universal_scan_job(
        query=scan_defaults["query"],
        keywords=scan_defaults["keywords"],
        companies_raw=scan_defaults["companies"],
        locations_raw=scan_defaults["locations"],
        career_urls_raw=scan_defaults["urls"],
        source_names=scan_defaults["sources"],
        limit_per_source=limit_per_source,
        max_pages=max_pages,
        scan_strategy=scan_defaults.get("strategy", DEFAULT_AUTO_APPLY_SCAN_STRATEGY),
    )
    if result.get("error"):
        return render_auto_apply_page(settings=settings, error=result["error"], scan_defaults=scan_defaults)
    return redirect(url_for("job", job_id=result["job_id"], from_page="auto-apply"))


@app.route("/auto-apply/run/<run_id>")
def auto_apply_run_detail(run_id):
    run = load_auto_apply_run(run_id)
    if not run:
        settings = load_auto_apply_settings()
        return render_auto_apply_page(
            settings=settings,
            error="Auto-apply run not found.",
            history=load_auto_apply_history(limit=8),
            status_code=404,
        )
    execution_config = get_auto_apply_connector_credentials()
    return render_template(
        "auto_apply_run.html",
        run=run,
        execution_config=execution_config,
        execution_policy=get_run_execution_policy(run, execution_config=execution_config),
        execution_error=(request.args.get("error") or "").strip(),
    )


@app.route("/auto-apply/run/<run_id>/execute", methods=["POST"])
def auto_apply_run_execute(run_id):
    run = load_auto_apply_run(run_id)
    if not run:
        abort(404)
    if not run.get("matches"):
        return redirect(url_for("auto_apply_run_detail", run_id=run_id))
    execution_config = get_auto_apply_connector_credentials()
    execution_policy = get_run_execution_policy(run, execution_config=execution_config)
    if not execution_policy["automation_enabled"]:
        return redirect(
            url_for(
                "auto_apply_run_detail",
                run_id=run_id,
                error="Apply flow is disabled for this run. Enable apply flow and create a new run to execute it.",
            )
        )

    exec_id = uuid.uuid4().hex[:10]
    job = {
        "id": exec_id,
        "run_id": run_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Queued for execution.",
        "updated_at": datetime.now().strftime("%H:%M:%S"),
        "total": len(run.get("matches", [])),
        "completed": 0,
        "submitted": 0,
        "prepared": 0,
        "failed": 0,
        "skipped": 0,
        "current_company": "",
        "current_role": "",
        "done": False,
        "error": "",
        "log_file": "",
        "results": [],
        "allow_submit": execution_policy["effective_allow_submit"],
        "require_review": execution_policy["require_review"],
    }
    AUTO_APPLY_EXECUTIONS[exec_id] = job
    save_auto_apply_execution(job)
    threading.Thread(target=auto_apply_execution_worker, args=(exec_id, run_id), daemon=True).start()
    return redirect(url_for("auto_apply_execution_page", exec_id=exec_id))


@app.route("/auto-apply/execution/<exec_id>")
def auto_apply_execution_page(exec_id):
    job = load_auto_apply_execution(exec_id)
    if not job:
        return render_template("auto_apply_execution.html", error="Execution job not found."), 404
    return render_template("auto_apply_execution.html", exec_id=exec_id, run_id=job.get("run_id"))


@app.route("/auto-apply/execution/<exec_id>/status")
def auto_apply_execution_status(exec_id):
    job = load_auto_apply_execution(exec_id)
    if not job:
        return jsonify({"error": "not_found"}), 404
    return jsonify(job)


@app.route("/profile")
def profile():
    return redirect(f"{url_for('auto_apply')}#applier")


@app.route("/credentials")
def credentials():
    return redirect(f"{url_for('auto_apply')}#applier")


@app.route("/linkedin-posts", methods=["GET", "POST"])
def linkedin_posts():
    output = ""
    error = ""
    if request.method == "POST":
        topic = request.form.get("topic", "").strip()
        audience = request.form.get("audience", "").strip()
        tone = request.form.get("tone", "").strip()
        length = request.form.get("length", "").strip()
        keywords = request.form.get("keywords", "").strip()
        cta = request.form.get("cta", "").strip()
        use_emojis = request.form.get("use_emojis") == "on"

        if not topic:
            error = "Add a topic or hook to generate a post."
        else:
            emoji_rule = "Include tasteful emojis." if use_emojis else "Do not use emojis."
            prompt = (
                "You are a LinkedIn content strategist. Create ONE post.\n"
                f"Topic: {topic}\n"
                f"Audience: {audience or 'General professional audience'}\n"
                f"Tone: {tone or 'Confident, helpful'}\n"
                f"Length: {length or '120-180 words'}\n"
                f"Keywords: {keywords or 'N/A'}\n"
                f"CTA: {cta or 'Invite readers to comment or share'}\n"
                f"{emoji_rule}\n"
                "Rules: Keep it scannable with short paragraphs. "
                "Avoid hashtags unless explicitly requested. "
                "Return ONLY the post text."
            )
            output = gemini_generate_content(prompt, temperature=0.55, max_output_tokens=500)
            if not output:
                error = "No output from Gemini. Check GEMINI_API_KEY or try again."

    return render_template(
        "linkedin_posts.html",
        output=output,
        error=error,
        gemini_enabled=bool(os.getenv("GEMINI_API_KEY", "").strip()),
    )


@app.route("/linkedin-review", methods=["GET", "POST"])
def linkedin_review():
    page = request.args.get("page", "1")
    view = request.args.get("view", "").strip().lower()
    view_all = view == "all"
    if request.method == "POST":
        url = request.form.get("profile_url", "").strip()
        pasted = request.form.get("profile_text", "").strip()
        upload = request.files.get("profile_file")
        text = ""
        source = ""
        if upload and upload.filename:
            filename = secure_filename(upload.filename)
            path = UPLOAD_DIR / f"linkedin_upload_{uuid.uuid4().hex}_{filename}"
            upload.save(path)
            text = extract_resume_text(path)
            source = "file"
        elif pasted:
            text = pasted
            source = "text"
        elif url:
            try:
                text = fetch_profile_text_from_url(url)
                source = "url"
            except RuntimeError as exc:
                history_all = list_linkedin_reviews()
                history, page, total_pages, total = paginate_items(history_all, page=page, per_page=20, view_all=view_all)
                return render_template(
                    "linkedin_review.html",
                    error=str(exc),
                    history=history,
                    trend_history=history_all,
                    gemini_enabled=bool(os.getenv("GEMINI_API_KEY", "").strip()),
                    page=page,
                    total_pages=total_pages,
                    view_all=view_all,
                    page_count=len(history),
                    total_count=total,
                )
        if not text:
            history_all = list_linkedin_reviews()
            history, page, total_pages, total = paginate_items(history_all, page=page, per_page=20, view_all=view_all)
            return render_template(
                "linkedin_review.html",
                error="Provide a LinkedIn URL, paste profile text, or upload a PDF/DOCX export. If the profile is private, ensure LinkedIn credentials are set in .env.",
                history=history,
                trend_history=history_all,
                gemini_enabled=bool(os.getenv("GEMINI_API_KEY", "").strip()),
                page=page,
                total_pages=total_pages,
                view_all=view_all,
                page_count=len(history),
                total_count=total,
            )

        analysis = analyze_linkedin_profile(text)
        analysis["source"] = source
        ai_payload = gemini_linkedin_analysis(text)
        if not ai_payload:
            ai_payload = build_fallback_ai(text, analysis)
        analysis["ai"] = ai_payload
        if isinstance(ai_payload.get("suggestions"), list):
            analysis["ai_suggestions"] = ai_payload.get("suggestions")
        if isinstance(ai_payload.get("keyword_analysis"), dict):
            analysis["ai_keywords"] = ai_payload.get("keyword_analysis")
        if isinstance(ai_payload.get("focus_areas"), list):
            analysis["ai_focus_areas"] = ai_payload.get("focus_areas")
        review_id = save_linkedin_review(text, analysis)
        return redirect(url_for("linkedin_review_detail", review_id=review_id))

    history_all = list_linkedin_reviews()
    history, page, total_pages, total = paginate_items(history_all, page=page, per_page=20, view_all=view_all)
    return render_template(
        "linkedin_review.html",
        history=history,
        trend_history=history_all,
        gemini_enabled=bool(os.getenv("GEMINI_API_KEY", "").strip()),
        page=page,
        total_pages=total_pages,
        view_all=view_all,
        page_count=len(history),
        total_count=total,
    )


@app.route("/linkedin-review/<review_id>")
def linkedin_review_detail(review_id):
    data = load_linkedin_review(review_id)
    if not data:
        history_all = list_linkedin_reviews()
        history, page, total_pages, total = paginate_items(history_all, page=1, per_page=20, view_all=False)
        return render_template(
            "linkedin_review.html",
            error="Review not found.",
            history=history,
            trend_history=history_all,
            gemini_enabled=bool(os.getenv("GEMINI_API_KEY", "").strip()),
            page=page,
            total_pages=total_pages,
            view_all=False,
            page_count=len(history),
            total_count=total,
        )
    gemini_enabled = bool(os.getenv("GEMINI_API_KEY", "").strip())
    return render_template("linkedin_review_detail.html", review=data, gemini_enabled=gemini_enabled)


@app.route("/linkedin-review/<review_id>/posts-analytics", methods=["POST"])
def linkedin_posts_analytics(review_id):
    data = load_linkedin_review(review_id)
    if not data:
        history_all = list_linkedin_reviews()
        history, page, total_pages, total = paginate_items(history_all, page=1, per_page=20, view_all=False)
        return render_template(
            "linkedin_review.html",
            error="Review not found.",
            history=history,
            trend_history=history_all,
            gemini_enabled=bool(os.getenv("GEMINI_API_KEY", "").strip()),
            page=page,
            total_pages=total_pages,
            view_all=False,
            page_count=len(history),
            total_count=total,
        )

    upload = request.files.get("posts_file")
    pasted = request.form.get("posts_text", "").strip()
    use_ai = request.form.get("use_ai") == "on"
    posts = []
    source = ""

    if upload and upload.filename:
        filename = secure_filename(upload.filename)
        path = UPLOAD_DIR / f"linkedin_posts_{uuid.uuid4().hex}_{filename}"
        upload.save(path)
        try:
            if path.suffix.lower() == ".csv":
                df = pd.read_csv(path)
            else:
                df = pd.read_excel(path)
            posts = parse_posts_from_dataframe(df)
            source = "upload"
        except Exception:
            posts = []
    elif pasted:
        source = "paste"
        try:
            if pasted.lstrip().startswith("{") or pasted.lstrip().startswith("["):
                payload = json.loads(pasted)
                if isinstance(payload, dict) and isinstance(payload.get("posts"), list):
                    posts = payload.get("posts")
                elif isinstance(payload, list):
                    posts = payload
            if not posts:
                lines = [l.strip() for l in pasted.splitlines() if l.strip()]
                posts = [{"content": line, "likes": 0, "comments": 0, "shares": 0, "impressions": 0} for line in lines]
        except Exception:
            posts = []

    analytics = analyze_posts(posts)
    if not analytics:
        gemini_enabled = bool(os.getenv("GEMINI_API_KEY", "").strip())
        return render_template(
            "linkedin_review_detail.html",
            review=data,
            gemini_enabled=gemini_enabled,
            analytics_error="Could not parse analytics data. Upload a CSV/XLSX or paste JSON.",
        )

    analytics["source"] = source or "paste"
    analytics["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if use_ai:
        profile_keywords = data.get("keyword_top", []) or []
        prompt = (
            "You are a LinkedIn content strategist. Based on the analytics and profile keywords below, "
            "suggest what to post next. Provide 5 post ideas and 3 content series themes.\n\n"
            f"Profile keywords: {', '.join(profile_keywords) if profile_keywords else 'N/A'}\n"
            f"Total posts: {analytics.get('total_posts')}\n"
            f"Avg engagement: {analytics.get('avg_engagement')}\n"
            f"Top topics: {', '.join(analytics.get('top_keywords', []))}\n"
            f"Low topics: {', '.join(analytics.get('bottom_keywords', []))}\n"
            f"What worked: {'; '.join(analytics.get('what_worked', []))}\n"
            f"What didn't: {'; '.join(analytics.get('what_didnt', []))}\n"
            "Return concise bullet points. No hashtags unless necessary."
        )
        ai_text = gemini_generate_content(prompt, temperature=0.5, max_output_tokens=500)
        analytics["ai_insights"] = ai_text or "No AI insights generated."

    update_linkedin_review(review_id, {"post_analytics": analytics})
    return redirect(url_for("linkedin_review_detail", review_id=review_id))


@app.route("/linkedin-review/<review_id>/keyword-bullets", methods=["POST"])
def linkedin_keyword_bullets(review_id):
    data = load_linkedin_review(review_id)
    if not data:
        return jsonify({"error": "Review not found."}), 404
    payload = request.get_json(silent=True) or {}
    keyword = (payload.get("keyword") or "").strip()
    if not keyword:
        return jsonify({"error": "Keyword is required."}), 400

    profile_text = data.get("text", "") or ""
    company_hint = detect_company_context(profile_text)
    bullets = gemini_keyword_bullets(profile_text, keyword, company_hint)
    if not bullets:
        bullets = fallback_keyword_bullets(profile_text, keyword, company_hint)
    if not bullets:
        return jsonify({"error": "No bullets generated."}), 500

    return jsonify({"keyword": keyword, "company": company_hint, "bullets": bullets})


@app.route("/resume-review", methods=["GET", "POST"])
def resume_review():
    page = request.args.get("page", "1")
    view = request.args.get("view", "").strip().lower()
    view_all = view == "all"
    has_gemini = bool(os.getenv("GEMINI_API_KEY", "").strip())
    ai_provider_label = get_resume_ai_provider_label()
    ai_enabled = bool(ai_provider_label)
    latest_full = load_latest_resume_review()
    top_fixes = build_resume_top_fixes(latest_full) if latest_full else []
    section_cards = build_resume_section_cards(latest_full) if latest_full else []
    ats_snapshot = build_resume_ats_snapshot(latest_full) if latest_full else {}
    if request.method == "POST":
        pasted = request.form.get("resume_text", "").strip()
        upload = request.files.get("resume_file")
        text = ""
        if pasted:
            text = pasted
        elif upload and upload.filename:
            filename = secure_filename(upload.filename)
            path = UPLOAD_DIR / f"resume_upload_{uuid.uuid4().hex}_{filename}"
            upload.save(path)
            text = extract_resume_text(path)

        if not text:
            history_all = list_resume_reviews()
            history, page, total_pages, total = paginate_items(history_all, page=page, per_page=20, view_all=view_all)
            return render_template(
                "resume_review.html",
                error="Provide resume text or upload a file.",
                history=history,
                trend_history=history_all,
                gemini_enabled=ai_enabled,
                ai_provider_label=ai_provider_label,
                latest_full=latest_full,
                top_fixes=top_fixes,
                section_cards=section_cards,
                ats_snapshot=ats_snapshot,
                page=page,
                total_pages=total_pages,
                view_all=view_all,
                page_count=len(history),
                total_count=total,
            )

        fallback_analysis = analyze_resume(text)
        ai_analysis = gemini_resume_analysis(text)
        analysis = merge_resume_analysis(fallback_analysis, ai_analysis)
        if analysis.get("analysis_engine") == "rule_based" and has_gemini:
            analysis["analysis_notice"] = format_gemini_error_message(
                LAST_GEMINI_ERROR,
                "Gemini analysis was unavailable, so the rule-based fallback was used.",
            )
        elif analysis.get("analysis_engine") == "ollama" and has_gemini and LAST_GEMINI_ERROR:
            analysis["analysis_notice"] = format_gemini_error_message(
                LAST_GEMINI_ERROR,
                "Gemini was unavailable for this run, so Ollama fallback was used.",
                fallback_label="Ollama fallback was used.",
            )
        review_id = save_resume_review(text, analysis)
        return redirect(url_for("resume_review_detail", review_id=review_id))

    history_all = list_resume_reviews()
    history, page, total_pages, total = paginate_items(history_all, page=page, per_page=20, view_all=view_all)
    return render_template(
        "resume_review.html",
        history=history,
        trend_history=history_all,
        gemini_enabled=ai_enabled,
        ai_provider_label=ai_provider_label,
        latest_full=latest_full,
        top_fixes=top_fixes,
        section_cards=section_cards,
        ats_snapshot=ats_snapshot,
        page=page,
        total_pages=total_pages,
        view_all=view_all,
        page_count=len(history),
        total_count=total,
    )


@app.route("/resume-review/<review_id>")
def resume_review_detail(review_id):
    data = load_resume_review(review_id)
    fix_all = bool(request.args.get("fix_all"))
    if not data:
        history_all = list_resume_reviews()
        history, page, total_pages, total = paginate_items(history_all, page=1, per_page=20, view_all=False)
        return render_template(
            "resume_review.html",
            error="Review not found.",
            history=history,
            trend_history=history_all,
            gemini_enabled=bool(get_resume_ai_provider_label()),
            ai_provider_label=get_resume_ai_provider_label(),
            latest_full=None,
            top_fixes=[],
            section_cards=[],
            ats_snapshot={},
            page=page,
            total_pages=total_pages,
            view_all=False,
            page_count=len(history),
            total_count=total,
        )
    return render_template(
        "resume_review_detail.html",
        review=data,
        section_report=build_resume_section_report(data),
        ats_snapshot=build_resume_ats_snapshot(data),
        recruiter_view=build_recruiter_view(data),
        fix_all=fix_all,
        gemini_enabled=bool(get_resume_ai_provider_label()),
        ai_provider_label=get_resume_ai_provider_label(),
    )


@app.route("/start", methods=["POST"])
def start():
    query = request.form.get("query", "").strip()
    companies_raw = request.form.get("companies", "").strip()
    min_posts = parse_int_field(request.form.get("min_posts", "").strip() or os.getenv("MIN_POSTS", "100"), 100, min_value=20, max_value=500)
    max_scrolls_raw = request.form.get("max_scrolls", "").strip() or os.getenv("MAX_SCROLLS", "")
    max_scrolls = parse_int_field(max_scrolls_raw, 40, min_value=1, max_value=500) if max_scrolls_raw else None
    result = queue_scan_job(query=query, companies_raw=companies_raw, min_posts=min_posts, max_scrolls=max_scrolls)
    if result.get("error"):
        return render_template("index.html", error=result["error"], defaults=get_defaults(), scan_history=list_scan_history())
    return redirect(url_for("job", job_id=result["job_id"]))


@app.route("/job/<job_id>")
def job(job_id):
    if job_id not in JOBS:
        return render_template("index.html", error="Job not found.", defaults=get_defaults(), scan_history=list_scan_history())
    from_page = (request.args.get("from_page") or "").strip().lower()
    back_href = "/scan"
    back_label = "Back to LinkedIn Scraper"
    if from_page == "auto-apply":
        back_href = "/auto-apply"
        back_label = "Back to Auto Job Apply"
    elif from_page == "job-compiler":
        back_href = "/job-compiler"
        back_label = "Back to Job Compiler"
    return render_template("job.html", job_id=job_id, back_href=back_href, back_label=back_label)


@app.route("/job/<job_id>/status")
def job_status(job_id):
    job = JOBS.get(job_id)
    if not job:
        return jsonify({"error": "not_found"}), 404
    payload = {
        "status": job["status"],
        "done": job["done"],
        "error": job["error"],
        "files": job["files"],
        "no_results": job.get("no_results", False),
        "raw_rows": job["raw_rows"],
        "quality_rows": job["quality_rows"],
        "current_company": job["current_company"],
        "company_index": job["company_index"],
        "company_total": job["company_total"],
        "updated_at": job["updated_at"],
        "scan_mode": job.get("scan_mode", "linkedin_posts"),
        "source_counts": job.get("source_counts", {}),
        "scan_strategy_label": job.get("scan_strategy_label", ""),
        "resolved_targets": job.get("resolved_targets", []),
        "blocked_urls": job.get("blocked_urls", []),
        "unsupported_urls": job.get("unsupported_urls", []),
        "unsupported_count": job.get("unsupported_count", 0),
        "resolved_url_count": job.get("resolved_url_count", 0),
    }
    return jsonify(payload)


@app.route("/email", methods=["GET"])
def email_select():
    email_cfg = get_email_cfg()
    if not (email_cfg["credentials_path"] or (email_cfg["client_id"] and email_cfg["client_secret"])):
        return render_template("email_select.html", error="Set Gmail OAuth credentials in .env before using email automation.")

    file_path = latest_master_quality_file()
    if not file_path:
        return render_template("email_select.html", error="No master quality file found. Run a scan first.")

    rows = load_quality_rows(file_path)
    if not rows:
        return render_template("email_select.html", error="No emails found in the master quality file.")

    stats = compute_recipient_stats(rows)
    unique_emails = len({(r.get("email") or "").strip().lower() for r in rows if r.get("email")})
    stats["unique_emails"] = unique_emails
    stats["total_rows"] = len(rows)

    view = request.args.get("view", "").strip().lower()
    page = int(request.args.get("page", "1") or 1)
    per_page = 20
    total_rows = len(rows)
    total_pages = max(1, (total_rows + per_page - 1) // per_page)
    if view == "all":
        page = 1
        total_pages = 1
        page_indices = range(total_rows)
    else:
        page = max(1, min(page, total_pages))
        start = (page - 1) * per_page
        end = start + per_page
        page_indices = range(start, min(end, total_rows))

    page_rows = [{**rows[i], "_idx": i} for i in page_indices]

    set_id = uuid.uuid4().hex
    EMAIL_SETS[set_id] = {"rows": rows, "stats": stats}

    return render_template(
        "email_select.html",
        rows=page_rows,
        set_id=set_id,
        file_name=file_path.name,
        stats=stats,
        page=page,
        total_pages=total_pages,
        view_all=view == "all",
        page_count=len(page_rows),
    )


@app.route("/email/compose", methods=["POST"])
def email_compose():
    set_id = request.form.get("set_id", "").strip()
    set_data = EMAIL_SETS.get(set_id, {})
    rows = set_data.get("rows", [])
    selected = request.form.getlist("selected")

    recipients = []
    for idx in selected:
        try:
            recipients.append(rows[int(idx)])
        except Exception:
            continue

    custom_emails = request.form.getlist("custom_email")
    custom_company = request.form.getlist("custom_company")
    custom_post_link = request.form.getlist("custom_post_link")
    custom_apply_links = request.form.getlist("custom_apply_links")

    for i, email in enumerate(custom_emails):
        email = (email or "").strip()
        if not email:
            continue
        recipients.append(
            {
                "email": email,
                "company": (custom_company[i] if i < len(custom_company) else "").strip(),
                "post_text": "",
                "post_link": (custom_post_link[i] if i < len(custom_post_link) else "").strip(),
                "apply_links": (custom_apply_links[i] if i < len(custom_apply_links) else "").strip(),
                "all_links": "",
            }
        )

    if not recipients:
        return render_template("email_select.html", error="Select at least one email.", rows=rows, set_id=set_id)

    recipients, duplicates = dedupe_recipients(recipients)
    stats = compute_recipient_stats(recipients)
    set_data["recipients"] = recipients
    set_data["dedupe_count"] = duplicates
    set_data["stats"] = stats
    EMAIL_SETS[set_id] = set_data

    return render_template("email_start.html", set_id=set_id)


@app.route("/email/start", methods=["POST"])
def email_start_post():
    set_id = request.form.get("set_id", "").strip()
    set_data = EMAIL_SETS.get(set_id, {})
    recipients = set_data.get("recipients", [])
    if not recipients:
        return render_template("email_select.html", error="Select at least one email.", rows=set_data.get("rows", []), set_id=set_id)

    resume = request.files.get("resume")
    if not resume or not resume.filename:
        return render_template("email_start.html", error="Please upload your resume.", set_id=set_id)

    filename = secure_filename(resume.filename)
    resume_path = UPLOAD_DIR / f"resume_{uuid.uuid4().hex}_{filename}"
    resume.save(resume_path)

    resume_text = extract_resume_text(resume_path)
    resume_profile = summarize_resume(resume_text)

    stats = set_data.get("stats") or compute_recipient_stats(recipients)
    duplicates = set_data.get("dedupe_count", 0)

    job_id = uuid.uuid4().hex
    EMAIL_JOBS[job_id] = {
        "recipients": recipients,
        "status": "Ready to send.",
        "done": False,
        "error": None,
        "sent": 0,
        "failed": 0,
        "log_file": "",
        "resume_profile": resume_profile,
        "resume_path": str(resume_path),
        "updated_at": datetime.now().strftime("%H:%M:%S"),
        "stats": stats,
        "duplicates": duplicates,
    }

    template = get_email_template(DEFAULT_EMAIL_TEMPLATE_ID)
    subject_template = template["subject"]
    body_template = template["body"]
    safe_profile = resume_profile or {"summary": "", "skills": [], "achievements": []}
    sample_context = build_email_context(recipients[0], safe_profile, "Your Name", "")
    sample_subject = render_email_template(subject_template, sample_context)
    sample_body = render_email_template(body_template, sample_context)

    return render_template(
        "email_compose.html",
        job_id=job_id,
        count=len(recipients),
        sample_subject=sample_subject,
        sample_body=sample_body,
        sample_context=sample_context,
        email_templates=EMAIL_TEMPLATES,
        template_id=template["id"],
        subject_template=subject_template,
        body_template=body_template,
        tokens=EMAIL_TOKENS,
        stats=stats,
        duplicates=duplicates,
    )


@app.route("/email/send/<job_id>", methods=["POST"])
def email_send(job_id):
    job = EMAIL_JOBS.get(job_id)
    if not job:
        template = get_email_template(DEFAULT_EMAIL_TEMPLATE_ID)
        subject_template = template["subject"]
        body_template = template["body"]
        sample_context = {
            "company": "Hiring Team",
            "role": "open roles",
            "skills": "",
            "summary": "",
            "achievements": "",
            "apply_links": "",
            "post_link": "",
            "sender_name": "Your Name",
            "sender_contact": "",
        }
        sample_subject = render_email_template(subject_template, sample_context)
        sample_body = render_email_template(body_template, sample_context)
        return render_template(
            "email_compose.html",
            error="Email job not found.",
            job_id=job_id,
            count=0,
            sample_subject=sample_subject,
            sample_body=sample_body,
            sample_context=sample_context,
            email_templates=EMAIL_TEMPLATES,
            template_id=template["id"],
            subject_template=subject_template,
            body_template=body_template,
            tokens=EMAIL_TOKENS,
            stats={"companies": 0, "missing_role": 0, "missing_apply": 0},
            duplicates=0,
        )

    sender_name = request.form.get("sender_name", "").strip()
    sender_contact = request.form.get("sender_contact", "").strip()
    template_id = request.form.get("template_id", "").strip() or DEFAULT_EMAIL_TEMPLATE_ID
    subject_template = request.form.get("subject_template", "").strip()
    body_template = request.form.get("body_template", "").strip()
    include_links = bool(request.form.get("include_links"))
    include_achievements = bool(request.form.get("include_achievements"))
    attach_resume = bool(request.form.get("attach_resume"))
    send_delay = normalize_delay(request.form.get("send_delay"))

    template = get_email_template(template_id)
    if not subject_template:
        subject_template = template["subject"]
    if not body_template:
        body_template = template["body"]

    safe_profile = job.get("resume_profile") or {"summary": "", "skills": [], "achievements": []}
    stats = job.get("stats") or compute_recipient_stats(job["recipients"])
    duplicates = job.get("duplicates", 0)
    sample_context = build_email_context(job["recipients"][0], safe_profile, sender_name or "Your Name", sender_contact)
    if not include_links:
        sample_context["apply_links"] = ""
        sample_context["post_link"] = ""
    if not include_achievements:
        sample_context["achievements"] = ""
    sample_subject = render_email_template(subject_template, sample_context)
    sample_body = render_email_template(body_template, sample_context)

    attach_path = job.get("resume_path", "")
    if not attach_path and attach_resume:
        return render_template(
            "email_compose.html",
            error="Resume not found. Please restart email automation.",
            job_id=job_id,
            count=len(job["recipients"]),
            sample_subject=sample_subject,
            sample_body=sample_body,
            sample_context=sample_context,
            email_templates=EMAIL_TEMPLATES,
            template_id=template_id,
            subject_template=subject_template,
            body_template=body_template,
            tokens=EMAIL_TOKENS,
            stats=stats,
            duplicates=duplicates,
        )

    email_cfg = get_email_cfg()
    if not (email_cfg["credentials_path"] or (email_cfg["client_id"] and email_cfg["client_secret"])):
        return render_template(
            "email_compose.html",
            error="Set Gmail OAuth credentials in .env.",
            job_id=job_id,
            count=len(job["recipients"]),
            sample_subject=sample_subject,
            sample_body=sample_body,
            sample_context=sample_context,
            email_templates=EMAIL_TEMPLATES,
            template_id=template_id,
            subject_template=subject_template,
            body_template=body_template,
            tokens=EMAIL_TOKENS,
            stats=stats,
            duplicates=duplicates,
        )

    job["subject_template"] = subject_template
    job["body_template"] = body_template
    job["include_links"] = include_links
    job["include_achievements"] = include_achievements
    job["send_delay"] = send_delay
    job["attach_resume"] = attach_resume
    job["template_id"] = template_id

    job["done"] = False
    job["status"] = "Queued."
    job["updated_at"] = datetime.now().strftime("%H:%M:%S")

    thread = threading.Thread(
        target=email_worker,
        args=(
            job_id,
            job["recipients"],
            str(attach_path),
            email_cfg,
            job.get("resume_profile", {}),
            sender_name,
            sender_contact,
            subject_template,
            body_template,
            include_links,
            include_achievements,
            send_delay,
            attach_resume,
        ),
        daemon=True,
    )
    thread.start()

    return redirect(url_for("email_status_page", job_id=job_id))


@app.route("/email/status/<job_id>")
def email_status(job_id):
    job = EMAIL_JOBS.get(job_id)
    if not job:
        return jsonify({"error": "not_found"}), 404
    payload = {
        "status": job["status"],
        "done": job["done"],
        "error": job["error"],
        "sent": job["sent"],
        "failed": job["failed"],
        "total": len(job["recipients"]),
        "log_file": job["log_file"],
        "updated_at": job["updated_at"],
    }
    return jsonify(payload)


@app.route("/email/progress/<job_id>")
def email_status_page(job_id):
    if job_id not in EMAIL_JOBS:
        return render_template("email_status.html", error="Email job not found.")
    return render_template("email_status.html", job_id=job_id)


@app.route("/scan-email/<job_id>", methods=["GET", "POST"])
def scan_email(job_id):
    job = JOBS.get(job_id)
    if not job:
        return render_template("scan_email.html", error="Scan job not found.")

    files = job.get("files", {})
    file_name = files.get("master_quality_xlsx") or files.get("master_quality_csv")
    file_path = resolve_output_path(file_name) if file_name else None
    if not file_path:
        return render_template("scan_email.html", error="Master quality file not available yet.")
    output_name = relative_output_name(file_path)

    if request.method == "POST":
        to_email = request.form.get("to_email", "").strip()
        if not to_email:
            return render_template("scan_email.html", error="Enter recipient email.", file_name=output_name, job_id=job_id)

        email_cfg = get_email_cfg()
        if not (email_cfg["credentials_path"] or (email_cfg["client_id"] and email_cfg["client_secret"])):
            return render_template("scan_email.html", error="Set Gmail OAuth credentials in .env.", file_name=output_name, job_id=job_id)

        try:
            send_email_gmail_api(
                credentials_path=email_cfg["credentials_path"],
                token_path=email_cfg["token_path"],
                to_email=to_email,
                subject="LinkedIn Hiring Scanner - Master Quality File",
                body="Attached is the master quality file from your scan.",
                attachment_path=str(file_path),
                client_id=email_cfg.get("client_id"),
                client_secret=email_cfg.get("client_secret"),
            )
            return render_template("scan_email.html", success=True, file_name=output_name, job_id=job_id)
        except Exception as exc:
            return render_template("scan_email.html", error=str(exc), file_name=output_name, job_id=job_id)

    return render_template("scan_email.html", file_name=output_name, job_id=job_id, label="Links and Emails Both")


@app.route("/scan-email-only/<job_id>", methods=["GET", "POST"])
def scan_email_only(job_id):
    job = JOBS.get(job_id)
    if not job:
        return render_template("scan_email.html", error="Scan job not found.")

    files = job.get("files", {})
    file_name = files.get("master_quality_xlsx") or files.get("master_quality_csv")
    source_path = resolve_output_path(file_name) if file_name else None
    if not source_path:
        return render_template("scan_email.html", error="Master quality file not available yet.")
    email_only_path = get_or_build_email_only_file(source_path)
    email_only_name = relative_output_name(email_only_path)

    if request.method == "POST":
        to_email = request.form.get("to_email", "").strip()
        if not to_email:
            return render_template("scan_email.html", error="Enter recipient email.", file_name=email_only_name, job_id=job_id, label="Email IDs Only")

        email_cfg = get_email_cfg()
        if not (email_cfg["credentials_path"] or (email_cfg["client_id"] and email_cfg["client_secret"])):
            return render_template("scan_email.html", error="Set Gmail OAuth credentials in .env.", file_name=email_only_name, job_id=job_id, label="Email IDs Only")

        try:
            send_email_gmail_api(
                credentials_path=email_cfg["credentials_path"],
                token_path=email_cfg["token_path"],
                to_email=to_email,
                subject="LinkedIn Hiring Scanner - Email IDs Only",
                body="Attached is the email-only file from your scan.",
                attachment_path=str(email_only_path),
                client_id=email_cfg.get("client_id"),
                client_secret=email_cfg.get("client_secret"),
            )
            return render_template("scan_email.html", success=True, file_name=email_only_name, job_id=job_id, label="Email IDs Only")
        except Exception as exc:
            return render_template("scan_email.html", error=str(exc), file_name=email_only_name, job_id=job_id, label="Email IDs Only")

    return render_template("scan_email.html", file_name=email_only_name, job_id=job_id, label="Email IDs Only")


@app.route("/scan-file-email/<path:filename>", methods=["GET", "POST"])
def scan_file_email(filename):
    file_path = resolve_output_path(filename)
    if not file_path:
        return render_scan_file_email_page(filename, error="Scan file not found.")
    output_name = relative_output_name(file_path)

    email_cfg = get_email_cfg()
    if request.method == "POST":
        to_email = request.form.get("to_email", "").strip()
        if not to_email:
            return render_scan_file_email_page(output_name, label="Past scan file", error="Enter recipient email.")
        if not (email_cfg["credentials_path"] or (email_cfg["client_id"] and email_cfg["client_secret"])):
            return render_scan_file_email_page(output_name, label="Past scan file", error="Set Gmail OAuth credentials in .env.")
        try:
            send_email_gmail_api(
                credentials_path=email_cfg["credentials_path"],
                token_path=email_cfg["token_path"],
                to_email=to_email,
                subject=f"Scan file: {file_path.name}",
                body="Attached is the requested scan file from Career Suite.",
                attachment_path=str(file_path),
                client_id=email_cfg.get("client_id"),
                client_secret=email_cfg.get("client_secret"),
            )
            return render_scan_file_email_page(output_name, label="Past scan file", success=True)
        except Exception as exc:
            return render_scan_file_email_page(output_name, label="Past scan file", error=str(exc))

    return render_scan_file_email_page(output_name, label="Past scan file")


@app.route("/download/<path:filename>")
def download(filename):
    file_path = resolve_output_path(filename)
    if not file_path:
        abort(404)
    return send_file(file_path, as_attachment=True, download_name=file_path.name)


@app.route("/job-compiler", methods=["GET"])
def job_compiler():
    return render_template(
        "job_compiler.html",
        ats_platforms=UNIVERSAL_SCAN_SOURCE_NAMES,
        compiler_sources=COMPILER_DATA_SOURCES,
        compiler_exports=COMPILER_EXPORTS,
        scan_history=list_scan_history(limit=10),
    )


@app.route("/job-compiler/start", methods=["POST"])
def job_compiler_start():
    query = request.form.get("query", "").strip()
    keywords = request.form.get("keywords", "").strip()
    companies_raw = request.form.get("companies", "").strip()
    locations_raw = request.form.get("locations", "").strip()
    data_sources = request.form.getlist("data_sources")
    sources = request.form.getlist("sources")
    export_formats = request.form.getlist("exports")
    limit_per_source = parse_int_field(request.form.get("limit_per_source"), 100, min_value=10, max_value=1000)
    max_pages = parse_int_field(request.form.get("max_pages"), 5, min_value=1, max_value=50)

    if not data_sources:
        data_sources = ["internal"]
    if "internal" not in data_sources:
        sources = []
    elif not sources:
        sources = UNIVERSAL_SCAN_SOURCE_NAMES
    if not export_formats:
        export_formats = ["career_feed", "atlas"]

    job_id = uuid.uuid4().hex
    scan_label = build_scan_run_label(query=query, keywords=split_multivalue_text(keywords), companies=split_multivalue_text(companies_raw))
    if not scan_label:
        scan_label = "job_compiler_feed"

    company_total = (len(sources) if "internal" in data_sources else 0) + (1 if "public_ats" in data_sources else 0)
    JOBS[job_id] = {
        "status": "Queued Compiler Job.",
        "done": False,
        "error": None,
        "files": {},
        "no_results": False,
        "raw_rows": 0,
        "quality_rows": 0,
        "current_company": "",
        "company_index": 0,
        "company_total": company_total,
        "updated_at": datetime.now().strftime("%H:%M:%S"),
        "scan_mode": "compiler",
        "scan_label": scan_label,
        "scan_strategy_label": "Compiler",
        "source_names": sources,
        "source_counts": {},
        "data_sources": data_sources,
        "export_formats": export_formats,
    }

    thread = threading.Thread(
        target=compiler_job_worker,
        args=(
            job_id, scan_label, query, 
            split_multivalue_text(keywords), 
            split_multivalue_text(companies_raw), 
            split_multivalue_text(locations_raw), 
            sources, limit_per_source, max_pages, data_sources, export_formats
        ),
        daemon=True,
    )
    thread.start()
    return redirect(url_for("job", job_id=job_id, from_page="job-compiler"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)



import time
from datetime import datetime

def run_job_scanner():
    print("Scanner started...")
    
    # 👉 CALL YOUR MAIN FUNCTION HERE
    # Example:
    # results = scan_jobs(...)
    
    print("Scanner finished...")


if __name__ == "__main__":
    while True:
        print(f"[{datetime.now()}] Running job scan...")
        
        try:
            run_job_scanner()
        except Exception as e:
            print("Error:", e)

        time.sleep(1800)  # runs every 30 mins


import os  # Make sure 'import os' is at the top of your file!

# ... rest of your code ...

if __name__ == '__main__':
    # Railway assigns a port automatically. Default to 5000 for local testing.
    port = int(os.environ.get("PORT", 5000))
    # host="0.0.0.0" is required to expose the app to the internet
    app.run(host="0.0.0.0", port=port)
