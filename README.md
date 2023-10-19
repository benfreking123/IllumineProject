# Illumine Project - Obsidian Vault



## Setup

1. Open Obsidian to Sync Vault
2. cd to IllumineProject
3. run main.py
2. npx quartz create (Only to create Index)
3. Push & Commit Repositroy
4. [Deploy Workflow](https://github.com/benfreking123/IllumineProject/actions/workflows/deploy.yml)
(Hosted at https://benfreking123.github.io/IllumineProject/)
OR
5. npx quartz build --serve



I found a fix to the issue in line 411 of the fill plugins>transformers>ofm.ts in the if statement "if (opts.parseTags)"

url: base + /IllumineProject/tags/${tag}
revert back to:
url: base + /tags/${tag}

I added an addition of /IllumineProject as a hot fix, I am assuming that somewhere in the bodyPage generation the tag url's are being sliced stangely. This fix did not great the TagList Component either
I'd love a true fix, but for now I will make do with this