# DeepBytes Hugo Site

This is the rebuild of the digital forensic blog using the Hugo Refresh theme.
The original generated site remains in the parent folder as a backup.

## Write a post

Create a Markdown file inside the appropriate folder under `content/`, add front matter, and write the post body.

```text
content/digital-forensics/my-new-post.md
content/ceh-malware-analysis/my-new-post.md
content/soc-operations/my-new-post.md
```

Digital Forensics also has these sub-sections:

```text
content/digital-forensics/guides/
content/digital-forensics/tools/
content/digital-forensics/case-studies/
```

Preview locally with `hugo server -D` and build with `hugo`. The generated deployment files are written to `public/`.
