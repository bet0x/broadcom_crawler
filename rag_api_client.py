import os
import json
from typing import Any, Dict, List, Optional, Tuple, Union, Iterable

import requests


class RAGApiClient:
    """
    Minimal standalone client for Documents and Collections endpoints from the RAG MCP Server.

    Auth: Bearer token (use `api_key`), sent as `Authorization: Bearer <token>`.

    Only implements endpoints under `/documents` and `/collections`.
    """

    def __init__(
        self,
        base_url: str = "http://127.0.0.1:9000",
        api_key: Optional[str] = None,
        timeout_seconds: int = 60,
        session: Optional[requests.Session] = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key or os.environ.get("RAG_API_KEY")
        self.timeout_seconds = timeout_seconds
        self.session = session or requests.Session()

        if not self.api_key:
            raise ValueError(
                "API key is required. Pass api_key or set RAG_API_KEY environment variable."
            )

        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
        })

    # -----------------------------
    # Internal helpers
    # -----------------------------
    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def _handle_response(self, resp: requests.Response) -> Any:
        resp.raise_for_status()
        if not resp.content:
            return None
        content_type = resp.headers.get("Content-Type", "")
        if "application/json" in content_type:
            return resp.json()
        return resp.content

    # -----------------------------
    # Documents
    # -----------------------------
    def list_documents(
        self,
        skip: int = 0,
        limit: int = 50,
        status_filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {"skip": skip, "limit": limit}
        if status_filter is not None:
            params["status_filter"] = status_filter
        resp = self.session.get(self._url("/documents/"), params=params, timeout=self.timeout_seconds)
        return self._handle_response(resp)

    def get_document(self, document_id: int) -> Dict[str, Any]:
        resp = self.session.get(self._url(f"/documents/{document_id}"), timeout=self.timeout_seconds)
        return self._handle_response(resp)

    def delete_document(self, document_id: int) -> None:
        resp = self.session.delete(self._url(f"/documents/{document_id}"), timeout=self.timeout_seconds)
        self._handle_response(resp)

    def reprocess_document(self, document_id: int) -> Dict[str, Any]:
        resp = self.session.post(self._url(f"/documents/{document_id}/reprocess"), timeout=self.timeout_seconds)
        return self._handle_response(resp)

    def get_document_chunks(
        self, document_id: int, skip: int = 0, limit: int = 100
    ) -> List[Dict[str, Any]]:
        params = {"skip": skip, "limit": limit}
        resp = self.session.get(
            self._url(f"/documents/{document_id}/chunks"), params=params, timeout=self.timeout_seconds
        )
        return self._handle_response(resp)

    def get_document_stats(self) -> Dict[str, Any]:
        resp = self.session.get(self._url("/documents/stats"), timeout=self.timeout_seconds)
        return self._handle_response(resp)

    def assign_document_to_collections(
        self, document_id: int, collection_ids: List[int]
    ) -> Dict[str, Any]:
        payload = {"collection_ids": collection_ids}
        resp = self.session.post(
            self._url(f"/documents/{document_id}/collections"), json=payload, timeout=self.timeout_seconds
        )
        return self._handle_response(resp)

    def remove_document_from_collection(self, document_id: int, collection_id: int) -> None:
        resp = self.session.delete(
            self._url(f"/documents/{document_id}/collections/{collection_id}"), timeout=self.timeout_seconds
        )
        self._handle_response(resp)

    def retry_document_processing(self, document_id: int) -> Dict[str, Any]:
        resp = self.session.post(self._url(f"/documents/{document_id}/retry"), timeout=self.timeout_seconds)
        return self._handle_response(resp)

    def inspect_document(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f)}
            resp = self.session.post(
                self._url("/documents/inspect"), files=files, timeout=self.timeout_seconds
            )
            return self._handle_response(resp)

    def upload_document(
        self,
        file_path: Optional[str] = None,
        files_paths: Optional[List[str]] = None,
        chunker: Optional[str] = None,
        chunk_size: Optional[int] = None,
        overlap: Optional[int] = None,
        threshold: Optional[float] = None,
        similarity_window: Optional[int] = None,
        min_sentences_per_chunk: Optional[int] = None,
        min_characters_per_sentence: Optional[int] = None,
        chunk_overlap_percentage: Optional[float] = None,
        process_immediately: Optional[bool] = None,
        enable_preview: Optional[bool] = None,
        page_from: Optional[int] = None,
        page_to: Optional[int] = None,
    ) -> Dict[str, Any]:
        data: Dict[str, Any] = {}
        if chunker is not None:
            data["chunker"] = chunker
        if chunk_size is not None:
            data["chunk_size"] = chunk_size
        if overlap is not None:
            data["overlap"] = overlap
        if threshold is not None:
            data["threshold"] = threshold
        if similarity_window is not None:
            data["similarity_window"] = similarity_window
        if min_sentences_per_chunk is not None:
            data["min_sentences_per_chunk"] = min_sentences_per_chunk
        if min_characters_per_sentence is not None:
            data["min_characters_per_sentence"] = min_characters_per_sentence
        if chunk_overlap_percentage is not None:
            data["chunk_overlap_percentage"] = chunk_overlap_percentage
        if process_immediately is not None:
            data["process_immediately"] = process_immediately
        if enable_preview is not None:
            data["enable_preview"] = enable_preview
        if page_from is not None:
            data["page_from"] = page_from
        if page_to is not None:
            data["page_to"] = page_to

        files: List[Tuple[str, Tuple[str, Any]]] = []
        file_handles: List[Any] = []
        try:
            if file_path:
                fh = open(file_path, "rb")
                file_handles.append(fh)
                files.append(("file", (os.path.basename(file_path), fh)))
            if files_paths:
                for p in files_paths:
                    fh = open(p, "rb")
                    file_handles.append(fh)
                    files.append(("files", (os.path.basename(p), fh)))

            resp = self.session.post(
                url=self._url("/documents/upload"), data=data, files=files or None, timeout=self.timeout_seconds
            )
            return self._handle_response(resp)
        finally:
            for fh in file_handles:
                try:
                    fh.close()
                except Exception:
                    pass

    def validate_url(self, url: str) -> Dict[str, Any]:
        payload = {"url": url}
        resp = self.session.post(self._url("/documents/validate-url"), json=payload, timeout=self.timeout_seconds)
        return self._handle_response(resp)

    def fetch_document(
        self,
        url: str,
        filename: Optional[str] = None,
        chunker: Optional[str] = None,
        chunk_size: Optional[int] = None,
        overlap: Optional[int] = None,
        threshold: Optional[float] = None,
        similarity_window: Optional[int] = None,
        min_sentences_per_chunk: Optional[int] = None,
        min_characters_per_sentence: Optional[int] = None,
        chunk_overlap_percentage: Optional[float] = None,
    ) -> Dict[str, Any]:
        data: Dict[str, Any] = {"url": url}
        if filename is not None:
            data["filename"] = filename
        if chunker is not None:
            data["chunker"] = chunker
        if chunk_size is not None:
            data["chunk_size"] = chunk_size
        if overlap is not None:
            data["overlap"] = overlap
        if threshold is not None:
            data["threshold"] = threshold
        if similarity_window is not None:
            data["similarity_window"] = similarity_window
        if min_sentences_per_chunk is not None:
            data["min_sentences_per_chunk"] = min_sentences_per_chunk
        if min_characters_per_sentence is not None:
            data["min_characters_per_sentence"] = min_characters_per_sentence
        if chunk_overlap_percentage is not None:
            data["chunk_overlap_percentage"] = chunk_overlap_percentage

        resp = self.session.post(
            self._url("/documents/fetch"), data=data, timeout=self.timeout_seconds
        )
        return self._handle_response(resp)

    def preview_chunking(
        self,
        file_path: str,
        chunker: Optional[str] = None,
        chunk_size: Optional[int] = None,
        overlap: Optional[int] = None,
        page_from: Optional[int] = None,
        page_to: Optional[int] = None,
        threshold: Optional[float] = None,
        similarity_window: Optional[int] = None,
        min_sentences_per_chunk: Optional[int] = None,
        min_characters_per_sentence: Optional[int] = None,
        chunk_overlap_percentage: Optional[float] = None,
    ) -> Any:
        data: Dict[str, Any] = {}
        if chunker is not None:
            data["chunker"] = chunker
        if chunk_size is not None:
            data["chunk_size"] = chunk_size
        if overlap is not None:
            data["overlap"] = overlap
        if page_from is not None:
            data["page_from"] = page_from
        if page_to is not None:
            data["page_to"] = page_to
        if threshold is not None:
            data["threshold"] = threshold
        if similarity_window is not None:
            data["similarity_window"] = similarity_window
        if min_sentences_per_chunk is not None:
            data["min_sentences_per_chunk"] = min_sentences_per_chunk
        if min_characters_per_sentence is not None:
            data["min_characters_per_sentence"] = min_characters_per_sentence
        if chunk_overlap_percentage is not None:
            data["chunk_overlap_percentage"] = chunk_overlap_percentage

        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f)}
            resp = self.session.post(
                self._url("/documents/preview-chunking"), data=data, files=files, timeout=self.timeout_seconds
            )
            return self._handle_response(resp)

    def list_document_images(self, document_id: int) -> Any:
        resp = self.session.get(self._url(f"/documents/{document_id}/images/"), timeout=self.timeout_seconds)
        return self._handle_response(resp)

    def get_document_image(self, document_id: int, image_filename: str) -> bytes:
        resp = self.session.get(
            self._url(f"/documents/{document_id}/images/{image_filename}"), timeout=self.timeout_seconds
        )
        data = self._handle_response(resp)
        if isinstance(data, bytes):
            return data
        # If server returns JSON wrapper, serialize back to bytes for caller flexibility
        return json.dumps(data).encode("utf-8")

    def get_document_status(self, document_id: int) -> Dict[str, Any]:
        resp = self.session.get(
            self._url(f"/documents/documents/{document_id}/status"), timeout=self.timeout_seconds
        )
        return self._handle_response(resp)

    # -----------------------------
    # Collections
    # -----------------------------
    def list_collections(self, skip: int = 0, limit: int = 50) -> Dict[str, Any]:
        params = {"skip": skip, "limit": limit}
        resp = self.session.get(self._url("/collections/"), params=params, timeout=self.timeout_seconds)
        return self._handle_response(resp)

    def create_collection(
        self, name: str, description: Optional[str] = None, is_public: Optional[bool] = None
    ) -> Dict[str, Any]:
        payload: Dict[str, Any] = {"name": name}
        if description is not None:
            payload["description"] = description
        if is_public is not None:
            payload["is_public"] = is_public
        resp = self.session.post(self._url("/collections/"), json=payload, timeout=self.timeout_seconds)
        return self._handle_response(resp)

    def get_collection(self, collection_id: int) -> Dict[str, Any]:
        resp = self.session.get(self._url(f"/collections/{collection_id}"), timeout=self.timeout_seconds)
        return self._handle_response(resp)

    def update_collection(
        self,
        collection_id: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
        is_public: Optional[bool] = None,
    ) -> Dict[str, Any]:
        payload: Dict[str, Any] = {}
        if name is not None:
            payload["name"] = name
        if description is not None:
            payload["description"] = description
        if is_public is not None:
            payload["is_public"] = is_public
        resp = self.session.put(
            self._url(f"/collections/{collection_id}"), json=payload, timeout=self.timeout_seconds
        )
        return self._handle_response(resp)

    def delete_collection(self, collection_id: int) -> None:
        resp = self.session.delete(self._url(f"/collections/{collection_id}"), timeout=self.timeout_seconds)
        self._handle_response(resp)

    def get_collection_documents(
        self, collection_id: int, skip: int = 0, limit: int = 50
    ) -> List[Dict[str, Any]]:
        params = {"skip": skip, "limit": limit}
        resp = self.session.get(
            self._url(f"/collections/{collection_id}/documents"), params=params, timeout=self.timeout_seconds
        )
        return self._handle_response(resp)


def _demo() -> None:
    """Basic smoke test of key calls. Set RAG_API_KEY env var or edit below."""
    client = RAGApiClient(api_key=os.environ.get("RAG_API_KEY", "dev-secret-token"))
    print("Server:", client.base_url)
    docs = client.list_documents()
    print("Documents total:", docs.get("total"))
    cols = client.list_collections()
    print("Collections total:", cols.get("total"))


if __name__ == "__main__":
    _demo()


