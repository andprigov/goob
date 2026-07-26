class Statistics:

    def show(

        self,

        records

    ):

        print()

        print("Crawl Statistics\n")

        print(

            f"Processed: {len(records)}"

        )

        print(

            f"Keywords: {sum(len(r['keywords']) for r in records)}"

        )
