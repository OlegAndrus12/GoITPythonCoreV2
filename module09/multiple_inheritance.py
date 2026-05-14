import random

# multiple inheritance via mixins: each mixin adds one independent behaviour
# neither mixin knows about the other — SmartHTTPClient combines them
#
# CacheMixin       RetryMixin       HTTPClient
#      \                |               /
#                SmartHTTPClient


class CacheMixin:
    def get_cached(self, url):
        return self._cache.get(url)

    def set_cached(self, url, data):
        self._cache[url] = data

    def is_cached(self, url):
        return url in self._cache


class RetryMixin:
    max_retries = 3

    def fetch_with_retry(self, url):
        for attempt in range(1, self.max_retries + 1):
            response = self._fetch(url)
            if response is not None:
                return response
            print(f"  [retry] attempt {attempt} failed for {url}")
        print(f"  [retry] all {self.max_retries} attempts exhausted")
        return None


class HTTPClient:
    def _fetch(self, url):
        # mock: fails 50% of the time to simulate network errors
        if random.random() < 0.5:
            return None
        return f"200 OK — body from {url}"

    def get(self, url):
        return self._fetch(url)


class SmartHTTPClient(CacheMixin, RetryMixin, HTTPClient):
    def __init__(self):
        self._cache = {}

    def get(self, url):
        if self.is_cached(url):
            print(f"[cache hit]  {url}")
            return self.get_cached(url)

        print(f"[cache miss] {url}")
        response = self.fetch_with_retry(url)
        if response:
            self.set_cached(url, response)
        return response


random.seed(42)

client = SmartHTTPClient()

print(client.get("https://api.example.com/users"))
print(client.get("https://api.example.com/posts"))
print()
print("--- repeat the same URLs ---")
print(client.get("https://api.example.com/users"))   # cache hit
print(client.get("https://api.example.com/posts"))   # cache hit

print()
print("--- MRO ---")
print(SmartHTTPClient.__mro__)
