# Automated QA Framework — GeoTech AI Chatbot

![CI](https://github.com/DharunKosanam/QA-Automated-Framework/actions/workflows/tests.yml/badge.svg)

End-to-end test automation framework that drives a live RAG chatbot
(the UVic "GeoTech AI / Geotechnical Assistant") like a real user —
logging in, asking questions, and verifying the answers, timing, and
core user flows. Built with Python, Playwright, and pytest, with
GitHub Actions running validation on every push.

## Tech stack

- **Python** — language for the whole framework
- **Playwright** — drives a real browser (auto-waiting, headless-capable)
- **pytest** — test runner, fixtures, and the smoke/regression/performance markers
- **Page Object Model** — reusable, maintainable page logic
- **GitHub Actions** — CI that validates the suite on every push

## Key design decisions

- **Page Object Model:** each screen (`LoginPage`, `ChatPage`) owns its
  locators and actions, so a UI change is a one-line fix, not a rewrite.
- **Config-driven environments:** the target URL and credentials come from
  a `.env` file via `config.py` — the same tests can point at the live app
