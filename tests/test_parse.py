from scraper.parse import Parser


def test_parse_articles_extracts_title():
    sample_html = """
        <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/tipping-the-velvet_999/index.html"><img src="media/cache/26/0c/260c6ae16bce31c8f8c95daddd9f4a1c.jpg" alt="Tipping the Velvet" class="thumbnail"></a>
            </div>
            <p class="star-rating One"> <i class="icon-star"></i> <i class="icon-star"></i> <i class="icon-star"></i> <i class="icon-star"></i> <i class="icon-star"></i> </p>
            <h3><a href="catalogue/tipping-the-velvet_999/index.html" title="Tipping the Velvet">Tipping the Velvet</a></h3>
            <div class="product_price">
            <p class="price_color">£53.74</p> <p class="instock availability"> <i class="icon-ok"></i> In stock </p> <form> <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
            </form> </div> </article>
        """

    result = Parser(sample_html).parse_articles()

    assert len(result) == 1
    assert result[0]["title"] == "Tipping the Velvet"
    assert result[0]["rating"] == "One"
    assert result[0]["price"] == "£53.74"
    assert result[0]["img"] == "media/cache/26/0c/260c6ae16bce31c8f8c95daddd9f4a1c.jpg"


def test_title_missing():
    sample_html = """
        <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/tipping-the-velvet_999/index.html"><img src="media/cache/26/0c/260c6ae16bce31c8f8c95daddd9f4a1c.jpg" alt="Tipping the Velvet" class="thumbnail"></a>
            </div>
            <p class="star-rating One"> <i class="icon-star"></i> <i class="icon-star"></i> <i class="icon-star"></i> <i class="icon-star"></i> <i class="icon-star"></i> </p>
            <div class="product_price">
            <p class="price_color">£53.74</p> <p class="instock availability"> <i class="icon-ok"></i> In stock </p> <form> <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
            </form> </div> </article>
        """
    result = Parser(sample_html).parse_articles()

    assert len(result) == 1
    assert result[0]["title"] == ""
    assert result[0]["rating"] == "One"
    assert result[0]["price"] == "£53.74"
    assert result[0]["img"] == "media/cache/26/0c/260c6ae16bce31c8f8c95daddd9f4a1c.jpg"
