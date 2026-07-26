from config import OUTPUT_FILE

from sources.source_loader import SourceLoader
from sources.url_filter import UrlFilter

from parsers.html_parser import HtmlParser
from parsers.metadata_parser import MetadataParser
from parsers.keyword_parser import KeywordParser

from storage.repository import Repository
from storage.json_writer import JsonWriter

from reports.statistics import Statistics

from utils.cleaner import Cleaner
from utils.logger import Logger

logger = Logger()

records = []

loader = SourceLoader()

for source in loader.load():

    if not UrlFilter().valid(source):

        continue

    html = Cleaner().normalize(

        source["html"]

    )

    title = HtmlParser().title(

        html

    )

    metadata = MetadataParser().build(

        source,

        title

    )

    keywords = KeywordParser().extract(

        html

    )

    records.append(

        Repository().collect(

            metadata,

            keywords

        )

    )

    logger.info(

        f"Processed {source['url']}"

    )

JsonWriter().save(

    records,

    OUTPUT_FILE

)

Statistics().show(

    records

)
