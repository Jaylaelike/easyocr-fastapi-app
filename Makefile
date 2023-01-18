serve:
	cd src && uvicorn main:app --reload

freeze:
	rm -f requirements.txt && pip freeze > requirements.txt

test:
	time curl -v -X POST -F file=@./test/test.jpg  localhost:8000/ocr

.PHONY: test freeze serve
