from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def xpath(driver, path, wait=0, error='no'):
	

def xpaths(driver, path, wait=0, error='no'):

def classname(driver, path, wait=0, error='no'):

def classnames(driver, path, wait=0, error='no'):

def id(driver, path, wait=0, error='no'):

def ids(driver, path, wait=0, error='no'):

def name(driver, path, wait=0, error='no'):

def names(driver, path, wait=0, error='no'):

def linktext(driver, path, wait=0, error='no'):

def linktexts(driver, path, wait=0, error='no'):

def partiallinktext(driver, path, wait=0, error='no'):

def partiallinktexts(driver, path, wait=0, error='no'):

def tagname(driver, path, wait=0, error='no'):

def tagnames(driver, path, wait=0, error='no'):

def cssselector(driver, path, wait=0, error='no'):

def cssselectors(driver, path, wait=0, error='no'):

