import asyncio
from types import SimpleNamespace

from tests.test_main_observability import MainModuleHarness


class CatchAllResponseHeaderTests(MainModuleHarness):
    """The FastAPI catch-all must preserve route()'s response headers.

    /sitemap.xml is served through the catch-all; wrapping every
    response in HTMLResponse would discard its XML Content-Type.
    """

    def request(self, url):
        return SimpleNamespace(url=url)

    def test_sitemap_keeps_xml_content_type_through_the_catch_all(self):
        main = self.import_main()
        response = asyncio.run(
            main.not_found("sitemap.xml", self.request("https://example.test/sitemap.xml"))
        )
        self.assertEqual(response.headers["Content-Type"], "application/xml; charset=utf-8")
        self.assertIn("<urlset", response.content)
        self.assertEqual(response.status_code, 200)

    def test_journey_pages_stay_html_through_the_catch_all(self):
        main = self.import_main()
        response = asyncio.run(
            main.not_found("journeys", self.request("https://example.test/journeys"))
        )
        self.assertTrue(response.headers["Content-Type"].startswith("text/html"))
        self.assertEqual(response.status_code, 200)

    def test_about_page_stays_html_through_explicit_and_catch_all_routes(self):
        main = self.import_main()
        explicit = asyncio.run(main.about_page())
        fallback = asyncio.run(main.not_found("about", self.request("https://example.test/about")))
        for response in (explicit, fallback):
            self.assertTrue(response.headers["Content-Type"].startswith("text/html"))
            self.assertEqual(response.status_code, 200)
            self.assertIn('rel="canonical" href="https://www.pythonbyexample.dev/about"', response.content)

    def test_privacy_page_stays_html_through_explicit_and_catch_all_routes(self):
        main = self.import_main()
        explicit = asyncio.run(main.privacy_page())
        fallback = asyncio.run(main.not_found("privacy", self.request("https://example.test/privacy")))
        for response in (explicit, fallback):
            self.assertTrue(response.headers["Content-Type"].startswith("text/html"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(
                'rel="canonical" href="https://www.pythonbyexample.dev/privacy"',
                response.content,
            )

    def test_unknown_paths_fall_back_to_html(self):
        main = self.import_main()
        response = asyncio.run(
            main.not_found("no-such-page", self.request("https://example.test/no-such-page"))
        )
        self.assertEqual(response.status_code, 404)
        self.assertNotIn('rel="canonical"', response.content)
        self.assertNotIn('property="og:url"', response.content)
        self.assertIn('<meta name="robots" content="noindex">', response.content)
