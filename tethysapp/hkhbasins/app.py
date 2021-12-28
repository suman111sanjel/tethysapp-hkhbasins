from tethys_sdk.base import TethysAppBase, url_map_maker


class Hkhbasins(TethysAppBase):
    """
    Tethys app class for Hkhbasins.
    """

    name = 'ECMWF Streamflow Prediction Tool - HKH Basins'
    index = 'hkhbasins:home'
    icon = 'hkhbasins/images/icon.gif'
    package = 'hkhbasins'
    root_url = 'hkhbasins'
    color = '#f39c12'
    description = ''
    tags = 'ECMWF Streamflow Prediction'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='hkhbasins',
                controller='hkhbasins.controllers.index'),
            UrlMap(
                name='chart',
                url='hkhbasins/chart',
                controller='hkhbasins.controllers.chart'),
            UrlMap(
                name='forecastpercent',
                url='hkhbasins/forecastpercent',
                controller='hkhbasins.controllers.forecastpercent'),
            UrlMap(
                name='getFeatures',
                url='hkhbasins/api/getFeatures',
                controller='hkhbasins.api.getFeatures'),
            UrlMap(
                name='getreturnPeriod',
                url='hkhbasins/api/getreturnPeriod',
                controller='hkhbasins.api.getreturnPeriod'),
            UrlMap(
                name='getHistoric',
                url='hkhbasins/api/getHistoric',
                controller='hkhbasins.api.getHistoric'),
            UrlMap(
                name='getFlowDurationCurve',
                url='hkhbasins/api/getFlowDurationCurve',
                controller='hkhbasins.api.getFlowDurationCurve'),
            UrlMap(
                name='getForecast',
                url='hkhbasins/api/getForecast',
                controller='hkhbasins.api.getForecast'),
            UrlMap(
                name='getForecastCSV',
                url='hkhbasins/getForecastCSV',
                controller='hkhbasins.controllers.getForecastCSV'),
            UrlMap(
                name='getHistoricCSV',
                url='hkhbasins/getHistoricCSV',
                controller='hkhbasins.controllers.getHistoricCSV'),
        )
        return url_maps
