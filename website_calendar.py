# https://codefights.com/arcade/python-arcade/picturing-the-parsibilities/pTZqFk8awghQba4ba
from utils import testFunction
import calendar

def websiteCalendar(x):
    month, year = x
    return calendar.HTMLCalendar().formatmonth(year, month).replace("\n",'')


testCases = [
    ((11,2016),
     "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" class=\"month\"><tr><th colspan=\"7\" class=\"month\">November 2016</th></tr><tr><th class=\"mon\">Mon</th><th class=\"tue\">Tue</th><th class=\"wed\">Wed</th><th class=\"thu\">Thu</th><th class=\"fri\">Fri</th><th class=\"sat\">Sat</th><th class=\"sun\">Sun</th></tr><tr><td class=\"noday\">&nbsp;</td><td class=\"tue\">1</td><td class=\"wed\">2</td><td class=\"thu\">3</td><td class=\"fri\">4</td><td class=\"sat\">5</td><td class=\"sun\">6</td></tr><tr><td class=\"mon\">7</td><td class=\"tue\">8</td><td class=\"wed\">9</td><td class=\"thu\">10</td><td class=\"fri\">11</td><td class=\"sat\">12</td><td class=\"sun\">13</td></tr><tr><td class=\"mon\">14</td><td class=\"tue\">15</td><td class=\"wed\">16</td><td class=\"thu\">17</td><td class=\"fri\">18</td><td class=\"sat\">19</td><td class=\"sun\">20</td></tr><tr><td class=\"mon\">21</td><td class=\"tue\">22</td><td class=\"wed\">23</td><td class=\"thu\">24</td><td class=\"fri\">25</td><td class=\"sat\">26</td><td class=\"sun\">27</td></tr><tr><td class=\"mon\">28</td><td class=\"tue\">29</td><td class=\"wed\">30</td><td class=\"noday\">&nbsp;</td><td class=\"noday\">&nbsp;</td><td class=\"noday\">&nbsp;</td><td class=\"noday\">&nbsp;</td></tr></table>"),
    ((1,1900),
    "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" class=\"month\"><tr><th colspan=\"7\" class=\"month\">January 1900</th></tr><tr><th class=\"mon\">Mon</th><th class=\"tue\">Tue</th><th class=\"wed\">Wed</th><th class=\"thu\">Thu</th><th class=\"fri\">Fri</th><th class=\"sat\">Sat</th><th class=\"sun\">Sun</th></tr><tr><td class=\"mon\">1</td><td class=\"tue\">2</td><td class=\"wed\">3</td><td class=\"thu\">4</td><td class=\"fri\">5</td><td class=\"sat\">6</td><td class=\"sun\">7</td></tr><tr><td class=\"mon\">8</td><td class=\"tue\">9</td><td class=\"wed\">10</td><td class=\"thu\">11</td><td class=\"fri\">12</td><td class=\"sat\">13</td><td class=\"sun\">14</td></tr><tr><td class=\"mon\">15</td><td class=\"tue\">16</td><td class=\"wed\">17</td><td class=\"thu\">18</td><td class=\"fri\">19</td><td class=\"sat\">20</td><td class=\"sun\">21</td></tr><tr><td class=\"mon\">22</td><td class=\"tue\">23</td><td class=\"wed\">24</td><td class=\"thu\">25</td><td class=\"fri\">26</td><td class=\"sat\">27</td><td class=\"sun\">28</td></tr><tr><td class=\"mon\">29</td><td class=\"tue\">30</td><td class=\"wed\">31</td><td class=\"noday\">&nbsp;</td><td class=\"noday\">&nbsp;</td><td class=\"noday\">&nbsp;</td><td class=\"noday\">&nbsp;</td></tr></table>"),
]


testFunction(testCases, websiteCalendar, 'websiteCalendar')
