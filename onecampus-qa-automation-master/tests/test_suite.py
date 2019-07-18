import unittest
from tests.dashboard.Dashboard_BestOC import Best_OC
from tests.dashboard.Dashboard_FeaturedCollection import Feature_Collection
from tests.dashboard.Dashboard_FirstScreen import First_Screen
from tests.dashboard.Dashboard_GlobalNetwork import Global_Network
from tests.dashboard.Dashboard_JobsOfTheFuture import Jobs_of_the_Future
from tests.dashboard.Dashboard_TopicSection import Topic_Section
from utilities.teststatus import TestStatus



tc1 = unittest.TestLoader().loadTestsFromTestCase(Best_OC)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Feature_Collection)
tc3 = unittest.TestLoader().loadTestsFromTestCase(First_Screen)
tc4 = unittest.TestLoader().loadTestsFromTestCase(Global_Network)
tc5 = unittest.TestLoader().loadTestsFromTestCase(Jobs_of_the_Future)
tc6 = unittest.TestLoader().loadTestsFromTestCase(Topic_Section)

# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6])

unittest.TextTestRunner(verbosity=2).run(smokeTest)