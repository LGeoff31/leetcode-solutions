<p>You are given an integer array <code>nums</code>. A <strong>good </strong><span data-keyword="subsequence-array">subsequence</span> is defined as a subsequence of <code>nums</code> where the absolute difference between any <strong>two</strong> consecutive elements in the subsequence is <strong>exactly</strong> 1.</p>

<p>Return the <strong>sum</strong> of all <em>possible</em> <strong>good subsequences</strong> of <code>nums</code>.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p><strong>Note </strong>that a subsequence of size 1 is considered good by definition.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Good subsequences are: <code>[1]</code>, <code>[2]</code>, <code>[1]</code>, <code>[1,2]</code>, <code>[2,1]</code>, <code>[1,2,1]</code>.</li>
	<li>The sum of elements in these subsequences is 14.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">40</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Good subsequences are: <code>[3]</code>, <code>[4]</code>, <code>[5]</code>, <code>[3,4]</code>, <code>[4,5]</code>, <code>[3,4,5]</code>.</li>
	<li>The sum of elements in these subsequences is 40.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
