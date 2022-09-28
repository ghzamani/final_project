python few_shot.py \
  --language persian \
  --model_weights=/mnt/NLP992-Vol2/clip_captions_weights/project_train_10_20_gpt-001.pt \
  --categories_path=/home/ubuntu/Zamani-Mobasher/final_project/clip_prefix_caption/data_preperation/zeroshot_fewshot/ \
  --image_path=/home/ubuntu/Zamani-Mobasher/final_project/clip_prefix_caption/data_preperation/zeroshot_fewshot/ \
  --prefix_length_clip=20 \
  --prefix_length=10 \
  --prefix_size=768 \
  --out_dir=./few_shot_weights/ \
  --shots=16 \
  --epochs=5 \
  --lr=2e-6