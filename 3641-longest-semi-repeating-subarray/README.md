<p>You are given an integer array <code>nums</code> of length <code>n</code> and an integer <code>k</code>.</p>

<p>A <strong>semi‑repeating</strong> subarray is a contiguous subarray in which at most <code>k</code> elements repeat (i.e., appear more than once).</p>

<p>Return the length of the longest <strong>semi‑repeating</strong> subarray in <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,1,2,3,4], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest semi-repeating subarray is <code>[2, 3, 1, 2, 3, 4]</code>, which has two repeating elements (2 and 3).</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,1,1], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest semi-repeating subarray is <code>[1, 1, 1, 1, 1]</code>, which has only one repeating element (1).</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,1,1], k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest semi-repeating subarray is <code>[1]</code>, which has no repeating elements.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= nums.length</code></li>
</ul>

<p>&nbsp;</p>
<style type="text/css">.spoilerbutton {display:block; border:dashed; padding: 0px 0px; margin:10px 0px; font-size:150%; font-weight: bold; color:#000000; background-color:cyan; outline:0;
}
.spoiler {overflow:hidden;}
.spoiler > div {-webkit-transition: all 0s ease;-moz-transition: margin 0s ease;-o-transition: all 0s ease;transition: margin 0s ease;}
.spoilerbutton[value="Show Message"] + .spoiler > div {margin-top:-2000%;}
.spoilerbutton[value="Hide Message"] + .spoiler {padding:5px;}
</style>
<input class="spoilerbutton" onclick="this.value=this.value=='Show Message'?'Hide Message':'Show Message';" type="button" value="Show Message" />
<div class="spoiler">
<div>
<p><strong>FOR TESTING ONLY. WILL BE DELETED LATER.</strong></p>
// Model solution has runtime of O(n log n), O(n*n) and above should TLE.

<pre>
# Bromelia

import sys
import random, json, string
import math
import datetime
from collections import defaultdict
ri = random.randint

MAX_N   = 100_000
MAX_VAL = 100_000

def randomString(n, allowed):
    return &#39;&#39;.join(random.choices(allowed, k=n))

def randomUnique(x, y, n):
    return random.sample(range(x, y + 1), n)

def randomArray(x, y, n):
    return [ri(x, y) for _ in range(n)]

def shuffle(arr):
    random.shuffle(arr)
    return arr

def pr(a):
    file.write(str(a).replace(&quot; &quot;, &quot;&quot;).replace(&quot;\&#39;&quot;, &quot;\&quot;&quot;).replace(&quot;\&quot;null\&quot;&quot;, &quot;null&quot;) + &#39;\n&#39;)

def prstr(a):
    pr(&quot;\&quot;&quot; + a + &quot;\&quot;&quot;)


def prtc(tc):
    nums, k = tc
    pr(nums)
    pr(k)
    
def examples():
    yield ([1, 2, 3, 1, 2, 3, 4], 2)
    yield ([1, 1, 1, 1, 1], 4)
    yield ([1, 1, 1, 1, 1], 0)

def smallCases():
    yield ([MAX_VAL], 0)
    yield ([MAX_VAL], 1)

    for len in range(1, 3 + 1):
        nums = [0] * len

        def recursiveGenerate(idx: int):
            if idx == len:
                for k in range(0, len + 1):
                    yield (nums, k)
            else:
                for nextElement in range(1, len + 1):
                    nums[idx] = nextElement
                    yield from recursiveGenerate(idx + 1)

        yield from recursiveGenerate(0)

def randomCases():
    params = [
        (    4,    20,      10, 400),
        (   21,  2000,    1000, 100),
        (MAX_N, MAX_N,      10,   2),
        (MAX_N, MAX_N,     500,   2),
        (MAX_N, MAX_N, MAX_VAL,   2),
    ]
    for minLen, maxLen, maxVal, testCount in params:
        for _ in range(testCount):
            len = ri(minLen, maxLen)
            k = ri(1, len)

            nums = [0] * len
            for i in range(len):
                nums[i] = ri(1, maxVal)        

            yield (nums, k)

def cornerCases():
    yield ([MAX_VAL] * MAX_N, 0)
    yield ([MAX_VAL] * MAX_N, MAX_N)
    yield ([i for i in range(1, MAX_N + 1)], 0)
    yield ([i for i in range(1, MAX_N + 1)], MAX_N)
    yield ([i // 2 + 1 for i in range(MAX_N)], MAX_N // 2 - 1)
    yield ([i % (MAX_N // 2) + 1 for i in range(MAX_N)], MAX_N // 2 - 1)


with open(&#39;test.txt&#39;, &#39;w&#39;) as file:
    random.seed(0)
    for tc in examples(): prtc(tc)
    for tc in smallCases(): prtc(tc)
    for tc in sorted(list(randomCases()), key = lambda x: len(x[0])): prtc(tc)
    for tc in cornerCases(): prtc(tc)
</pre>
</div>
</div>
