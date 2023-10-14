from flask import Blueprint, request, render_template, jsonify
from hotel_service import HotelService


hotels_bp = Blueprint(
    "hotels",
    __name__,
    url_prefix="/hotels",
    template_folder="templates",
)


@hotels_bp.get("/")
def index():
    return render_template("index.html")


@hotels_bp.get("/search")
def render_search_hotels():
    return render_template("hotel_search.html")


@hotels_bp.post("/search")
def search_hotels():
    page = int(request.form.get("page") or 1)
    limit = int(request.form.get("limit") or 10)
    keyword = request.form.get("keyword", "").strip()
    if len(keyword) < 3:
        return jsonify({"error": "keyword must be at least 3 characters long"}), 400

    results = HotelService().search(keyword=keyword, page=page, limit=limit)

    return render_template(
        "results.html",
        results=results,
        keyword=keyword,
        current_page=page,
        limit=limit,
        context="search",
    )


@hotels_bp.get("/browse")
def browse_hotels():
    page = int(request.args.get("page") or 1)
    limit = int(request.args.get("limit") or 10)

    results = HotelService().browse(page=page, limit=limit)

    return render_template(
        "results.html",
        results=results,
        current_page=page,
        limit=limit,
        context="browse",
    )
 