.PHONY: test clean
all:
	$(MAKE) -C libmegahal

test:
	$(MAKE) -C test

clean:
	$(MAKE) -C libmegahal clean
	$(MAKE) -C test clean
