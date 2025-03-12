import pytest

from .data import catalogue_data, season_data

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_seasons():
    assert season_data.one_piece == await catalogue_data.one_piece.seasons()
    assert season_data.mha == await catalogue_data.mha.seasons()
    assert season_data.gumball == await catalogue_data.gumball.seasons()


@pytest.mark.asyncio
async def test_avancement():
    assert (
        await catalogue_data.one_piece.advancement()
        == "La suite sortira à partir d'avril 2025"
    )
    assert await catalogue_data.gumball.advancement() == "Aucune donnée."
    assert (
        await catalogue_data.mha.advancement() == "La saison 8 sortira en automne 2025"
    )


@pytest.mark.asyncio
async def test_correspondance():
    assert (
        await catalogue_data.one_piece.correspondance()
        == "Episode 1122 -> Chapitre 1088"
    )
    assert await catalogue_data.gumball.correspondance() == "Aucune donnée."
    assert (
        await catalogue_data.mha.correspondance()
        == "Saison 7 Épisode 21 -> Chapitre 399"
    )
