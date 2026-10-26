---
name: "reference-requirements-txt-for-the-ins-215d350e67c17118"
description: "Shows how to fix reference requirements.txt for the install_requires kwarg in setuptools setup.py file. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_U7ZCSo9j3JWq5a2cJ3LVkQ"
  title: "Reference requirements.txt for the install_requires kwarg in setuptools setup.py file"
  version: "skv_ElmOwHOcflTfsbjVmcvsyA"
  updated: "2026-10-04T05:39:13.557762+00:00"
  canonical_url: "https://vectle.com/skills/skl_U7ZCSo9j3JWq5a2cJ3LVkQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/14399534/reference-requirements-txt-for-the-install-requires-kwarg-in-setuptools-setup-py\"]"
---

## TL;DR

Alternatively, even if not advised, it is still possible to parse the requirements.txt file (if it doesn't refer any external requirements by URL) with the following hack (tested with pip 9.0.1 ): install_reqs = parse_requirements('requirements.txt', session='hack') This doesn't filter environment markers though.

## When to use

You are seeing this: In old versions of pip, more specifically older than 6.0 , there is a public API that can be used to achieve this. Use this skill when you run into "Reference requirements.txt for the install_requires kwarg in setuptools setup.py file".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: pip 9.0.1, django 1.5.1, mezzanine 1.4.6, guessitgt 0.5.2, tvdb_apigt 1.8.2, hachoir-metadatagt 1.3.3, hachoir-parsergt 1.3.4. If you are on something much newer or older, the details may have shifted.

Update 12/2024: This does not work in recent versions of Python, primarily because the function has been moved around in the pip module. Either way, as stated below by maintainers of the library, it is not recommended to import and use this function, as it is an internal function which is subject to change and being moved around. Old answer: You can flip it around and list the dependencies in setup.py and have a single character , a dot . , in requirements.txt instead. Alternatively, even if not advised, it is still possible to parse the requirements.txt file (if it doesn't refer any external requirements by URL) with the following hack (tested with pip 9.0.1 ): install_reqs = parse_requirements('requirements.txt', session='hack') This doesn't filter environment markers though. In old versions of pip, more specifically older than 6.0 , there is a public API that can be used to achieve this. A requirement file can contain comments ( # ) and can include some other files ( --requirement or -r ). Thus, if you really want to parse a requirements.txt you can use the pip parser: from pip.req import parse_requirements # parse_requirements() returns generator of pip.req.InstallRequirement objects install_reqs = parse_requirements([requirements_path]) # reqs is a list of requirement # e.g. ['django==1.5.1', 'mezzanine==1.4.6'] reqs = [str(ir.req) for ir in install_reqs] setup( ... install_requires=reqs )

Context: I have a requirements.txt file that I'm using with Travis-CI. It seems silly to duplicate the requirements in both requirements.txt and setup.py , so I was hoping to pass a file handle to the install_requires kwarg in setuptools.setup . Is this possible? If so, how should I go about doing it? Here is my requirements.txt file: guessit&gt;=0.5.2 tvdb_api&gt;=1.8.2 hachoir-metadata&gt;=1.3.3 hachoir-core&gt;=1.3.3 hachoir-parser&gt;=1.3.4


---

Source: [Vectle](https://vectle.com/skills/skl_U7ZCSo9j3JWq5a2cJ3LVkQ). Version: `skv_ElmOwHOcflTfsbjVmcvsyA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
