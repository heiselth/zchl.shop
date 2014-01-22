from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class ZchlshopLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import zchl.shop
        xmlconfig.file(
            'configure.zcml',
            zchl.shop,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'zchl.shop:default')

ZCHL_SHOP_FIXTURE = ZchlshopLayer()
ZCHL_SHOP_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ZCHL_SHOP_FIXTURE,),
    name="ZchlshopLayer:Integration"
)
ZCHL_SHOP_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ZCHL_SHOP_FIXTURE, z2.ZSERVER_FIXTURE),
    name="ZchlshopLayer:Functional"
)
