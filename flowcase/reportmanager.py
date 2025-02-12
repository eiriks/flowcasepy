import datetime
import logging
import time
from typing import Optional

import requests

log = logging.getLogger(__name__)


class ReportManager:
    def __init__(self, url, auth_header, verbose=False):
        self.url = url
        self._auth_header = auth_header
        self.verbose = verbose

    # REPORTS
    # referance case reports
    # Step 1: Initiate Report Request
    def initiate_report(self) -> str:
        request_data = {
            "offset": 0,
            "size": 100,
            "must": [],
            "workflow_stage_filter": "live",
            "filter_owned": False,
            "output_format": "xlsx",
        }

        response = requests.post(self.url, json=request_data, headers=self._auth_header)
        if response.status_code == 200:
            return response.json()["id"]  # ["_id"]
        else:
            raise Exception(f"Failed to initiate report: {response.status_code}")

    # Trinn 2: Pulle for å sjekke om rapporten er ferdig
    def pull_report_status(self, report_id: str) -> str:
        """Pull to check if the report is finished."""
        url = f"{self.url}/{report_id}"
        log.debug(f"Polling report status at {url}")

        while True:
            response = requests.get(url, headers=self._auth_header)
            report_data = response.json()

            percent_processed = report_data.get("percentProcessed", 0)
            state = report_data.get("status", "started")

            log.debug(f"Report processing: {percent_processed}%")

            if state == "finished":
                file_url = report_data.get("file").get("url")
                if file_url:
                    log.debug("Report is finished!")
                    return file_url
                else:
                    raise Exception("Report finished, but no file URL found.")
            log.debug(report_data)
            log.debug("Waiting 5s for report to finish...")
            time.sleep(5)  # Wait 5 seconds before next polling

    # Trinn 3: Last ned rapportfilen fra den signerte URL-en
    def download_report_file(self, file_url, output_path):
        response = requests.get(file_url)

        if response.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(response.content)
            if self.verbose:
                print(f"Report downloaded successfully: {output_path}")
        else:
            raise Exception(
                f"Error downloading file: {response.status_code}, {response.text}"
            )

    # fiannlay do all the things
    # get todays year as YYYY and month as MM and day as DD in a string

    # def generate_report(self):
    #     return self.report.generate_report()

    def generate_report(self, output_filename: Optional[str] = None) -> str:
        print("initiating report")
        report_id = self.initiate_report()
        print("pulling report status")
        file_url = self.pull_report_status(report_id)

        # make a filename with todays date
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        if not output_filename:
            output_filename = f"reference_report_{today}.xlsx"
        else:
            output_filename = f"{output_filename}_{today}.xlsx"

        print(f"downloading report file to {output_filename}")
        self.download_report_file(file_url, output_filename)
        return output_filename
