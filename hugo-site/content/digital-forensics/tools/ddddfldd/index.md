---
title: "dd, dcfldd, dc3dd Data Acquisition Tools for Linux"
summary: "Understanding dd, dcfldd, and dc3dd commands."
summaryImage: "summary.jpg"
tags: ["data-acquisition", "linux"]
url: "/category/tools/ddddfldd/"
---

<h1 id="using-dddcflddd3cdd-command-line-tools-for-computer-foresnic-data-acquisition">Using dd,dcfldd,d3cdd command line tools for Computer foresnic data acquisition</h1>
<p>We will learn to create forensic image of a storage drive(In my case pendrive) using commandline tools</p>
<hr>
<p><a href="https://www.youtube.com/watch?v=q0GtDP_HNsw">Click here to  watch this lab on youtube</a></p>
<h2 id="prerequisite"><em>Prerequisite</em></h2>
<ol>
<li>You should have any 64bit Linux OS</li>
<li>Active internet connection</li>
<li>One pendrive connected to Linux OS. I used 8GB pendrive</li>
<li>You can check whether your pendrive is connected or not using  <strong>fdisk</strong> command</li>
</ol>
<p><em>fdisk output in my case is as follow</em></p>
<p><img src="/img/fdiskoutput.jpg" alt="fdiskoutput" title="Check Yellow markings"></p>
<hr>
<h2 id="a-dd-command">A) dd command</h2>
<ol>
<li>dd command in digital forensic help investigator to take create image file of suspect’s storage drive.</li>
<li>dd command can be used to clone not only internal partitions but also external storage drives attached to machine.</li>
</ol>
<p><strong>Example command</strong></p>
<div class="highlight"><pre style="color:#f8f8f2;background-color:#272822;-moz-tab-size:4;-o-tab-size:4;tab-size:4"><code class="language-bash" data-lang="bash">    dd <span style="color:#66d9ef">if</span><span style="color:#f92672">=</span>/dev/sdb  bs<span style="color:#f92672">=</span><span style="color:#ae81ff">4096</span> of<span style="color:#f92672">=</span>/home/coep/Desktop/firstimage.dd conv<span style="color:#f92672">=</span>noerror,sync status<span style="color:#f92672">=</span>progress
</code></pre></div><p><strong>Command execution in kali linux</strong></p>
<p><img src="/img/ddcmd.jpg" alt="dd execution" title="After this execution check your created image file"></p>
<p>Command will clone my pendrive(/dev/sdb) and store image of it  on desktop as follow.</p>
<p><img src="/img/ddoutput.jpg" alt="dd output" title="It created image file on desktop"></p>
<p>Thus we cloned and created image file of  pendrive succesfully using dd command.</p>
<hr>
<h2 id="b-dcfldd-command">B) dcfldd command</h2>
<p>It is enhanced verion of dd command</p>
<p>Useful feature for forensic investigator :</p>
<ul>
<li>On-the-fly hashing of the transmitted data.</li>
<li>Progress bar of how much data has already been<br>
sent.</li>
<li>Wiping of disks with known patterns.
Verification that the image is identical to the original drive, bit-for-bit.</li>
<li>Simultaneous output to more than one file/disk is possible.</li>
<li>The output can be split into multiple files.
Logs and data can be piped into external applications.</li>
</ul>
<p><strong>For installing in kali linux</strong></p>
<div class="highlight"><pre style="color:#f8f8f2;background-color:#272822;-moz-tab-size:4;-o-tab-size:4;tab-size:4"><code class="language-bash" data-lang="bash">    sudo apt-get install dcfldd
</code></pre></div><p><strong>Example Command</strong></p>
<div class="highlight"><pre style="color:#f8f8f2;background-color:#272822;-moz-tab-size:4;-o-tab-size:4;tab-size:4"><code class="language-bash" data-lang="bash">dcfldd <span style="color:#66d9ef">if</span><span style="color:#f92672">=</span>/dev/sdb hash<span style="color:#f92672">=</span>md5,sha256 hashwindow<span style="color:#f92672">=</span>2G md5log<span style="color:#f92672">=</span>md5.txt sha256log<span style="color:#f92672">=</span>sha256.txt hashconv<span style="color:#f92672">=</span>after bs<span style="color:#f92672">=</span>4k conv<span style="color:#f92672">=</span>noerror,sync split<span style="color:#f92672">=</span>2G splitformat<span style="color:#f92672">=</span>aa of<span style="color:#f92672">=</span>sdb_image.dd
</code></pre></div><p><strong>Command execution in kali linux</strong></p>
<p><img src="/img/dcflddexecution.jpg" alt="dcfldd execution" title="It will create four image files"></p>
<blockquote>
<p>Above command will create four output files named</p>
<p>sdb_image.dd.aa, sdb_image.dd.ab, sdb_image.dd.ac, sdb_image.dd.ad</p>
</blockquote>
<p>and will  also create two files called <em>md5.txt</em> and <em>sha256.txt</em> containing hash values of output files.</p>
<p><img src="/img/dcflddoutput.jpg" alt="dcfldd output" title="It has splitted image of my 8 GB pendrive into four files "></p>
<p>Note: <em>dcfldd is based on older version of dd. Research found that it is unstable hence it’s use should be strictly avoided during real forensic investigation.</em></p>
<hr>
<h2 id="c-dc3dd-command">C) dc3dd command</h2>
<p>dc3dd is based on patched version of dd command.It is worth noting that dcfldd is fork of GNU dd command whereas dc3dd is a patch to current version of dd.</p>
<p><strong>Few notable Features</strong></p>
<ul>
<li>Support direct input/output mode</li>
<li>On the fly hashing with multiple algorithms(MD5,SHA-1,SHA-256 and SHA-512)</li>
<li>Combined error logs. Group error together.</li>
<li>Pattern wiping. Wipe output files with a single hex digit or a text pattern</li>
<li>Verify mode</li>
<li>Progress report</li>
<li>Able to split output files in fixed sized chunk</li>
</ul>
<p><strong>For installing in kali linux</strong></p>
<div class="highlight"><pre style="color:#f8f8f2;background-color:#272822;-moz-tab-size:4;-o-tab-size:4;tab-size:4"><code class="language-bash" data-lang="bash">    sudo apt-get install dc3dd
</code></pre></div><p><strong>Example Command</strong></p>
<div class="highlight"><pre style="color:#f8f8f2;background-color:#272822;-moz-tab-size:4;-o-tab-size:4;tab-size:4"><code class="language-bash" data-lang="bash">    dc3dd <span style="color:#66d9ef">if</span><span style="color:#f92672">=</span>/dev/sdb  of<span style="color:#f92672">=</span>/home/coep/Desktop/dc3dd_pdimage.dd hash<span style="color:#f92672">=</span>md5 log<span style="color:#f92672">=</span>/home/coep/Desktop/dc3ddpdlog.log
</code></pre></div><p><strong>Command execution in kali linux</strong></p>
<p><img src="/img/dc3ddexecution.jpg" alt="dcfldd execution" title="It will createimage file amd hash log on desktop"></p>
<p>This will create output on desktop in two files one will be image file <strong>dc3dd_pdimage.dd</strong> and another file will be <strong>dc3ddpdlog.log</strong></p>
<p><img src="/img/dc3ddoutput.jpg" alt="dc3dd output" title="It will create image file on desktop "></p>
<hr>
<p>Thus we learned three command line tools for data acquision.</p>
<blockquote>
<p>In video I have also calculated on the fly hash of images.
<a href="https://www.youtube.com/watch?v=q0GtDP_HNsw">Do check it !!</a></p>
</blockquote>
<p>Thanks!!!!!!!!!!!!!!!!!!!!!!!!!!!! :)</p>
<hr>
<h2 id="references">References</h2>
<p><a href="https://forensicswiki.xyz/wiki/index.php?title=Dcfldd">forensicwiki</a></p>
