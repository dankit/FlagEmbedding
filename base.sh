set -e

exec torchrun --nproc_per_node 1 \
    -m FlagEmbedding.finetune.reranker.encoder_only.base \
    --model_name_or_path BAAI/bge-reranker-large \
    --cache_dir ./cache/model \
    --train_data ./reranker_case_hold_dataset.jsonl \
    --cache_path ./cache/data \
    --train_group_size 3 \
    --query_max_len 256 \
    --passage_max_len 256 \
    --pad_to_multiple_of 8 \
    --knowledge_distillation False \
    --output_dir ./finetuning-checkpoints \
    --overwrite_output_dir \
    --learning_rate 2e-5 \
    --fp16 \
    --num_train_epochs 2 \
    --per_device_train_batch_size 3 \
    --gradient_accumulation_steps 1 \
    --dataloader_drop_last True \
    --warmup_ratio 0.1 \
    --weight_decay 0.01 \
    --logging_steps 200 \
    --save_steps 500 \
    --save_total_limit 3