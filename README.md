# Indonesian Holidays Calendar

Indonesian public holiday calendar, updated automatically each year.

## Output

| Format | Description |
|--------|-------------|
| `.ics` | iCalendar — import into Google Calendar, Apple Calendar, Outlook, etc. |
| `.json` | JSON array with `date`, `event`, and `type` fields |

## Usage

### Subscribe via URL (auto-updates)

Use this URL to subscribe — calendar apps will sync changes automatically:

```
https://github.com/game5413/Indonesian-Holidays-Calendar/releases/latest/download/calendar.ics
```

| App | Steps |
|-----|-------|
| **Google Calendar** | Settings → Add calendar → From URL → paste URL |
| **Apple Calendar** | File → New Calendar Subscription → paste URL |
| **Outlook** | Add calendar → Subscribe from web → paste URL |

### Import file into calendar

Download [latest](https://github.com/game5413/Indonesian-Holidays-Calendar/releases/latest) calendar event, then import manually into your calendar app.

## Source

Data scraped from [kalenderku.id](https://kalenderku.id). Their say data sourced from **SKB 3 Menteri** (Surat Keputusan Bersama), a joint decree issued annually and signed by:

- Menteri Agama
- Menteri Ketenagakerjaan
- Menteri Pendayagunaan Aparatur Negara dan Reformasi Birokrasi (PANRB)

## New Release

Calendar files are generated automatically via GitHub Actions on a schedule every January. The latest release reflects the current year's holiday data.

> **Data availability:** Holiday data depends on the SKB 3 Menteri decree being published by the government. This document is typically released several months before the new year, but exact timing varies. If the calendar for the new year is not yet available at January 1st, it means the source data has not been published yet.

> **Note:** GitHub Actions scheduled workflows are not guaranteed to run at the exact scheduled time. Delays of 30–60 minutes are common, and in some cases the run may be skipped entirely during periods of high load or repository inactivity. See community discussions: [#156282](https://github.com/orgs/community/discussions/156282), [#52477](https://github.com/orgs/community/discussions/52477) — and a detailed write-up at [upptime.js.org](https://upptime.js.org/blog/2021/01/22/github-actions-schedule-not-working/).

If the latest release appears outdated, hit me on section [issues](https://github.com/game5413/Indonesian-Holidays-Calendar/issues) to manually dispatch the automation.