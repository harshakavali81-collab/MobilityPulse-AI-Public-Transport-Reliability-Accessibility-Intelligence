install:
	python -m pip install -r requirements.txt
	python -m pip install -e .
demo:
	python scripts/generate_demo.py
api:
	uvicorn backend.app.main:app --reload --port 8000
test:
	pytest -q
exports:
	python scripts/export_powerbi.py
model:
	python -m mobilitypulse.models.train_delay_model --allow-synthetic
web:
	cd frontend && npm install && npm run dev
docker:
	docker compose up --build
