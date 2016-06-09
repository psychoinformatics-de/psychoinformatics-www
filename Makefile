PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
TMPDIR=$(BASEDIR)/tmp

SSH_HOST=kumo.ovgu.de
SSH_PORT=22
SSH_USER=git
SSH_TARGET_DIR=/var/www/psychoinformatics/www
RSYNC_OPTS = -rzhv -P --delete --copy-links --exclude drafts

VER_FONTAWESOME=4.6.3

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make devserver [PORT=8000]          start/restart develop_server.sh    '
	@echo '   make stopserver                     stop local server                  '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '                                                                          '
	@echo '   make updatedeps                     update all website dependencies    '
	@echo '                                          see makefile for additional     '
	@echo '                                          dependency targets              '
	@echo '   make fontawesome                    download and extract FontAwesome   '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)
	[ ! -d $(TMPDIR) ] || rm -rf $(TMPDIR)
	pyclean ./

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

stopserver:
	$(BASEDIR)/develop_server.sh stop
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

ssh_upload: publish
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

updatedeps: $(TMPDIR) fontawesome

$(TMPDIR):
	mkdir -p $@

fontawesome:
	curl -L -o $(TMPDIR)/fa.zip https://github.com/FortAwesome/Font-Awesome/archive/v$(VER_FONTAWESOME).zip
	unzip -j $(TMPDIR)/fa.zip Font-Awesome-$(VER_FONTAWESOME)/css/font-awesome.min.css -d pelican-theme/static/css/
	unzip -j $(TMPDIR)/fa.zip Font-Awesome-$(VER_FONTAWESOME)/fonts/*webfont* -d pelican-theme/static/fonts/

.PHONY: html help clean regenerate devserver publish ssh_upload rsync_upload updatedeps fontawesome
