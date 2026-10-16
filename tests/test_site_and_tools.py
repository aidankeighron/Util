"""
Unit tests for the Util site structure, navigation layouts, and clean catalog presentation.
"""

from typing import Dict, List, Optional, Set
import os
import unittest


class TestSiteStructure(unittest.TestCase):
    """
    Test suite verifying site structure, markdown front matter integrity,
    selector panel behavior, and clean root catalog presentation.
    """

    def setUp(self) -> None:
        """
        Initializes base paths for testing.
        """
        self.base_dir: str = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")
        )
        self.docs_dir: str = os.path.join(self.base_dir, "docs")
        self.assets_dir: str = os.path.join(self.docs_dir, "assets")
        self.languages_dir: str = os.path.join(self.assets_dir, "Languages")

    def _parse_front_matter(self, file_path: str) -> Dict[str, str]:
        """
        Parses YAML front matter from a markdown file.

        Args:
            file_path (str): The absolute path to the markdown file.

        Returns:
            Dict[str, str]: A dictionary containing key-value pairs from the front matter.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        front_matter: Dict[str, str] = {}
        with open(file_path, "r", encoding="utf-8") as file_handle:
            lines = file_handle.readlines()

        if len(lines) == 0:
            return front_matter

        if not lines[0].strip() == "---":
            return front_matter

        for line in lines[1:]:
            stripped_line = line.strip()
            if stripped_line == "---":
                break

            if ":" in stripped_line:
                key, value = stripped_line.split(":", 1)
                front_matter[key.strip()] = value.strip()

        return front_matter

    def test_storage_guide_files_removed(self) -> None:
        """
        Verifies that storage guide and architectural blueprint files are removed.

        Returns:
            None
        """
        site_doc_path: str = os.path.join(
            self.assets_dir, "Tools", "Storage Architecture.md"
        )
        standalone_doc_path: str = os.path.join(
            self.docs_dir, "STORAGE_ARCHITECTURE.md"
        )

        self.assertFalse(
            os.path.exists(site_doc_path),
            f"Storage guide should be removed at {site_doc_path}",
        )
        self.assertFalse(
            os.path.exists(standalone_doc_path),
            f"Standalone storage guide should be removed at {standalone_doc_path}",
        )

    def test_all_content_scripts_have_valid_front_matter(self) -> None:
        """
        Validates that all markdown content files have proper layout and language headers.

        Returns:
            None
        """
        available_categories: Set[str] = set()
        for filename in os.listdir(self.languages_dir):
            if filename.endswith(".md"):
                cat_name = filename[:-3]
                available_categories.add(cat_name)

        self.assertGreater(len(available_categories), 0)

        for root, _, files in os.walk(self.assets_dir):
            normalized_root = root.replace("\\", "/")
            if "assets/Languages" in normalized_root:
                continue

            for file in files:
                if not file.endswith(".md"):
                    continue

                full_path = os.path.join(root, file)
                front_matter = self._parse_front_matter(full_path)

                self.assertIn(
                    "layout",
                    front_matter,
                    f"Missing layout in {full_path}",
                )
                self.assertEqual(
                    front_matter["layout"],
                    "script",
                    f"Expected layout 'script' in {full_path}",
                )

                self.assertIn(
                    "language",
                    front_matter,
                    f"Missing language in {full_path}",
                )
                self.assertIn(
                    front_matter["language"],
                    available_categories,
                    f"Language {front_matter['language']} in {full_path} not found in Languages",
                )

    def test_selector_panel_templates_exist(self) -> None:
        """
        Verifies that the sidebar selector panel and layout templates exist.

        Returns:
            None
        """
        sidebar_path = os.path.join(self.docs_dir, "_includes", "sidebar.html")
        header_path = os.path.join(self.docs_dir, "_includes", "header.html")
        default_layout_path = os.path.join(self.docs_dir, "_layouts", "default.html")
        home_layout_path = os.path.join(self.docs_dir, "_layouts", "home.html")
        css_path = os.path.join(self.docs_dir, "assets", "css", "layout.css")
        js_path = os.path.join(self.docs_dir, "assets", "js", "main.js")

        self.assertTrue(os.path.exists(sidebar_path))
        self.assertTrue(os.path.exists(header_path))
        self.assertTrue(os.path.exists(default_layout_path))
        self.assertTrue(os.path.exists(home_layout_path))
        self.assertTrue(os.path.exists(css_path))
        self.assertTrue(os.path.exists(js_path))

    def test_scroll_persistence_logic_in_script(self) -> None:
        """
        Verifies that main.js contains scroll position restoration and
        scrollIntoView logic to keep the selected item in view.

        Returns:
            None
        """
        js_path = os.path.join(self.docs_dir, "assets", "js", "main.js")
        with open(js_path, "r", encoding="utf-8") as f:
            js_code = f.read()

        self.assertIn("scrollIntoView", js_code)
        self.assertIn("sessionStorage", js_code)
        self.assertIn("util_sidebar_scroll_top", js_code)

    def test_built_site_contains_selector_panel_and_stripped_home(self) -> None:
        """
        Verifies that the generated site contains the left selector panel,
        and that the root page is stripped down without blueprint text.

        Returns:
            None
        """
        site_index_path = os.path.join(self.docs_dir, "_site", "index.html")
        if not os.path.exists(site_index_path):
            self.skipTest("_site/index.html not built yet")

        with open(site_index_path, "r", encoding="utf-8") as f:
            index_html = f.read()

        self.assertIn('id="sidebar"', index_html)
        self.assertIn('id="sidebar-search"', index_html)
        self.assertIn('class="app-layout"', index_html)
        self.assertIn('class="catalog-sections"', index_html)
        self.assertNotIn("Architecture Blueprint", index_html)
        self.assertNotIn("Storage Guide", index_html)


if __name__ == "__main__":
    unittest.main()
