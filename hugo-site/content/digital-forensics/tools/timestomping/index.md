---
title: "NTFS and ext4 File Stomping"
summary: "Manipulating timestamps of files stored in NTFS or ext4 file systems."
summaryImage: "summary.jpg"
tags: ["lab3", "linux"]
url: "/category/tools/timestomping/"
---

<h1 id="ntfs-and-ext4-file-stomping">NTFS and ext4 File Stomping</h1>
<p><em>We will learn to manipulate timestamps of file systems. First I will show you how to change timestamps of NTFS file system using setmace tool and then we will manipulate ext4 file system timestamps in linux</em></p>
<hr>
<h2 id="a--ntfs-time-stomping">A)  NTFS Time stomping</h2>
<h5 id="prerequisite">Prerequisite</h5>
<ol>
<li>
<p>You should have windows xp/7/8 to perform this lab. I have not tested this tool on windows 10/11.</p>
</li>
<li>
<p>Download setmace tool from following link 
<a href="https://github.com/jschicht/SetMace/blob/master/SetMace.exe">setmace.exe official download link</a></p>
</li>
<li>
<p>Store above downloaded file <strong>Setmace.exe</strong>  on desktop.</p>
</li>
<li>
<p>Create and store one sample text file(In my case sids.txt). We will change timestamps of this file.</p>
</li>
</ol>
<blockquote>
<p>Note : store setmace.exe and your text file on different windows storage drives(C,D,E,..).</p>
<p>For example:  Store <strong>setmace.exe</strong> on desktop (Say C:\Admin\Desktop)   and store text file <strong>sids.txt</strong> on D drive (Say D:\sids.txt)</p>
</blockquote>
<h5 id="procedure-for-ntfs-time-stomping">Procedure for NTFS Time stomping</h5>
<ol>
<li>First I will check current timestamp on my sids.txt file</li>
</ol>
<p><img src="/img/timestomp/previous_timestamp_NTFS.jpg" alt="Current timestamp " title="It will show current timestamp of sids.txt"></p>
<ol start="2">
<li>
<p>Now I will change <strong>creation timestamp</strong> of sids.txt file. For that open command prompt(with admin privliege)
and change directory where you have kept <strong>setmace.exe</strong> file. (In my case Desktop)</p>
</li>
<li>
<p>Run following command.It will change file creation timestamp</p>
</li>
</ol>
<div class="highlight"><pre style="color:#f8f8f2;background-color:#272822;-moz-tab-size:4;-o-tab-size:4;tab-size:4"><code class="language-bash" data-lang="bash">C:<span style="color:#ae81ff">\U</span>sers<span style="color:#ae81ff">\j</span>ohn<span style="color:#ae81ff">\D</span>esktop>SetMace.exe E:<span style="color:#ae81ff">\s</span>ids.txt -c <span style="color:#e6db74">"2000:01:01:00:00:00:789:1234"</span>-si
</code></pre></div><p><img src="/img/timestomp/execution_of_command.jpg" alt="Execution of setmace tool. Creation timestamp being changed" title="It will change current timestamp of sids.txt"></p>
<p>We can see changed creation timestamp of file.As shown below.</p>
<p><img src="/img/timestomp/changed_created_timestamp.jpg" alt="changed timesamp "></p>
<ol start="4">
<li>Now I will change <strong>Last accessed</strong> time stamp of sids.txt file. Follow above steps as it is. Just insert following command in command prompt.</li>
</ol>
<div class="highlight"><pre style="color:#f8f8f2;background-color:#272822;-moz-tab-size:4;-o-tab-size:4;tab-size:4"><code class="language-bash" data-lang="bash">C:<span style="color:#ae81ff">\U</span>sers<span style="color:#ae81ff">\j</span>ohn<span style="color:#ae81ff">\D</span>esktop>SetMace.exe E:<span style="color:#ae81ff">\s</span>ids.txt -a <span style="color:#e6db74">"2000:01:01:00:00:00:789:1234"</span> -si
</code></pre></div><p>above command Execution will look like this.</p>
<p><img src="/img/timestomp/setmace_lastaccess_execution.jpg" alt="Command execution for changing last accessed timestamp"></p>
<p>After succesfull execution.We can check changed last accessed timestamp.</p>
<p><img src="/img/timestomp/setmace_lastaccess_output.jpg" alt="Changed last accessed timestamp"></p>
<blockquote>
<p>Similarly we can change various timestamps of NTFS file systems. 
You can perform more time stamp manipulations by  following official <a href="https://github.com/jschicht/SetMace">documentation</a></p>
</blockquote>
<hr>
<hr>
<h2 id="b-ext4-time-stomping">B) ext4 Time Stomping</h2>
<h5 id="prerequisite-1">Prerequisite</h5>
<ol>
<li>You should have linux OS.You can change timestamp of any  file on this system.
I will change timestamp of <strong>sids.pdf</strong>  file which is stored on  desktop of my ubuntu(SANS SIFT) linux distro.</li>
</ol>
<h5 id="procedure-">Procedure :</h5>
<ol>
<li>We will check time stamp of <strong>sids.pdf</strong>  file.</li>
</ol>
<blockquote>
<p>Note: We also need another pdf file (In my case <strong>Network-Forensics-Poster.pdf</strong>) whose timestamp we will assign to <strong>sids.pdf</strong> 
.Thus before manipulation of timestamp, I will check timestamp of both pdf files.</p>
</blockquote>
<ol start="2">
<li>Now we will use <strong>touch</strong> command to change timestamp of <strong>sids.pdf</strong> file.</li>
</ol>
<div class="highlight"><pre style="color:#f8f8f2;background-color:#272822;-moz-tab-size:4;-o-tab-size:4;tab-size:4"><code class="language-bash" data-lang="bash">sudo touch -r Network-Forensics-Poster.pdf sids.pdf
</code></pre></div><p><img src="/img/timestomp/ext4_timestomping.png" alt="ext4 file stomping"></p>
<hr>
<h2 id="conclusion">Conclusion</h2>
<p>Thus using setmace tool we changed timestamp in NTFS File system. 
Using simple touch command we changed ext4 file system timestamp.</p>
